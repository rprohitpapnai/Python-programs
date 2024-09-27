import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from pandas.core.interchange.dataframe_protocol import DataFrame
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier



diabetes=pd.read_csv("diabetes.csv")
diabetes.dropna(axis=0,subset=['Outcome'],inplace=True)

Y=diabetes.Outcome
X=diabetes.drop('Outcome', axis=1)
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2)
model=RandomForestClassifier()
model.fit(X_train,Y_train)
Y_pred=model.predict(X_test)
print('accuracy:',accuracy_score(Y_pred,Y_test))
knn=KNeighborsClassifier(2)
knn.fit(X_train,Y_train)
k_pred=knn.predict(X_test)
print('accuracy',accuracy_score(k_pred,Y_test))
