import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#importing dataset which is saved locally
df = pd.read_csv('company_sales_data.csv')

#Exercise 4

# add a grid in the plot. gridline style should "-".


#Solution

columns = ["month_number","facecream","facewash","toothpaste","bathingsoap","shampoo","moisturizer","total_units","total_profit"]


#plotting the graph
plt.figure(figsize=(5,5))

plt.scatter(x=df['month_number'],y=df['toothpaste'],label='Toothpaste Sales')
plt.grid(True,linestyle='--')
plt.title('Monthly Toothpaste Sale')
plt.xlabel('Month number')
plt.ylabel('Toothpaste Stock')
plt.legend()
plt.show()
