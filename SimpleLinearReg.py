import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
df=pd.read_csv('https://raw.githubusercontent.com/mariya-sherin/DSML/main/advertising%20-%20advertising.csv')
print(df)
x=df['TV']
Y=df['Sales']

x_train,x_test,y_train,y_test=train_test_split(x,Y,test_size=0.2)
x_train=x_train.values.reshape(-1,1)
x_test=x_test.values.reshape(-1,1)
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(x_train.reshape(-1, 1), y_train)

from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(x_train.reshape(-1, 1), y_train)
def sales_predicted(budget):
  return model.predict([[budget]])
print(sales_predicted(50))
slope = model.coef_[0]
intercept = model.intercept_
print("Slope:", slope)
print("Intercept:", intercept)
