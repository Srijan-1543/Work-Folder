import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

d = {
    "First column": pd.Series([1,2,3,4,5,6],index=["one","two","three","four","five","six"]),
    "Second column":pd.Series([1,2,3,4],index=["one","two","three","four"])
}
df=pd.DataFrame(d)
print(df)

data = np.array(["aaa","bbb","ccc","ddd"])
df=pd.DataFrame(data)
print(df)

a = [1,2,3,4,5]
b = [0,2,5,6,8]
plt.plot(a,b)
plt.show()