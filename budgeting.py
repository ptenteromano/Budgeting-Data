
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[101]:


def trunc(num, trim):
    return float(format(num, trim))


# In[49]:


expenses = pd.read_excel('expenses.xlsx')
income = pd.read_excel('income.xlsx')


# In[50]:


income.set_index('Month', inplace=True)
expenses.set_index('Name', inplace=True)


# In[51]:

print(income['Income2'].sum())
totalIncome = income['Income1'].sum() + income['Income2'].sum()
totalIncome


# In[102]:


totalMonthlyIncomeEqual = trunc(totalIncome/12,'0.2f')
totalMonthlyIncomeEqual


# In[103]:


totalMonthlyExpense = trunc(expenses['Expense'].sum(), '0.2f')
totalMonthlyExpense


# In[104]:


totalMonthlyWithoutRent = trunc(totalMonthlyExpense - expenses.loc['Rent']['Expense'], '0.2f')
totalMonthlyWithoutRent


# In[63]:


rent = expenses.loc['Rent']['Expense']
rent = int(rent)
rent


# In[105]:


rentPercent = trunc(rent/totalMonthlyIncomeEqual,'0.4f')
rentPercent *= 100
rentPercent


# In[112]:


targetRentPrice = trunc(.30 * totalMonthlyIncomeEqual, '0.2f')
targetRentPrice


# In[106]:


otherCostPercent = trunc(totalMonthlyWithoutRent / totalMonthlyIncomeEqual, '0.4f')
otherCostPercent *= 100
otherCostPercent


# In[92]:


totalPercentOfIncome = otherCostPercent + rentPercent
totalPercentOfIncome


# In[123]:


spendingMoney = trunc(totalPercentOfIncome/100 * totalMonthlyIncomeEqual, '0.2f')
spendingMoney


# In[124]:


a = pd.DataFrame(columns=['Rent Percentage', 'Expense Percentage', 'Total Percentage', 'Avg Monthly Income', 'Spending Money'])


# In[125]:


a.loc[0] = [rentPercent, otherCostPercent, totalPercentOfIncome, totalMonthlyIncomeEqual, spendingMoney]


# In[127]:


a.to_excel('./result.xlsx')


# In[130]:


print("Results...")
print("Average Monthly Income: ", totalMonthlyIncomeEqual)
print("Rent Percentage: ", rentPercent)
print("Other Expenses Percentage: ", otherCostPercent)
print("Total Percentage of Income: ", totalPercentOfIncome)
print("Left over Cash: ", spendingMoney)

