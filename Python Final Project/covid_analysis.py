import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from datetime import datetime

# Set plotting style
sns.set_style('whitegrid')
plt.style.use('fivethirtyeight')
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 12

# Load the dataset
file_path = 'D:\PLP\Python Final Project\owid-covid-data.csv'
df = pd.read_csv(file_path)

# Display basic information
print(f"Dataset shape: {df.shape}")
print(f"Number of countries: {df['location'].nunique()}")
print(f"Date range: {df['date'].min()} to {df['date'].max()}")

# Preview the data
print(df.head())

# Check columns
print("Columns in the dataset:")
for i, col in enumerate(df.columns, 1):
    print(f"{i}. {col}")

# Missing values summary
missing_values = df.isnull().sum()
missing_percentage = (missing_values / len(df)) * 100
missing_df = pd.DataFrame({
    'Missing Values': missing_values,
    'Percentage': missing_percentage
})
print("\nColumns with missing values:")
print(missing_df[missing_df['Missing Values'] > 0].sort_values(by='Percentage', ascending=False))

# Convert 'date' to datetime
df['date'] = pd.to_datetime(df['date'])
df['month'] = df['date'].dt.month
df['year'] = df['date'].dt.year
df['day'] = df['date'].dt.day

# Focus countries
focus_countries = ['United States', 'India', 'Brazil', 'United Kingdom', 'Russia',
                   'France', 'Germany', 'South Africa', 'China', 'Japan']
df_focus = df[df['location'].isin(focus_countries)].copy()

# Latest data per country
latest_data = df.sort_values('date').groupby('location').tail(1).copy()

# Top 15 by total cases
top_countries_cases = latest_data.sort_values('total_cases', ascending=False).head(15)

# Bar plot
plt.figure(figsize=(14, 8))
sns.barplot(x='total_cases', y='location', data=top_countries_cases, palette='viridis')
plt.title('Top 15 Countries by Total COVID-19 Cases')
plt.xlabel('Total Cases')
plt.ylabel('Country')
plt.ticklabel_format(style='plain', axis='x')
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.show()

# Total cases over time
plt.figure(figsize=(16, 10))
for country in focus_countries:
    country_data = df[df['location'] == country]
    plt.plot(country_data['date'], country_data['total_cases'], label=country)
plt.title('COVID-19 Total Cases Over Time')
plt.xlabel('Date')
plt.ylabel('Total Cases')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.xticks(rotation=45)
plt.ticklabel_format(style='plain', axis='y')
plt.tight_layout()
plt.show()

# Total deaths over time
plt.figure(figsize=(16, 10))
for country in focus_countries:
    country_data = df[df['location'] == country]
    plt.plot(country_data['date'], country_data['total_deaths'], label=country)
plt.title('COVID-19 Total Deaths Over Time')
plt.xlabel('Date')
plt.ylabel('Total Deaths')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.xticks(rotation=45)
plt.ticklabel_format(style='plain', axis='y')
plt.tight_layout()
plt.show()

# New cases (7-day avg)
plt.figure(figsize=(16, 10))
for country in focus_countries:
    country_data = df[df['location'] == country]
    plt.plot(country_data['date'], country_data['new_cases_smoothed'], label=country)
plt.title('COVID-19 New Cases Over Time (7-day Rolling Average)')
plt.xlabel('Date')
plt.ylabel('New Cases (7-day avg)')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Death rate
latest_data['death_rate'] = (latest_data['total_deaths'] / latest_data['total_cases'].replace(0, np.nan)) * 100
death_rate_data = latest_data[latest_data['total_cases'] > 10000]
top_death_rates = death_rate_data.sort_values('death_rate', ascending=False).head(15)

plt.figure(figsize=(14, 8))
sns.barplot(x='death_rate', y='location', data=top_death_rates, palette='coolwarm')
plt.title('Top 15 Countries by COVID-19 Death Rate')
plt.xlabel('Death Rate (%)')
plt.ylabel('Country')
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.show()

# Vaccination progress
plt.figure(figsize=(16, 10))
for country in focus_countries:
    country_data = df[df['location'] == country]
    plt.plot(country_data['date'], country_data['people_fully_vaccinated_per_hundred'], label=country)
plt.title('Vaccination Progress (% Fully Vaccinated)')
plt.xlabel('Date')
plt.ylabel('% Fully Vaccinated')
plt.ylim(0, 100)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Top vaccinated countries
vaccination_data = latest_data.dropna(subset=['people_fully_vaccinated_per_hundred'])
vaccination_data = vaccination_data.sort_values('people_fully_vaccinated_per_hundred', ascending=False).head(15)

plt.figure(figsize=(14, 8))
sns.barplot(x='people_fully_vaccinated_per_hundred', y='location', data=vaccination_data, palette='viridis')
plt.title('Top 15 Countries by Vaccination Rate')
plt.xlabel('% Fully Vaccinated')
plt.ylabel('Country')
plt.xlim(0, 100)
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.show()

# Pie charts
plt.figure(figsize=(18, 15))
pie_countries = ['United States', 'India', 'United Kingdom', 'Brazil', 'South Africa', 'Japan']

for i, country in enumerate(pie_countries, 1):
    if country in latest_data['location'].values:
        country_data = latest_data[latest_data['location'] == country].iloc[0]
        vacc_pct = country_data['people_fully_vaccinated_per_hundred'] if not pd.isna(country_data['people_fully_vaccinated_per_hundred']) else 0
        pie_data = [vacc_pct, 100 - vacc_pct]
        labels = ['Fully Vaccinated', 'Not Fully Vaccinated']
        colors = ['#2ecc71', '#e74c3c']
        plt.subplot(2, 3, i)
        plt.pie(pie_data, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
        plt.title(f'{country} - Vaccination Status')
        plt.axis('equal')

plt.suptitle('Vaccination Status by Country (% of Population)', fontsize=18)
plt.tight_layout()
plt.subplots_adjust(top=0.9)
plt.show()

# Scatter plot: death rate vs vaccination
scatter_data = latest_data[
    (latest_data['total_cases'] > 10000) & 
    (~latest_data['people_fully_vaccinated_per_hundred'].isna())
]

plt.figure(figsize=(14, 10))
sns.scatterplot(
    data=scatter_data,
    x='people_fully_vaccinated_per_hundred',
    y='death_rate',
    hue='continent',
    size='total_cases',
    sizes=(50, 1000),
    alpha=0.7
)

for country in focus_countries:
    if country in scatter_data['location'].values:
        c_data = scatter_data[scatter_data['location'] == country].iloc[0]
        plt.annotate(
            country,
            (c_data['people_fully_vaccinated_per_hundred'], c_data['death_rate']),
            textcoords="offset points", xytext=(0, 5), ha='center'
        )

plt.title('Vaccination Rate vs Death Rate')
plt.xlabel('% Fully Vaccinated')
plt.ylabel('Death Rate (%)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
