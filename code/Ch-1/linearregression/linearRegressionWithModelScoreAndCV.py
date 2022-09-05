# data simulatins

import numpy as np
from sklearn.model_selection import train_test_split

X, y = np.arange(10).reshape((5, 2)), range(5)
X_train, X_test, y_train, y_test = train_test_split(X , y, test_size=0.33, random_state=42)

# linear regression

from sklearn.linear_model import LinearRegression

lm = LinearRegression()
model = lm.fit(X_train, y_train)
predictions = lm.predict(X_test)

print(model.score(X_test, y_test))
print(predictions)

# cross validation

from sklearn.model_selection import cross_val_score, cross_val_predict

scores = cross_val_score(model, X, y, cv=2)
predictions = cross_val_predict(model, X, y, cv=2)

print(scores)
print(predictions)
