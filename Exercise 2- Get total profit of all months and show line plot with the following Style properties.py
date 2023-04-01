import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#importing dataset which is saved locally
df = pd.read_csv('company_sales_data.csv')

#Solution

columns = ["month_number","facecream","facewash","toothpaste","bathingsoap","shampoo","moisturizer","total_units","total_profit"]


#plotting the graph
plt.figure(figsize=(5,5))

plt.plot(df['month_number'],df['total_units'],c='r',linestyle='--',marker='o',linewidth=3,label='Total Units')
plt.title('Company profit per month')
plt.xlabel('Month Number')
plt.ylabel('Sold units number')
plt.legend(loc = 'lower right')

plt.show()