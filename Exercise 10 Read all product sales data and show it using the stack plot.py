import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



#importing dataset which is saved locally
df = pd.read_csv('company_sales_data.csv')

#Exercise 7

# Exercise 7: Read the total profit of each month and show it using the histogram to see the most common profit ranges

#Solution

bathingsoap = df['bathingsoap'].tolist()
facewash = df['facewash'].tolist()
monthlist = df['month_number'].tolist()
moisturizer = df['moisturizer'].tolist()
toothpaste = df['toothpaste'].tolist()
facecream = df['facecream'].tolist()
shampoo = df['shampoo'].tolist()

columns = ["month_number","facecream","facewash","toothpaste","bathingsoap","shampoo","moisturizer","total_units","total_profit"]

# Plotting the graph
plt.figure(figsize=(5,5))
plt.title("All product sales data using stack plot")



plt.stackplot(monthlist, facecream, facewash, toothpaste, bathingsoap, shampoo, moisturizer,colors=['m','c','r','k','g','y'],labels=columns[1:7])

plt.xlabel('Month Number')
plt.ylabel('Sales unints in Number')
plt.legend(loc='upper left')
plt.legend()
plt.show()