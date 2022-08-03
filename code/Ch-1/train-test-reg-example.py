import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score, cross_val_predict
from sklearn import metrics

# USING SIMULATIONS

X, y = np.arange(10).reshape((5, 2)), range(5)
list(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

# fit a model
lm = LinearRegression()
model = lm.fit(X_train, y_train)
predictions = lm.predict(X_test)

print(model.score(X_test, y_test))

scores = cross_val_score(model, X, y, cv=2)
print("Cross-validated scores:", scores)
predictions = cross_val_predict(model, X, y, cv=2)

# USING DIABETES DATA SET

# Load the Diabetes dataset

columns = "age sex bmi map tc ldl hdl tch ltg glu".split() # Declare the columns names
diabetes = datasets.load_diabetes() # Call the diabetes dataset from sklearn
df = pd.DataFrame(diabetes.data, columns=columns) # load the dataset as a pandas data frame
y = diabetes.target # define the target variable (dependent variable) as y

# create training and testing vars

X_train, X_test, y_train, y_test = train_test_split(df, y, test_size=0.2)
print(X_train.shape, y_train.shape)
print(X_test.shape, y_test.shape)

# fit a model

lm = linear_model.LinearRegression()
model = lm.fit(X_train, y_train)
predictions = lm.predict(X_test)

if __name__ == "__main__":
    print(X)
    print(y)
    print(X_train)
    print(X_test)
    print(y_train)
    print(y_test)
