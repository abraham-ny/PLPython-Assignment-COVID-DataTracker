import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("owid_covid_data.csv")

# Select a specific date for analysis (latest available data)
latest_data = df[df['date'] == df['date'].max()]

for country in ['Kenya', 'USA', 'India']:
    country_data = latest_data[latest_data['location'] == country]
    
    if country_data.empty:
        print(f"No data available for {country}")
        continue  # Skip to next country

    vaccinated = country_data['total_vaccinations'].values[0]
    population = country_data['population'].values[0]
    unvaccinated = population - vaccinated

    # Create Pie Chart
    labels = ['Vaccinated', 'Unvaccinated']
    sizes = [vaccinated, unvaccinated]
    colors = ['green', 'red']

    plt.figure(figsize=(6, 6))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=90)
    plt.title(f'Vaccination Distribution in {country}')
    plt.show()

