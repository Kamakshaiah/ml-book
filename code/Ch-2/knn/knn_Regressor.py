# data
X = [[0], [1], [2], [3]]
y = [0, 0, 1, 1]

# fit
from sklearn.neighbors import KNeighborsRegressor
neigh = KNeighborsRegressor(n_neighbors=2)
neigh.fit(X, y)

# predict
print(neigh.predict([[1.5]]))
