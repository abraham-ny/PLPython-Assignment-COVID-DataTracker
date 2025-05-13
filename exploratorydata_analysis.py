#plot cases over time for selected countries
import pandas as pd
import matplotlib.pyplot as plt

#Load data
df =pd.read_csv("owid_covid_data.csv")
#Convert date column to datetime
df['date'] = pd.to_datetime(df['date'])

#Plot total cases over time for the countires
plt.figure(figsize=(12, 6))
for country in ['Kenya', 'USA', 'India']:
    country_data = df[df['location'] == country]
    plt.plot(country_data['date'], country_data['total_cases'], label=country)

    plt.xlabel('date')
    plt.ylabel('Total Cases')
    plt.title('Total COVID-19 Cases Over Time')
    plt.legend()
    plt.xticks(rotation=45)
    plt.show()


