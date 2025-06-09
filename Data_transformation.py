import pandas as pd
from datetime import datetime, timedelta

# Load cleaned CSV (from original test outputs)
df = pd.read_csv("cleaned_defensive_data.csv")

# -------------------------------
# Add Region Based on Location
# -------------------------------
region_map = {
    'US': 'North America', 'CA': 'North America',
    'BR': 'South America', 'GB': 'Europe', 'FR': 'Europe', 'DE': 'Europe',
    'NG': 'Africa', 'KE': 'Africa', 'ZA': 'Africa', 'AO': 'Africa',
    'CN': 'Asia', 'JP': 'Asia', 'IN': 'Asia', 'SG': 'Asia',
    'AE': 'Middle East', 'SA': 'Middle East',
    'AU': 'Oceania', 'NZ': 'Oceania',
}

def extract_region(loc):
    try:
        country_code = loc.strip()[-2:]
        return region_map.get(country_code, "Other")
    except:
        return "Other"

df["Region"] = df["LOCATION"].apply(extract_region)

# -------------------------------
# Add Test Category
# -------------------------------
def test_category(test):
    test = test.upper()
    if test in ['PING', 'TRACEROUTE']:
        return "Latency"
    elif "HTTPS" in test or "SSL" in test:
        return "Security"
    elif "DOWNLOAD" in test or "UPLOAD" in test:
        return "Throughput"
    else:
        return "Other"

df["Test Category"] = df["TEST"].apply(test_category)

# -------------------------------
# Add Performance Grade
# -------------------------------
def grade(val):
    if pd.isna(val):
        return "Unknown"
    elif val < 100:
        return "Good"
    elif val < 300:
        return "Average"
    else:
        return "Poor"

df["Performance Grade"] = df["metric_mean"].apply(grade)

# -------------------------------
# Add Synthetic Timestamp
# -------------------------------
start_time = datetime(2025, 5, 30, 8, 0, 0)
df["Log Timestamp"] = [
    (start_time + timedelta(minutes=15 * i)).strftime("%Y-%m-%d %H:%M:%S")
    for i in range(len(df))
]

# -------------------------------
# Save Enhanced CSV
# -------------------------------
df.to_csv("mock_dashboard_enhanced.csv", index=False)
print("✅ mock_dashboard_enhanced.csv exported.")
