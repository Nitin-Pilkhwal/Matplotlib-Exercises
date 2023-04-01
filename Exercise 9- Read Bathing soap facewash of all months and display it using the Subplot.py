import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



#importing dataset which is saved locally
df = pd.read_csv('company_sales_data.csv')

#Solution

bathingsoap = df['bathingsoap'].tolist()
facewash = df['facewash'].tolist()
monthlist = df['month_number'].tolist()
columns = ["month_number","facecream","facewash","toothpaste","bathingsoap","shampoo","moisturizer","total_units","total_profit"]

# Plotting the graph
# plt.figure(figsize=(5,5))
plt.subplot(2,1,1)
plt.title('Sales data of Bathing Soap')
plt.plot(monthlist,bathingsoap,c='black',marker='o',linewidth=3)
plt.subplot(2,1,2)
plt.title('Sales data of facewash')
plt.plot(monthlist,facewash,c='r',marker='o',linewidth=3)

plt.xticks(monthlist)
plt.ylabel('Sales unit in number')
plt.xlabel('Month Number')
plt.show()