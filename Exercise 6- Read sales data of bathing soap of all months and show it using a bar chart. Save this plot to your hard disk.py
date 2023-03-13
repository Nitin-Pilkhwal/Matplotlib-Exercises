import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



#importing dataset which is saved locally
df = pd.read_csv('company_sales_data.csv')

bathingsoap = df['bathingsoap'].tolist()
monthlist = df['month_number'].tolist()
#Exercise 6

# Read the sales data of bathing soap of all months and show it using a bara chart and save this plot to your hard disk

#Solution

columns = ["month_number","facecream","facewash","toothpaste","bathingsoap","shampoo","moisturizer","total_units","total_profit"]

# Plotting the graph
plt.figure(figsize=(5,5))
plt.bar([a-0.25 for a in monthlist],bathingsoap,width=0.5,align='edge')
plt.xlabel('Months')
plt.title('Sales Data')
plt.ylabel('No. of soaps sell per year')
plt.grid(True,linestyle='--')
plt.xticks(monthlist)

plt.savefig('D:\sales_data_of_bathingsoap.png',dpi=150)

plt.show()