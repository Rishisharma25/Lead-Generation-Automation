import pandas as pd
from datetime import datetime


def generate_leads(file_path):
    # Load dataset
    df = pd.read_csv(file_path, dtype=str)

    # Ensure required columns exist
    required_cols = ["name", "domain", "linkedin url", "locality", "country", "industry", "size range"]
    for col in required_cols:
        if col not in df.columns:
            df[col] = "N/A"

    # Select and rename columns
    df = df[required_cols].rename(columns={
        "name": "Name",
        "domain": "Domain",
        "linkedin url": "LinkedIn",
        "locality": "City",
        "country": "Country",
        "industry": "Industry",
        "size range": "Company Size",
    })

    # Data cleaning
    df["Name"] = df["Name"].str.strip().str.title()
    df["Country"] = df["Country"].str.strip().str.title()
    df["City"] = df["City"].str.strip()

    df.replace("", pd.NA, inplace=True)
    df.dropna(subset=["Name"], inplace=True)
    df.drop_duplicates(subset=["Name"], inplace=True)
    df.fillna("N/A", inplace=True)

    # Limit entries (as per assignment requirement)
    df = df.iloc[:30]

    # Generate fields
    df["Generated Email"] = df["Domain"].apply(
        lambda d: f"contact@{d}" if d != "N/A" else "N/A"
    )

    df["Website"] = df["Domain"].apply(
        lambda d: f"https://{d}" if d != "N/A" else "N/A"
    )

    # Final structure
    df = df[[
        "Name", "Generated Email", "Website", "LinkedIn",
        "City", "Country", "Industry", "Company Size"
    ]]

    # Export to Excel
    output_file = f"leads_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
    df.to_excel(output_file, index=False)

    print(f"Leads file created: {output_file}")


if __name__ == "__main__":
    generate_leads("companies_sample.csv")
