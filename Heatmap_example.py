#Heatmaps (optional for correlation analysis)
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("owid_covid_data.csv")

# Select relevant numeric columns
columns_of_interest = ['total_cases', 'total_deaths', 'new_cases', 'new_deaths', 'total_vaccinations']
df_selected = df[columns_of_interest].dropna()

# Compute correlation matrix
corr_matrix = df_selected.corr()

# Plot heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)

plt.title('COVID-19 Data Correlation Heatmap')
plt.show()
