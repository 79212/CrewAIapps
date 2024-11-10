import pandas as pd
import matplotlib.pyplot as plt

# Load the data from CSV
df = pd.read_csv('./sales_product_cat.csv')

# Plot the vertical bar chart
plt.figure(figsize=(10,6))
colors = df['Product Category'].map({'Electronics': 'blue', 'Home Appliances': 'green', 'Furniture': 'orange'})
plt.bar(df['Product Name'], df['Revenue ($)'], color=colors)

# Adding titles and labels
plt.title('Revenue by Product Name')
plt.xlabel('Product Name')
plt.ylabel('Revenue ($)')
plt.xticks(rotation=45)

# Save the plot
plt.tight_layout()
plt.savefig('detailed_chart.png')
plt.show()