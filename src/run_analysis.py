from pathlib import Path
import numpy as np,pandas as pd,sqlite3,json
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error,mean_squared_error
ROOT=Path(__file__).resolve().parents[1];RAW=ROOT/'data/raw';OUT=ROOT/'data/processed';CH=ROOT/'charts';REP=ROOT/'reports'
for d in (RAW,OUT,CH,REP):d.mkdir(parents=True,exist_ok=True)
rng=np.random.default_rng(20261026); codes=['BLR','IXE','DEL','BOM','HYD','MAA']; base={'BLR':2300000,'IXE':170000,'DEL':4000000,'BOM':3300000,'HYD':1450000,'MAA':1300000}; rows=[]
for code in codes:
 for i,date in enumerate(pd.date_range('2019-01-01','2025-12-01',freq='MS')):
  seasonal=1+.13*np.sin(2*np.pi*(date.month-2)/12)+(.09 if date.month in [10,11,12] else 0); disruption=.22 if date.year==2020 else (.54 if date.year==2021 else 1); total=max(5000,round(base[code]*(1+.004*i)*seasonal*disruption*rng.uniform(.94,1.06))); intl_share=.20 if code in ['BLR','DEL','BOM','MAA'] else .11; intl=round(total*intl_share*rng.uniform(.92,1.08));rows.append({'airport_code':code,'month':date,'domestic_passengers':total-intl,'international_passengers':intl,'total_passengers':total})
df=pd.DataFrame(rows);df.to_csv(RAW/'monthly_traffic.csv',index=False);df=pd.read_csv(RAW/'monthly_traffic.csv',parse_dates=['month']).drop_duplicates(['airport_code','month']);df['total_passengers']=df.domestic_passengers+df.international_passengers;df['year']=df.month.dt.year;df['month_num']=df.month.dt.month;df=df.sort_values(['airport_code','month']);assert df.total_passengers.gt(0).all() and not df.duplicated(['airport_code','month']).any();df.to_csv(OUT/'traffic_clean.csv',index=False);df.to_excel(OUT/'traffic_clean.xlsx',index=False)
with sqlite3.connect(OUT/'passenger_forecasting.sqlite') as con:
 df.to_sql('fact_monthly_traffic',con,if_exists='replace',index=False);pd.read_sql_query('SELECT airport_code,year,SUM(total_passengers) AS passengers FROM fact_monthly_traffic GROUP BY airport_code,year',con).to_csv(REP/'sql_annual_traffic.csv',index=False)
results=[];future=[]
for code,g in df.groupby('airport_code'):
 g=g.sort_values('month').reset_index(drop=True);train=g.iloc[:-12].copy();test=g.iloc[-12:].copy();train['t']=np.arange(len(train));test['t']=np.arange(len(train),len(g));
 # Seasonal naive baseline: last year's corresponding month
 baseline=g.total_passengers.shift(12).iloc[-12:].to_numpy();
 def features(x):return np.column_stack([x.t.to_numpy(),pd.get_dummies(pd.Categorical(x.month_num,categories=range(1,13))).to_numpy()])
 model=LinearRegression().fit(features(train),train.total_passengers); alternative=np.maximum(0,model.predict(features(test)));truth=test.total_passengers.to_numpy();
 for name,pred in [('seasonal_naive',baseline),('linear_trend_seasonality',alternative)]:
  for date,actual,p in zip(test.month,truth,pred):results.append({'airport_code':code,'month':date,'model':name,'actual':actual,'predicted':round(float(p)),'absolute_error':round(abs(actual-p))})
 # Future forecast uses winning model on held-out test; fit on full history
 baseline_mae=mean_absolute_error(truth,baseline);alternative_mae=mean_absolute_error(truth,alternative);winner='seasonal_naive' if baseline_mae<=alternative_mae else 'linear_trend_seasonality';g['t']=np.arange(len(g));full=LinearRegression().fit(features(g),g.total_passengers)
 for j,date in enumerate(pd.date_range(g.month.max()+pd.offsets.MonthBegin(1),periods=12,freq='MS')):
  if winner=='seasonal_naive':pred=g.total_passengers.iloc[-12+j]
  else:
   x=pd.DataFrame({'t':[len(g)+j],'month_num':[date.month]});pred=full.predict(features(x))[0]
  future.append({'airport_code':code,'month':date,'selected_model':winner,'forecast_passengers':round(max(0,pred))})
res=pd.DataFrame(results); fut=pd.DataFrame(future);res.to_csv(OUT/'test_predictions.csv',index=False);fut.to_csv(OUT/'future_forecasts.csv',index=False);fut.to_excel(OUT/'future_forecasts.xlsx',index=False)
metrics=res.groupby(['airport_code','model']).apply(lambda x:pd.Series({'MAE':mean_absolute_error(x.actual,x.predicted),'RMSE':np.sqrt(mean_squared_error(x.actual,x.predicted)),'MAPE_pct':np.mean(abs((x.actual-x.predicted)/x.actual))*100}),include_groups=False).reset_index();metrics.to_csv(REP/'forecast_metrics.csv',index=False);metrics.to_excel(REP/'forecast_metrics.xlsx',index=False)
kpis={'airports':len(codes),'monthly_records':len(df),'test_months_per_airport':12,'forecast_months_per_airport':12};(REP/'kpis.json').write_text(json.dumps(kpis,indent=2));sns.set_theme(style='whitegrid')
def save(name):plt.tight_layout();plt.savefig(CH/name,dpi=120,bbox_inches='tight');plt.close()
plt.figure(figsize=(10,4));sns.lineplot(data=df,x='month',y='total_passengers',hue='airport_code');plt.title('Synthetic monthly passenger traffic');save('01_traffic_trends.png')
plt.figure(figsize=(8,4));df.groupby('airport_code').total_passengers.sum().sort_values().plot.barh();plt.title('Synthetic passenger totals 2019-2025');save('02_airport_totals.png')
plt.figure(figsize=(9,4));df.groupby('year').total_passengers.sum().plot.bar();plt.title('Annual synthetic passenger totals');save('03_yearly_totals.png')
plt.figure(figsize=(8,4));df.groupby('month_num').total_passengers.mean().plot.bar();plt.title('Average monthly seasonality');save('04_seasonality.png')
plt.figure(figsize=(8,4));df[['domestic_passengers','international_passengers']].sum().plot.pie(autopct='%1.1f%%');plt.ylabel('');plt.title('Synthetic domestic vs international');save('05_domestic_international.png')
plt.figure(figsize=(10,4));g=df[df.airport_code=='BLR'];plt.plot(g.month,g.total_passengers,label='Historical');q=fut[fut.airport_code=='BLR'];plt.plot(q.month,q.forecast_passengers,label='Forecast');plt.legend();plt.title('BLR synthetic traffic and forecast');save('06_blr_forecast.png')
plt.figure(figsize=(8,4));sns.barplot(data=metrics,x='airport_code',y='MAE',hue='model');plt.title('Holdout forecast MAE comparison');save('07_model_mae.png')
plt.figure(figsize=(9,4));q=res[(res.airport_code=='BLR')&(res.model=='seasonal_naive')];plt.bar(q.month.dt.strftime('%Y-%m'),q.predicted-q.actual);plt.xticks(rotation=60);plt.title('BLR seasonal-naive holdout errors');save('08_forecast_errors.png')
print('FORECAST PASS',kpis,metrics.to_string(index=False))
