
#  Import Libraries and Read Data
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_excel(r"c:\Users\DELL\Downloads\sales_large.xlsx") 
# Explore the Data
print(df)                  # Print entire DataFrame
print(df.head(10))         # First 10 rows
print(df.tail(5))          # Last 5 rows
print(df.info())           # DataFrame info
print(df.columns)          # Columns names
print(df.shape)            # Rows and columns count
print(df.index)            # Index info
print(df.values)           # Values
print(df.dtypes)           # Data types
# Check for Missing Values
print(df.isnull())         # Check for nulls   
# Sales Analysis
total_sales=df['Sales'].sum()
avg_sales=df['Sales'].mean()
max_sales=df['Sales'].max()
min_sales=df['Sales'].min()
print(total_sales)
print(avg_sales)
print(max_sales)
print(min_sales)
print(df['Sales'].describe())
# Specific Data Access
print(df['Product'])        # Product column   
print(df.iloc[14])          # 15th row
print(df[df['Sales']>500]['Product'])         # Products with Sales > 500
print(df['Sales']>500)                          # Boolean mask
# Sort and Group Data
df=df.sort_values(by='Sales',ascending=False)
print(df)
grouped_max=df.groupby('Sales')['Sales'].max()
print(grouped_max)
grouped_min=df.groupby('Sales')['Sales'].min()
print(grouped_min)
#  Plotting
df.groupby('Product')['Sales'].sum().plot(kind='bar')
plt.title('Total Sales per Product')
plt.xlabel('Product')
plt.ylabel('Total Sales')
plt.show()
