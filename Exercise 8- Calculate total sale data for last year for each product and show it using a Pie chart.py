import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



#importing dataset which is saved locally
df = pd.read_csv('company_sales_data.csv')

#Exercise 7

# Exercise 7: Read the total profit of each month and show it using the histogram to see the most common profit ranges

#Solution

columns = ["month_number","facecream","facewash","toothpaste","bathingsoap","shampoo","moisturizer","total_units","total_profit"]


salesData   = [df ['facecream'].sum(), df ['facewash'].sum(), df ['toothpaste'].sum(),df ['bathingsoap'].sum(), df ['shampoo'].sum(),df ['moisturizer'].sum()]

# Plotting the graph
plt.figure(figsize=(5,5))
plt.pie(salesData,labels=columns[1:7],autopct="%1.1f%%")
plt.legend()
plt.show()