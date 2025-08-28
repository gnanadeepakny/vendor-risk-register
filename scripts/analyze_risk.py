import pandas as pd
import matplotlib.pyplot as plt
import os

# File path
file_path = os.path.join("data", "vendor_register_template.csv")

try:
    # Load the CSV
    df = pd.read_csv(file_path)

    # Basic dataset overview
    print("✅ Data Loaded Successfully\n")
    print("📊 Dataset Preview:")
    print(df.head(), "\n")

    print("🔎 Summary Statistics:")
    print(df.describe(include="all"), "\n")

    # Risk distribution plot
    plt.figure(figsize=(8, 5))
    df['Risk Score'].hist(bins=10, edgecolor='black')
    plt.title("Distribution of Vendor Risk Scores")
    plt.xlabel("Risk Score")
    plt.ylabel("Number of Vendors")

    # Save chart into outputs/
    output_path = os.path.join("outputs", "risk_distribution.png")
    plt.savefig(output_path)
    plt.close()

    print(f"📈 Risk distribution chart saved at: {output_path}")

except FileNotFoundError:
    print(f"❌ File not found: {file_path}. Make sure the CSV exists.")
except Exception as e:
    print(f"⚠️ An error occurred: {e}")
