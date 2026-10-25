# Airport Passenger Traffic and Demand Forecasting

**Portfolio project — reproducible synthetic demonstration, not official aviation statistics.** Airport identifiers correspond to real Indian airports. All shipment/booking/traffic observations and financial figures are generated.

## Business problem
Understand simulated passenger trends and benchmark 12-month demand forecasts.

## Stack
Python, Pandas, NumPy, SQLite, SQL, Excel, CSV, Jupyter, Matplotlib, Seaborn, scikit-learn.

## Windows setup (Python 3.11 or 3.12 recommended)
```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python src/run_analysis.py
python -m jupyter lab
```
Open `analysis.ipynb` and select **Run All**. If `py -3.12` is unavailable, install Python 3.12 or use `py -3.11`. Execute commands from the project folder.

## Project files
`src/run_analysis.py` creates raw and cleaned datasets, a SQLite database, SQL query reports, eight charts, and KPI summaries. `data/raw` and `data/processed` contain generated CSV and XLSX files. `docs` contains business and interview notes. Regenerate all files by rerunning the script.

## Data quality and methodology
Fixed NumPy random seed; injected duplicate removed; cargo and ticket data include injected missing fare/weight imputed with median; primary keys and positive quantities validated. SQLite aggregation independently produces reports. Forecasting uses chronological final-12-month holdout per airport; MAE, RMSE and MAPE are evaluated; the selected model is fitted on all data for the next 12 months.

## Limitations
Synthetic distributions and relationships are assumptions, not measured Indian airline performance. Ticket route contribution uses invented estimated costs, **not audited profitability**. Cargo on-time percentage excludes cancellations; average delay floors early deliveries at zero. Forecast accuracy reflects only synthetic patterns, not real-world demand.

## GitHub upload
```powershell
git init
git add .
git commit -m "Add reproducible synthetic dataset and analysis"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git push -u origin main
```
Create the empty repository first. Suggested commits: scaffold, data generation, ETL and SQL, visualizations, findings, docs. Do not commit secrets or `.venv`.

## Resume-ready description
Built a reproducible Python/SQL aviation analytics pipeline using synthetic Indian aviation datasets, data validation, eight visualizations, SQLite reporting, and Excel exports.

## Suggested GitHub topics
`data-analytics`, `python`, `pandas`, `sqlite`, `jupyter-notebook`, `aviation`, `portfolio-project`, `synthetic-data`.
