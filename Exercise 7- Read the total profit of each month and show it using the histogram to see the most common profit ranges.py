import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



#importing dataset which is saved locally
df = pd.read_csv('company_sales_data.csv')

totalprofit = df['total_profit'].tolist()
monthlist = df['month_number'].tolist()


# Exercise 7: Read the total profit of each month and show it using the histogram to see the most common profit ranges

#Solution

columns = ["month_number","facecream","facewash","toothpaste","bathingsoap","shampoo","moisturizer","total_units","total_profit"]

# Plotting the graph
plt.figure(figsize=(5,5))

profit_range = [150000, 175000, 200000, 225000, 250000, 300000, 350000]
plt.hist(totalprofit,profit_range,label='Profit Data')
plt.legend()
plt.show()