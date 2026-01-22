import pandas as pd

df = pd.read_csv("data/raw_data.csv")
report = []

# Missing values
report.append("MISSING VALUES:\n" + str(df.isnull().sum()) + "\n")

# Duplicates
duplicates = df.duplicated().sum()
report.append(f"DUPLICATE ROWS: {duplicates}\n")
df = df.drop_duplicates()

# Schema validation
expected_schema = {
    "id": "int64",
    "name": "object",
    "age": "int64",
    "department": "object",
    "salary": "int64"
}

schema_issues = []
for col, dtype in expected_schema.items():
    if col not in df.columns:
        schema_issues.append(f"Missing column: {col}")
    else:
        try:
            df[col] = df[col].astype(dtype)
        except:
            schema_issues.append(f"Invalid datatype in column: {col}")

report.append("SCHEMA ISSUES:\n" + "\n".join(schema_issues) + "\n")

# Cleaning
df['age'] = pd.to_numeric(df['age'], errors='coerce')
df['age'] = df['age'].fillna(df['age'].median())
df['department'] = df['department'].fillna("Unknown")

# Save outputs
df.to_csv("output/cleaned_data.csv", index=False)

with open("output/quality_report.txt", "w") as f:
    for line in report:
        f.write(line + "\n")

print("✅ Data Quality Check Completed")
