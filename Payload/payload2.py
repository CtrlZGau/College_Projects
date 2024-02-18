from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,r2_score

iris = load_iris()

# setting yp the data for training
Y = np.asarray(iris.target)

X= np.asarray(iris.data)
X = np.delete(X,1,axis=1)
X = np.delete(X,2,axis=1)

X_train, X_test, y_train, y_test = train_test_split(X,Y,test_size=0.2,random_state=50)

# Initialising the model
model = LogisticRegression()
model.fit(X_train,y_train)

#Prediction
y_predicted = model.predict(X_test)

# Evaluation of training model
mse = mean_squared_error(y_test,y_predicted)
r2 = r2_score(y_test,y_predicted)
print("Mean Squared Error: ",mse)
print("R-squared Error: ",r2)




