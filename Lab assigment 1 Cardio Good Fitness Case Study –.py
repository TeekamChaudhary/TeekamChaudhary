import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv("C:/Users/teeka/Downloads/CardioGoodFitness.csv")

products = ['TM195', 'TM498', 'TM798']
sales = [50, 30, 20]


plt.bar(products, sales)


plt.title('Product Sales')
plt.xlabel('Product')
plt.ylabel('Sales')

variables = ['gender', 'age', 'education', 'relationship status', 'annual household income', 
             'average times per week', 'average miles per week', 'self-rated fitness']
for var in variables:
    plt.figure(figsize=(10,4))
    sns.histplot(data=df, x=var, kde=True)
    plt.title('Histogram of ' + var)
    plt.show()
