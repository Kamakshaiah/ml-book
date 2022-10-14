from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegressionCV
X, y = load_iris(return_X_y=True)

clf = LogisticRegressionCV(cv=5, random_state=0).fit(X, y)
clf.predict(X[:2, :])
clf.predict_proba(X[:2, :]).shape
clf.score(X, y)

