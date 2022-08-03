# Linear Regression
import numpy as np
from sklearn import datasets
from sklearn.linear_model import LinearRegression

# load the diabetes datasets
dataset = datasets.load_diabetes()

# fit a linear regression model to the data
model = LinearRegression()
model.fit(dataset.data, dataset.target)
print(model)

# make predictions
expected = dataset.target
predicted = model.predict(dataset.data)

# >>>>>>>Print out the statistics<<<<<<<<<<<<<
model.summary() # not work

# summarize the fit of the model
mse = np.mean((predicted-expected)**2)
print model.intercept_, model.coef_, mse, 
print(model.score(dataset.data, dataset.target))