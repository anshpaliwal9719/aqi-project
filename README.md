# AQI Data Analysis System

**Beginner-Level B.Tech Mini Project**  
**Submitted by: Ansh Paliwal**

## Project overview
This project demonstrates basic Air Quality Index (AQI) data analysis using only Python, Pandas and NumPy. It creates a small dataset, inspects and cleans records, calculates AQI statistics, compares average AQI by city, classifies readings and exports processed data to CSV.

## Technologies
- Python
- Pandas
- NumPy
- Google Colab (to run the notebook)

## Files
- `AQI_Data_Analysis_System_Ansh_Paliwal.ipynb` — Google Colab-compatible notebook.
- `README.md` — project description and instructions.

## How to run
1. Open [Google Colab](https://colab.research.google.com/).
2. Select **File → Upload notebook**.
3. Upload `AQI_Data_Analysis_System_Ansh_Paliwal.ipynb`.
4. Run each cell from top to bottom.
5. The final code cell creates `aqi_analysis_result.csv`. Download it from the Colab Files panel.

## Data notice
The dataset contains illustrative sample values for learning. It is not live or official AQI data. Do not present the values as actual measurements. For real-world analysis, replace the sample values with verified readings and document the data source, monitoring station and date range.

## Analysis performed
1. Dataset creation and display.
2. Dataset inspection (head, shape and data types).
3. Missing-value and duplicate checks.
4. Basic cleaning.
5. Mean, maximum, minimum and standard deviation using NumPy.
6. City-wise average AQI using Pandas.
7. AQI category classification.
8. Highest AQI record and category counts.
9. CSV export.

## References
- [Python documentation](https://docs.python.org/3/)
- [Pandas documentation](https://pandas.pydata.org/docs/)
- [NumPy documentation](https://numpy.org/doc/)
- [Central Pollution Control Board (CPCB), India](https://cpcb.nic.in/)
