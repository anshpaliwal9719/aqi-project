"""
AQI DATA ANALYSIS SYSTEM
Beginner-level B.Tech Mini Project
Submitted by: Muthunarayan

Libraries: Python, Pandas, NumPy, Matplotlib

IMPORTANT:
The built-in dataset below is illustrative sample data for demonstrating
data analysis. It is NOT live or officially measured AQI data.
Replace it with verified readings before using the results in a formal study.

To run:
1. Install libraries: pip install pandas numpy matplotlib
2. Run: python aqi_analysis.py
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# STEP 1: Create a sample AQI dataset
data = {
    "City": [
        "Delhi", "Delhi", "Mumbai", "Mumbai",
        "Lucknow", "Lucknow", "Chennai", "Chennai",
        "Kolkata", "Kolkata"
    ],
    "Date": [
        "2026-01-01", "2026-01-02", "2026-01-01", "2026-01-02",
        "2026-01-01", "2026-01-02", "2026-01-01", "2026-01-02",
        "2026-01-01", "2026-01-02"
    ],
    "AQI": [280, 310, 125, 140, 190, 175, 75, 82, 160, 170],
    "PM2.5": [150, 170, 65, 72, 95, 88, 35, 40, 80, 85],
    "PM10": [220, 240, 110, 120, 160, 150, 70, 75, 135, 145]
}

df = pd.DataFrame(data)
df["Date"] = pd.to_datetime(df["Date"])


# STEP 2: Display and inspect the dataset
print("\n========== AQI DATASET ==========")
print(df)

print("\nDataset shape (rows, columns):", df.shape)
print("\nMissing values:")
print(df.isnull().sum())


# STEP 3: Clean the data
df["AQI"] = pd.to_numeric(df["AQI"], errors="coerce")
df["PM2.5"] = pd.to_numeric(df["PM2.5"], errors="coerce")
df["PM10"] = pd.to_numeric(df["PM10"], errors="coerce")

df = df.dropna(subset=["City", "Date", "AQI"])
df = df.drop_duplicates()


# STEP 4: Calculate AQI statistics using NumPy
aqi_values = df["AQI"].to_numpy()

print("\n========== AQI STATISTICS ==========")
print("Average AQI:", round(np.mean(aqi_values), 2))
print("Maximum AQI:", np.max(aqi_values))
print("Minimum AQI:", np.min(aqi_values))
print("Standard deviation:", round(np.std(aqi_values), 2))


# STEP 5: Calculate average AQI city-wise using Pandas
city_aqi = df.groupby("City")["AQI"].mean().sort_values(ascending=False)

print("\n========== CITY-WISE AVERAGE AQI ==========")
print(city_aqi)
print("\nHighest average AQI city:", city_aqi.idxmax())
print("Lowest average AQI city:", city_aqi.idxmin())


# STEP 6: Classify AQI readings using simple category bands
def get_aqi_category(value):
    if value <= 50:
        return "Good"
    elif value <= 100:
        return "Satisfactory"
    elif value <= 200:
        return "Moderate"
    elif value <= 300:
        return "Poor"
    elif value <= 400:
        return "Very Poor"
    else:
        return "Severe"


df["AQI_Category"] = df["AQI"].apply(get_aqi_category)

print("\n========== AQI CATEGORIES ==========")
print(df[["City", "Date", "AQI", "AQI_Category"]])


# STEP 7: Find the record with the highest AQI
highest_record = df.loc[df["AQI"].idxmax()]

print("\n========== HIGHEST AQI RECORD ==========")
print(highest_record)


# STEP 8: Draw a bar chart of average AQI by city
plt.figure(figsize=(9, 5))
city_aqi.sort_values().plot(kind="bar", color="skyblue")
plt.title("Average AQI by City")
plt.xlabel("City")
plt.ylabel("Average AQI")
plt.tight_layout()
plt.savefig("average_aqi_by_city.png")
plt.show()


# STEP 9: Draw a chart of AQI readings
plt.figure(figsize=(9, 5))
plt.plot(df["Date"], df["AQI"], marker="o")
plt.title("AQI Readings in the Sample Dataset")
plt.xlabel("Date")
plt.ylabel("AQI")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig("aqi_readings.png")
plt.show()


# STEP 10: Save analysed data to a CSV file
df.to_csv("aqi_analysis_result.csv", index=False)

print("\nAnalysis completed successfully!")
print("Files created:")
print("- average_aqi_by_city.png")
print("- aqi_readings.png")
print("- aqi_analysis_result.csv")
