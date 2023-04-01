import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#importing dataset which is saved locally
df = pd.read_csv('company_sales_data.csv')


#Solution

columns = ["month_number","facecream","facewash","toothpaste","bathingsoap","shampoo","moisturizer","total_units","total_profit"]

facecream = df['facecream'].tolist()
facewash = df['facewash'].tolist()
monthlist = df['month_number'].tolist()

#plotting the graph
plt.figure(figsize=(5,5))

plt.bar([a-0.25 for a in monthlist],facecream,width=0.50,color='r',label='Facecream',align='edge')
plt.bar([a-0.25 for a in monthlist],facewash,width=-0.50,color='b',label='Facewash',align='edge')
plt.grid(True, linestyle="--")
plt.legend(loc = 'upper left')
plt.xticks(monthlist)

plt.show()