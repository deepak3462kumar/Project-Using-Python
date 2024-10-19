import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Load the CSV file
file_path = 'Olympic.csv'
df = pd.read_csv(file_path)

# Set the aesthetic style of the plots
sns.set(style="whitegrid")

# 1. Top 5 countries by total medals
top_medal_countries = df[['country', 'total', 'gold', 'silver', 'bronze']].sort_values(by='total', ascending=False).head(5)

plt.figure(figsize=(10, 6))
sns.barplot(x='total', y='country', data=top_medal_countries, palette='viridis')
plt.title('Top 5 Countries by Total Medals', fontsize=16)
plt.xlabel('Total Medals')
plt.ylabel('Country')
plt.show()

# 1a. Medal type breakdown (gold, silver, bronze)
top_countries_medals = df[['country', 'gold', 'silver', 'bronze']].sort_values(by='gold', ascending=False).head(5)
top_countries_medals.set_index('country').plot(kind='bar', stacked=True, figsize=(10, 6), colormap='tab20c')
plt.title('Medal Breakdown (Gold, Silver, Bronze) - Top 5 Countries', fontsize=16)
plt.xlabel('Country')
plt.ylabel('Number of Medals')
plt.show()


# 3. Top 5 countries by medals per capita (total medals / population in millions)
df['medals_per_capita'] = df['total'] / df['population']
top_medals_per_capita = df[['country', 'medals_per_capita']].sort_values(by='medals_per_capita', ascending=False).head(5)

plt.figure(figsize=(10, 6))
sns.barplot(x='medals_per_capita', y='country', data=top_medals_per_capita, palette='plasma')
plt.title('Top 5 Countries by Medals Per Capita', fontsize=16)
plt.xlabel('Medals Per Capita (per million people)')
plt.ylabel('Country')
plt.show()

# 4. GDP per medal (GDP in billions / total medals) - Inefficiency
df['gdp_per_medal'] = df['gdp'] / df['total']
top_gdp_per_medal = df[['country', 'gdp_per_medal']].sort_values(by='gdp_per_medal', ascending=False).head(5)

plt.figure(figsize=(10, 6))
sns.barplot(x='gdp_per_medal', y='country', data=top_gdp_per_medal, palette='magma')
plt.title('Top 5 Countries by GDP Per Medal (Inefficiency)', fontsize=16)
plt.xlabel('GDP Per Medal (in billions)')
plt.ylabel('Country')
plt.show()

# 5. GDP vs. total medals (scatter plot with trend line)
plt.figure(figsize=(10, 6))
sns.regplot(x='gdp', y='total', data=df, scatter_kws={'s':50}, color='b', line_kws={"color": "red"})
plt.title('GDP vs Total Medals', fontsize=16)
plt.xlabel('GDP (in billions)')
plt.ylabel('Total Medals')
plt.show()

# 6. Population vs. total medals (scatter plot with trend line)
plt.figure(figsize=(10, 6))
sns.regplot(x='population', y='total', data=df, scatter_kws={'s':50}, color='g', line_kws={"color": "orange"})
plt.title('Population vs Total Medals', fontsize=16)
plt.xlabel('Population (in millions)')
plt.ylabel('Total Medals')
plt.show()

# 7. Medal Efficiency Index (medals per capita / GDP per capita)
# First calculate GDP per capita (GDP / population)
df['gdp_per_capita'] = df['gdp'] / df['population']
df['medal_efficiency_index'] = df['medals_per_capita'] / df['gdp_per_capita']

top_efficiency = df[['country', 'medal_efficiency_index']].sort_values(by='medal_efficiency_index', ascending=False).head(5)

plt.figure(figsize=(10, 6))
sns.barplot(x='medal_efficiency_index', y='country', data=top_efficiency, palette='coolwarm')
plt.title('Top 5 Countries by Medal Efficiency Index', fontsize=16)
plt.xlabel('Medal Efficiency Index')
plt.ylabel('Country')
plt.show()
