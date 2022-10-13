import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import train_test_split
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
import pickle
import seaborn as sns
from sklearn.metrics import confusion_matrix, accuracy_score

model=LinearRegression()
df=pd.read_csv(r"D:\Software_Coding Files\Verzeo-Python with machine learning\Passengerweed.csv")
print(df)

x=df.iloc[:,[0]].values
y=df.iloc[:,1].values
print(df.info())
model.fit(x,y)
print(model.predict([[42]]))
y_pred=model.predict(x)
print(y_pred)
plt.plot(x,y_pred)
plt.show()

print(r2_score(y_pred,y))
pickle.dump(model,open('tempo.pkl','wb'))
reload_model=pickle.load(open('tempo.pkl','rb'))

y_pred=reload_model.predict(x)
print(y_pred)
plt.plot(x,y_pred)
plt.show()