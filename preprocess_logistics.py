"""
Week 2 - Logistics Data Collection, Cleaning and Preprocessing

Run from the project root:
    python src/preprocess_logistics.py
"""

from pathlib import Path
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

ROOT = Path(__file__).resolve().parents[1]
RAW_FILE = ROOT / "data" / "raw" / "logistics_data.csv"
OUTPUT_FILE = ROOT / "data" / "processed" / "cleaned_logistics_data.csv"
REPORT_FILE = ROOT / "reports" / "preprocessing_summary.txt"

NUMERIC_COLS = ["Quantity", "Shipping_Cost", "Delivery_Time"]
CATEGORICAL_COLS = ["Transport_Mode", "Destination_Region", "Status"]


def iqr_bounds(data: pd.DataFrame, column: str):
    q1 = data[column].quantile(0.25)
    q3 = data[column].quantile(0.75)
    iqr = q3 - q1
    return q1 - 1.5 * iqr, q3 + 1.5 * iqr


def main():
    df = pd.read_csv(RAW_FILE)

    before_rows = len(df)
    missing_before = int(df.isnull().sum().sum())
    duplicates_before = int(df.duplicated().sum())

    # Remove exact duplicate records.
    df = df.drop_duplicates().copy()

    # Fill numerical missing values with median.
    for col in NUMERIC_COLS:
        df[col] = df[col].fillna(df[col].median())

    # Fill categorical missing values with mode.
    for col in CATEGORICAL_COLS:
        df[col] = df[col].fillna(df[col].mode()[0])

    # Detect outliers for review. They are NOT automatically deleted.
    outlier_report = {}
    for col in NUMERIC_COLS:
        lower, upper = iqr_bounds(df, col)
        mask = (df[col] < lower) | (df[col] > upper)
        outlier_report[col] = {
            "lower_bound": float(lower),
            "upper_bound": float(upper),
            "count": int(mask.sum()),
        }

    # Normalize selected numerical features to 0-1.
    scaler = MinMaxScaler()
    df[NUMERIC_COLS] = scaler.fit_transform(df[NUMERIC_COLS])

    # Validation.
    missing_after = int(df.isnull().sum().sum())
    duplicates_after = int(df.duplicated().sum())

    assert missing_after == 0, "Missing values remain after preprocessing."
    assert duplicates_after == 0, "Duplicate rows remain after preprocessing."

    df.to_csv(OUTPUT_FILE, index=False)

    lines = [
        "WEEK 2 LOGISTICS PREPROCESSING SUMMARY",
        "=" * 45,
        f"Raw records: {before_rows}",
        f"Duplicates detected: {duplicates_before}",
        f"Missing cells before cleaning: {missing_before}",
        f"Records after duplicate removal: {len(df)}",
        f"Missing cells after cleaning: {missing_after}",
        f"Duplicate rows after cleaning: {duplicates_after}",
        "",
        "Potential outliers (review, not automatic deletion):",
    ]

    for col, info in outlier_report.items():
        lines.append(
            f"- {col}: {info['count']} | "
            f"bounds=({info['lower_bound']:.2f}, {info['upper_bound']:.2f})"
        )

    REPORT_FILE.write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))
    print(f"\nSaved: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
