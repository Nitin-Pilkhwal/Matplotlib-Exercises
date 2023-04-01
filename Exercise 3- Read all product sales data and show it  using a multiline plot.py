import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#importing dataset which is saved locally
df = pd.read_csv('company_sales_data.csv')

#Solution

columns = ["month_number","facecream","facewash","toothpaste","bathingsoap","shampoo","moisturizer","total_units","total_profit"]


#plotting the graph
plt.figure(figsize=(5,5))

plt.plot(df['month_number'],df['facecream'],marker='o',c='r',linewidth=3,label='facecream')
plt.plot(df['month_number'],df['facewash'],marker='o',c='blue',linewidth=3,label='facewash')
plt.plot(df['month_number'],df['toothpaste'],marker='o',c='orange',linewidth=3,label='toothpaste')
plt.plot(df['month_number'],df['bathingsoap'],marker='o',c='green',linewidth=3,label='bathingsoap')
plt.plot(df['month_number'],df['shampoo'],marker='o',c='brown',linewidth=3,label='shampoo')
plt.plot(df['month_number'],df['moisturizer'],marker='o',linewidth=3,label='moisturizer')

plt.xlabel('Unit')
plt.ylabel('Month Number')
plt.legend(loc = 'upper left')
plt.show()