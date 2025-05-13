#Bar charts (top countries by total cases).
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("owid_covid_data.csv")

# Aggregate total cases by country
top_countries = df.groupby('location')['total_cases'].max().nlargest(10)  # Top 10 countries

# Create bar chart
plt.figure(figsize=(12, 6))
top_countries.sort_values().plot(kind='barh', color='skyblue')

plt.xlabel('Total Cases')
plt.ylabel('Country')
plt.title('Top 10 Countries by Total COVID-19 Cases')
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.show()
