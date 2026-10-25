# Ten interview questions and answers

**1. What business problem does this project solve?**

It demonstrates monitoring aviation operational or commercial KPIs.

**2. Why use synthetic data?**

It allows safe, reproducible learning without claiming access to proprietary records.

**3. How do you ensure reproducibility?**

A fixed NumPy random seed and versioned generator code.

**4. What is a primary key?**

A unique row identifier, such as shipment_id or booking_id; for traffic, airport and month.

**5. How did you handle duplicates?**

Drop duplicate identifiers before aggregating to avoid double counting.

**6. How did you handle missing values?**

Check missing observations and chronological coverage; never interpolate across test boundaries.

**7. Why use SQLite alongside Pandas?**

SQL models the relational reporting workflow while Pandas handles flexible transformations.

**8. How do you avoid misleading charts?**

Use time-based train/test split and show MAE/RMSE for both forecasting methods.

**9. What is a limitation of your analysis?**

Generated distributions are assumptions and do not establish real-world causality.

**10. How would you improve this with real data?**

Replace generated input with documented authorized datasets and rerun validation.

## LinkedIn description
Built a complete synthetic aviation analytics case study with Python, SQLite, Jupyter, visual reporting, reproducible data and business recommendations.
