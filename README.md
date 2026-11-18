# AQI Data Analysis System

**Beginner-level B.Tech Mini Project**  
**Submitted by:** Muthunarayan

## Overview
This project demonstrates basic air-quality data analysis using Python, Pandas, NumPy and Matplotlib. It displays a sample dataset, checks missing values, cleans records, calculates AQI statistics, compares average AQI by city, assigns simple AQI categories, and creates charts.

> **Data notice:** The values included in the code are illustrative sample values for learning. They are not live or official measurements and should not be used to describe actual city air quality. For a research or final hackathon submission, replace them with verified data and document the source, monitoring station, date range and download date.

## Technologies
- Python
- Pandas
- NumPy
- Matplotlib

## Project files
- `aqi_analysis.py` — main Python program
- `README.md` — project description and run instructions

## How to run
1. Install Python 3.
2. Install the required libraries:
   ```bash
   pip install pandas numpy matplotlib
   ```
3. Run the program:
   ```bash
   python aqi_analysis.py
   ```

The program creates:
- `average_aqi_by_city.png`
- `aqi_readings.png`
- `aqi_analysis_result.csv`

## Use your own dataset
Replace the sample dictionary in `aqi_analysis.py` with a CSV import such as:

```python
df = pd.read_csv("your_aqi_data.csv")
df["Date"] = pd.to_datetime(df["Date"])
```

The CSV should contain these columns: `City`, `Date`, `AQI`, `PM2.5`, and `PM10`.

## AQI category bands used
The example uses these simplified Indian AQI bands: Good (0–50), Satisfactory (51–100), Moderate (101–200), Poor (201–300), Very Poor (301–400), Severe (401–500). Confirm the applicable official standard and category calculation when working with real measurements.

## Possible future improvements
- Import verified live or historical data from an official source.
- Compare more cities and monitoring stations.
- Add pollutant-wise analysis and time-based trends.
- Build an interactive dashboard.

## References
- [Python documentation](https://docs.python.org/3/)
- [Pandas documentation](https://pandas.pydata.org/docs/)
- [NumPy documentation](https://numpy.org/doc/)
- [Matplotlib documentation](https://matplotlib.org/stable/)
- [Central Pollution Control Board (CPCB), India](https://cpcb.nic.in/)
