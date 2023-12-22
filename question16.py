
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('C:\\Users\\26kal\Downloads\sales_data - Sheet1.csv')

total_profit = data['Total profit'].sum()
plt.figure(figsize=(8, 6))

plt.plot(data['Months'], data['Total profit'], linestyle='--', color='blue', linewidth=4, label='Total Profit')
plt.xlabel('Months')
plt.ylabel('Total units')
plt.legend(loc='lower right')
plt.title(f'Total Profit of All Months: {total_profit}')
plt.show()

plt.figure(figsize=(8, 6))

plt.plot(data['Months'], data['Chair'], label='Chair')
plt.plot(data['Months'], data['Table'], label='Table')

plt.xlabel('Months')
plt.ylabel('Total Units')
plt.legend()

plt.title('Number of Units Sold per Month for Each Product')
plt.show()

chair_table_data = data[['Months', 'Chair', 'Table']]

bar_width = 0.35
index = chair_table_data.index

plt.bar(index, chair_table_data['Chair'], bar_width, label='Chair')
plt.bar(index + bar_width, chair_table_data['Table'], bar_width, label='Table')
plt.xlabel('Months')
plt.ylabel('Units Sold')
plt.xticks(index + bar_width / 2, chair_table_data['Months'])
plt.legend()

plt.title('Number of Units Sold per Month for Chair and Table')
plt.show()

plt.figure(figsize=(8, 6))

products = ['Chair', 'Table']
plt.stackplot(data['Months'], data[products].values.T, labels=products)
plt.xlabel('Months')
plt.ylabel('Units Sold')
plt.legend()

plt.title('Stack Plot of All Product Sales Data')
plt.show()

