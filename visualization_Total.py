#Line Chart(cases overtime)
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("owid_covid_data.csv")

# Convert date column to datetime format
df['date'] = pd.to_datetime(df['date'])

# Plot total cases over time
plt.figure(figsize=(10, 5))
for country in ['Kenya', 'USA', 'India']:
    country_data = df[df['location'] == country]
    plt.plot(country_data['date'], country_data['total_cases'], label=country)

plt.xlabel('Date')
plt.ylabel('Total Cases')
plt.title('Total COVID-19 Cases Over Time')
plt.legend()
plt.xticks(rotation=45)
plt.show()
