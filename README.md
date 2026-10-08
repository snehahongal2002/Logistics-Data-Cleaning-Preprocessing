# Week 2 – Data Collection, Cleaning and Preprocessing for Logistics Analysis

## Project Overview

This project demonstrates a Python-based data preprocessing pipeline for logistics analysis. It follows the methodology documented in the Week 2 internship report and simulates realistic shipment data containing common quality issues.

The workflow covers:

1. Data collection simulation
2. Dataset profiling
3. Missing-value detection and treatment
4. Duplicate detection and removal
5. Outlier detection using the Interquartile Range (IQR)
6. Min-Max normalization
7. Final validation
8. Export of an analysis-ready dataset

## Dataset

The project uses a simulated educational logistics dataset rather than confidential company data.

The dataset contains:

- Shipment ID
- Transport mode
- Destination region
- Quantity
- Shipping cost
- Delivery time
- Shipment status

The raw data intentionally contains missing values, one duplicate, and extreme observations so the preprocessing process can be demonstrated reproducibly.

## Repository Structure

```text
week2-logistics-data-preprocessing/
├── data/
│   ├── raw/
│   │   └── logistics_data.csv
│   ├── processed/
│   │   └── cleaned_logistics_data.csv
│   └── README.md
├── docs/
├── notebooks/
│   └── Week_2_Logistics_Preprocessing.ipynb
├── reports/
│   └── preprocessing_summary.txt
├── src/
│   └── preprocess_logistics.py
├── .gitignore
├── requirements.txt
└── README.md
```

## Technologies

- Python
- Pandas
- NumPy
- Scikit-learn
- Jupyter Notebook

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/week2-logistics-data-preprocessing.git
cd week2-logistics-data-preprocessing
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the preprocessing script

```bash
python src/preprocess_logistics.py
```

The script creates:

`data/processed/cleaned_logistics_data.csv`

and:

`reports/preprocessing_summary.txt`

### 4. Run the notebook

```bash
jupyter notebook notebooks/Week_2_Logistics_Preprocessing.ipynb
```

## Methodology

### Missing values
- Numerical fields: median imputation
- Categorical fields: mode imputation

Median was selected because logistics quantities, costs, and delivery times can be skewed by unusually large shipments or delays.

### Duplicate records
Exact duplicate rows are removed to prevent double counting.

### Outliers
The IQR method is used:

`Lower bound = Q1 - 1.5 × IQR`

`Upper bound = Q3 + 1.5 × IQR`

Potential outliers are flagged for business investigation. They are not automatically deleted because genuine exceptional logistics events can be analytically valuable.

### Normalization
Min-Max scaling transforms selected numerical variables to a 0–1 range. This is useful for distance-based methods and many machine-learning workflows.

## Key Learning Outcome

The project demonstrates that reliable logistics analytics depends on systematic data quality management. Proper preprocessing supports accurate shipment metrics, transportation-cost analysis, delivery-performance measurement, capacity planning, and future predictive analytics.

## Disclaimer

This is an educational simulation created for an internship task. It does not contain confidential company information or personally identifiable customer data.
