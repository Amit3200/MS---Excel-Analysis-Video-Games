import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

df=pd.read_excel("salesrp.xlsx")
df.head()
df=df.fillna(0)
print(df)
df1=df
X=df["Genres"]
y=np.array(y)
Y=df[["Action","Adventure","Fighting","Misc","Platform","Puzzle","Racing","Role-Playing","Shooter","Simulation","Sports","Strategy"]]   
X=df[['Genres']]
reg=LinearRegression().fit(X,Y)
rk17=reg.predict([[2017]])
rk18=reg.predict([[2018]])
rk19=reg.predict([[2019]])
rk20=reg.predict([[2020]])
print(rk17)
for i in rk17[0]:
    print(i)
Y=[rk17,rk18,rk19,rk20]
X=[2017,2018,2019,2020]
d={2017:list(rk17[0]),2018:list(rk18[0]),2019:list(rk19[0]),2020:list(rk20[0])}
df12=pd.DataFrame.from_dict(d)
df12.to_csv('out1.csv')

