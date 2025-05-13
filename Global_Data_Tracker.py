# --- Import necessary libraries ---
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import requests
from datetime import datetime

# Set seaborn style for visualization
sns.set(style="whitegrid")

# --- Task 1: Data Loading ---
print("Loading data...")

# Attempt to fetch real-time data
try:
    url = "https://covid19.who.int/WHO-COVID-19-global-data.csv"
    data = pd.read_csv(url)
    data.to_csv("datasets/covid_data.csv", index=False)  # Save a local copy
    print("Data successfully fetched and saved.")
except Exception as e:
    print(f"Failed to fetch real-time data. Error: {e}")
    # Attempt to load from local file
    data = pd.read_csv("datasets/covid_data.csv")
    print("Loaded data from local CSV.")

# Display the first 5 rows
display(data.head())

# --- Task 2: Data Exploration ---
print("\nDataset Info:")
data.info()

print("\nMissing Values Check:")
print(data.isnull().sum())

# Data Cleaning (if necessary)
data.fillna(0, inplace=True)

# --- Task 3: Data Analysis ---
print("\nBasic Statistics:")
display(data.describe())

# Group by Country and compute total cases and deaths
global_summary = data.groupby('Country').sum()[['Cumulative_cases', 'Cumulative_deaths']]
global_summary = global_summary.sort_values(by='Cumulative_cases', ascending=False)

# Display the top 10 most affected countries
print("\nTop 10 Countries by Total Cases:")
display(global_summary.head(10))

# --- Task 4: Data Visualization ---
# Line Chart: Global Cumulative Cases Over Time
plt.figure(figsize=(10, 5))
sns.lineplot(data=data, x='Date_reported', y='Cumulative_cases')
plt.title('Global Cumulative COVID-19 Cases Over Time')
plt.xticks(rotation=45)
plt.show()

# Bar Chart: Top 10 Countries by Cases
plt.figure(figsize=(8, 5))
sns.barplot(x=global_summary.head(10).index, y=global_summary['Cumulative_cases'].head(10), palette='Blues_d')
plt.title('Top 10 Countries by COVID-19 Cases')
plt.xticks(rotation=45)
plt.show()

# Histogram: Distribution of Daily New Cases
plt.figure(figsize=(8, 5))
sns.histplot(data['New_cases'], bins=20, color='orange', kde=True)
plt.title('Distribution of Daily New Cases')
plt.show()

# Scatter Plot: New Cases vs. New Deaths
plt.figure(figsize=(8, 5))
sns.scatterplot(x='New_cases', y='New_deaths', data=data, hue='Country', legend=False)
plt.title('New Cases vs. New Deaths')
plt.show()
