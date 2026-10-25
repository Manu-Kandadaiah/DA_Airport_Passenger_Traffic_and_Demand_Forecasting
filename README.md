# Airport Passenger Traffic and Demand Forecasting

A reproducible data analytics project that explores monthly passenger
traffic across six Indian airports and compares forecasting approaches
to estimate the next 12 months of demand.

> **Data note:** This project uses generated synthetic data,
> not official airport or airline statistics. Airport codes identify
> real airports, but the observations and results are simulated.

## Business Problem

Airport and aviation teams need to understand passenger-demand patterns,
compare forecast methods, and prepare reliable summaries for planning.
Raw monthly records can contain duplicate rows, inconsistent fields, and
data spread across multiple formats.

## Solution

This project builds a repeatable Python analytics pipeline that cleans
and validates monthly traffic data, stores reporting data in SQLite,
exports analysis-ready CSV and Excel files, visualizes trends, and
benchmarks two forecasting methods using a chronological holdout.

## Key Features

-   Generates and processes synthetic monthly traffic records for six
    airports.
-   Cleans data, removes duplicate airport-month records, and derives
    total passengers, year, and month features.
-   Validates positive passenger counts and uniqueness of airport-month
    records.
-   Exports clean datasets to CSV and Excel.
-   Uses SQLite and SQL for structured storage and reporting.
-   Creates charts and KPI summaries for exploratory analysis.
-   Compares `linear_trend_seasonality` and `seasonal_naive` forecasting
    baselines.
-   Evaluates forecasts with MAE, RMSE, and MAPE.
-   Produces a 12-month forecast for each airport.
-   Supports rerunning the pipeline to regenerate outputs as the project
    evolves.

## Forecast Evaluation Snapshot

The current run processed **504 monthly records across 6 airports**,
using the final **12 months per airport** as the test period. In this
run, the seasonal-naive baseline achieved a lower MAPE than the linear
trend-and-seasonality model at all six airports.

  Airport code     Seasonal-naive MAPE
  -------------- ---------------------
  BLR                            4.26%
  BOM                            6.22%
  DEL                            4.73%
  HYD                            5.19%
  IXE                            3.62%
  MAA                            4.13%

These scores describe only the current synthetic dataset and test
window. They should not be interpreted as real-world aviation forecast
accuracy.

## Tech Stack and Skills

**Tools:** Python, Pandas, NumPy, SQLite, SQL, CSV, Excel, JupyterLab,
Matplotlib, Seaborn, scikit-learn, Git, GitHub.

**Skills demonstrated:** - Data cleaning and preprocessing - Exploratory
data analysis (EDA) - Data validation and quality checks - Feature
engineering for time series - SQL querying and aggregation - Data
visualization and KPI reporting - Time-series train/test design -
Forecast benchmarking and error metrics - Excel/CSV reporting and
workflow automation - Reproducible project organization and
documentation

## Project Structure

``` text
03-airport-passenger-forecasting/
├── src/
│   └── run_analysis.py       # Main data and forecasting pipeline
├── data/
│   ├── raw/                  # Generated source data
│   └── processed/            # Cleaned datasets and exports
├── charts/                   # Generated visualizations
├── reports/                  # KPI and model evaluation reports
├── sql/                      # SQL queries and reporting logic
├── docs/                     # Project notes and documentation
├── analysis.ipynb             # Interactive analysis notebook
├── requirements.txt           # Python dependencies
└── README.md
```

Generated files may vary according to the implementation and
configuration in the repository. The pipeline can regenerate supported
outputs.

## How to Run on Windows

### 1. Install Python

Python **3.12** is recommended. Confirm that Python and pip are
available:

``` powershell
py -3.12 --version
```

### 2. Open the project folder

Run all commands from the root directory of this repository.

### 3. Create and activate a virtual environment

``` powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, you can invoke the environment's Python
directly with `.\.venv\Scripts\python.exe`.

### 4. Install dependencies

``` powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

If an Excel export fails with
`ModuleNotFoundError: No module named 'openpyxl'`, install it using:

``` powershell
python -m pip install openpyxl
```

### 5. Run the analysis pipeline

``` powershell
python src/run_analysis.py
```

The script generates or refreshes the project's data outputs, reports,
charts, and forecast evaluation according to the current code.

### 6. Open the notebook (optional)

``` powershell
python -m jupyter lab
```

Open `analysis.ipynb` in JupyterLab and select **Run All** to review the
interactive analysis. If Windows Application Control blocks Jupyter or a
compiled Python package, consult the relevant Windows security logs or
your system administrator; reinstalling packages may not bypass an
application-control policy.

## Methodology

1.  Generate reproducible synthetic data using a fixed random seed.
2.  Load and clean monthly airport traffic records.
3.  Remove duplicate airport-month rows and derive passenger and
    calendar features.
4.  Validate record uniqueness and positive total passenger counts.
5.  Export clean data and create structured SQLite/SQL reports.
6.  Explore traffic patterns using charts and summary KPIs.
7.  Hold out the final 12 months for each airport for chronological
    evaluation.
8.  Compare the linear trend-and-seasonality model with a seasonal-naive
    baseline using MAE, RMSE, and MAPE.
9.  Fit the selected approach on the available data and produce a
    12-month forecast per airport.

## Limitations

-   All passenger observations are synthetic; they are not official
    airport statistics.
-   Forecast scores reflect the assumptions and patterns built into the
    generated data.
-   Synthetic-data performance does not establish performance on real
    passenger demand.
-   Use verified official datasets and additional backtesting before
    making operational or investment decisions.

## Future Improvements

-   Replace generated data with verified public airport traffic data.
-   Add a configurable date range and airport selection.
-   Include prediction intervals and compare additional forecasting
    models.
-   Add rolling-origin cross-validation and seasonal error analysis.
-   Build a dashboard using Streamlit, Power BI, or Tableau.
-   Add automated tests, data-quality checks, and a CI workflow.
-   Document data sources, assumptions, and model versions.

## GitHub Topics

`data-analytics` `python` `pandas` `sqlite` `sql` `jupyter-notebook`
`time-series-forecasting` `synthetic-data`

for six airports, generate KPI reports and visualizations, and benchmark
12-month forecasts using MAE, RMSE, and MAPE.
