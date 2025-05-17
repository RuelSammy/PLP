
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('iris_sample.csv')

print("First 5 rows:")
print(df.head())

print("\nData types:")
print(df.dtypes)

print("\nMissing values:")
print(df.isnull().sum())

print("\nBasic statistics:")
print(df.describe())

print("\nGroup mean by species:")
print(df.groupby('species').mean(numeric_only=True))

plt.figure(figsize=(16, 10))

plt.subplot(2, 2, 1)
plt.plot(df.index, df['sepal_length'], marker='o')
plt.title('Sepal Length Trend')
plt.xlabel('Index')
plt.ylabel('Sepal Length')

plt.subplot(2, 2, 2)
sns.barplot(x='species', y='petal_length', data=df)
plt.title('Average Petal Length per Species')

plt.subplot(2, 2, 3)
plt.hist(df['sepal_width'], bins=5, color='skyblue', edgecolor='black')
plt.title('Distribution of Sepal Width')
plt.xlabel('Sepal Width')

plt.subplot(2, 2, 4)
plt.scatter(df['sepal_length'], df['petal_length'], c='green')
plt.title('Sepal Length vs Petal Length')
plt.xlabel('Sepal Length')
plt.ylabel('Petal Length')

plt.tight_layout()
plt.show()
