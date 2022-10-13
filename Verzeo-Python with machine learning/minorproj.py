import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn import preprocessing
import matplotlib.pyplot as plt
import pickle
import seaborn as sns
from sklearn.metrics import accuracy_score

test = pd.read_csv(r"D:\Software_Coding Files\Verzeo-Python with machine learning\test.csv")
train = pd.read_csv(r"D:\Software_Coding Files\Verzeo-Python with machine learning\train.csv")

#training 

print(train.head())
train_numeric_data=train
label_encoder = preprocessing.LabelEncoder()
train_numeric_data['Sex']= label_encoder.fit_transform(train_numeric_data['Sex']) 
train_numeric_data['Sex'].unique()
train_numeric_data['Embarked']= label_encoder.fit_transform(train_numeric_data['Embarked']) 
train_numeric_data['Embarked'].unique()
train_numeric_data=train_numeric_data.drop(['PassengerId'],axis=1)
train_numeric_data=train_numeric_data.drop(['Cabin'],axis=1)
train_numeric_data=train_numeric_data.dropna()
print("__________________")
print(train_numeric_data)
print("######################################")
print(train_numeric_data.info())
print("######################################")
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
train_numeric_data=train_numeric_data.select_dtypes(include=['float64','int64','int32'])
x=train_numeric_data.iloc[:,1:8].values
y=train_numeric_data.iloc[:,0].values
x_train,x_test,y_train,y_test = train_test_split(x,y,random_state=0)
model=LogisticRegression()
model.fit(x_train,y_train)
y_pred=model.predict(x_test)
print("###########")
print(y_pred)
print("###########")
print(y_test)
print("###########")
print(r2_score(y_test,y_pred))

sns.histplot(x='Pclass', data=train)
plt.title("Count of People in Passenger Class")
plt.show()

sns.histplot(x='Age', data=train)
plt.title("Count of People in Age")
plt.show()

plt.plot(train['Embarked'].value_counts())
plt.title("Count of People in Embarked")

print("^^^^^^^^^^^^^^^^^^")
print("Max: ",max(max(train['Fare']),max(test['Fare'])))
print("Min: ",min(min(train['Fare']),min(test['Fare'])))
print(max(test['Fare']))

plt.show()


#testing

test_numeric_data=test
label_encoder = preprocessing.LabelEncoder()
test_numeric_data['Sex']= label_encoder.fit_transform(test_numeric_data['Sex']) 
test_numeric_data['Sex'].unique()
test_numeric_data['Embarked']= label_encoder.fit_transform(test_numeric_data['Embarked']) 
test_numeric_data['Embarked'].unique()
test_numeric_data=test_numeric_data.drop(['PassengerId'],axis=1)
test_numeric_data=test_numeric_data.drop(['Cabin'],axis=1)
test_numeric_data=test_numeric_data.dropna()

test_numeric_data=test_numeric_data.select_dtypes(include=['float64','int64','int32'])
input=test_numeric_data.iloc[:,0:8].values
output=model.predict(input)

print("**********************************************************")
print(output)










