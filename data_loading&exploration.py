import pandas as pd

# Load the sales dataset
df = pd.read_csv("owid_covid_data.csv")

# Check column names
print(df.columns)

key_columns = ['date', 'location', 'total_cases', 'total_deaths', 'new_cases', 'new_deaths', 'total_vaccinations']

# Check if these columns exist
existing_columns = [col for col in key_columns if col in df.columns]
print("Key Columns Found:", existing_columns)

# Shows the first 5 rows by default
print(df[existing_columns].head())  # Display first few rows of key columns

#Identify missing values
print(df.isnull().sum())  # Shows the number of missing values in each column

# Filter the DataFrame to include only the specified countries
df = df[df["location"].isin(["Kenya", "USA", "India"])]
print("Filtered DataFrame:")
print(df[existing_columns].head())  # Display first few rows of key columns after filtering 

# Drop rows with missing dates and critical values
df = df.dropna(subset=['date', 'total_cases', 'total_deaths']) 

#Convert date column to datetime: pd.to_datetime().
df['date'] = pd.to_datetime(df['date'])

df = df.assign(
    total_vaccinations=df["total_vaccinations"].fillna(0),
    new_cases=df["new_cases"].fillna(df["new_cases"].mean())
)
# Fill missing values in 'total_vaccinations' with 0 and 'new_cases' with the mean of 'new_cases'
# Fill missing values in 'total_vaccinations' with 0 and 'new_cases' with the mean of 'new_cases'


df.fillna({"total_vaccinations": 0, "new_cases": df["new_cases"].mean()}, inplace=True)


