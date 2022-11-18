# data 
samples = [[0., 0., 0.], [0., .5, 0.], [1., 1., .5]]

# fit/model
from sklearn.neighbors import NearestNeighbors
neigh = NearestNeighbors(n_neighbors=1)
neigh.fit(samples)

# NN
print(neigh.kneighbors([[1., 1., 1.]]))
