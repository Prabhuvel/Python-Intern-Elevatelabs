import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load CSV using Pandas
df = pd.read_csv("sales_data.csv") 

# Step 2: Group by category (example: 'Product' or 'Region') and sum sales
# Assuming the CSV has columns: 'Product', 'Sales'
sales_summary = df.groupby("Product")["Sales"].sum().reset_index()

# Step 3: Plot the data
plt.figure(figsize=(8, 5))
plt.bar(sales_summary["Product"], sales_summary["Sales"], color='skyblue')
plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
