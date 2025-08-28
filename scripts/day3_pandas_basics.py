# scripts/day3_pandas_basics.py
from pathlib import Path
import sys
import pandas as pd

def load_register():
    excel_path = Path("data/vendor_register_template.xlsx")
    csv_path = Path("data/vendor_register_template.csv")

    if excel_path.exists():
        df = pd.read_excel(excel_path)
        source = excel_path
    elif csv_path.exists():
        df = pd.read_csv(csv_path)
        source = csv_path
    else:
        print("❌ No data file found in data/. Expected vendor_register_template.xlsx or .csv")
        sys.exit(1)
    return df, source

def main():
    df, source = load_register()
    print(f"✅ Loaded {len(df)} rows from: {source}")

    # 1) Inspect columns & dtypes
    print("\n▶ Columns:", list(df.columns))
    print("\n▶ Data types BEFORE:")
    print(df.dtypes)

    # 2) Clean column names (strip spaces)
    df.columns = [c.strip() for c in df.columns]

    # 3) Parse 'Assessment Date' to datetime
    if "Assessment Date" in df.columns:
        df["Assessment Date"] = pd.to_datetime(df["Assessment Date"], errors="coerce")

    print("\n▶ Data types AFTER:")
    print(df.dtypes)

    # 4) Peek at data
    print("\n▶ First 5 rows:")
    print(df.head().to_string(index=False))

    # 5) Basic filters
    high_risk = df[df["Risk Score"] >= 80]
    missing_assessment = df[df["Assessment Date"].isna()]

    print(f"\n▶ High-risk vendors (Risk Score >= 80): {len(high_risk)}")
    if not high_risk.empty:
        print(high_risk[["Vendor Name", "Service", "Risk Score"]].to_string(index=False))

    print(f"\n▶ Vendors with missing Assessment Date: {len(missing_assessment)}")
    if not missing_assessment.empty:
        print(missing_assessment[["Vendor Name", "Service"]].to_string(index=False))

    # 6) Save filtered views to outputs/
    out_dir = Path("outputs")
    out_dir.mkdir(exist_ok=True)
    high_risk.to_csv(out_dir / "day3_high_risk.csv", index=False)
    missing_assessment.to_csv(out_dir / "day3_missing_assessment.csv", index=False)

    print(f"\n💾 Saved: {out_dir / 'day3_high_risk.csv'}")
    print(f"💾 Saved: {out_dir / 'day3_missing_assessment.csv'}")

if __name__ == "__main__":
    main()
