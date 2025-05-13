import pandas as pd

# Load dataset
df = pd.read_csv("owid_covid_data.csv")

# Assume 'population' column exists in the dataset
df['vaccinated_percentage'] = (df['total_vaccinations'] / df['population']) * 100

# Display results
print(df[['date', 'location', 'vaccinated_percentage']].dropna())

