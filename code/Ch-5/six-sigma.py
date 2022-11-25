## https://github.com/samirsaci/lss-logistic-regression/blob/main/Logistic%20Regression.ipynb
## minimum bonus needed to reach 75% of a productivity target

# plots

import seaborn as sns
plt.figure(figsize=(12, 6))
ax = plt.gca()
sns.regplot(x='Lines', y='Error', data=df_pickaccuracy, logistic=True, ax = ax)
plt.xlabel('Number of Lines per Wave (Lines/Wave)')
plt.ylabel('Probability of picking error in the wave')
plt.show()

# logistic regression

import scipy.stats as stat
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Define X, y
X = df_pickaccuracy[['Lines']]
y = df_pickaccuracy['Error']
# Training/Test Sets 
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=0)
# Instantiate the model
log_regression = LogisticRegression()
# Fit your model
log_regression.fit(X_train,y_train)

# Calculate p-value (source: https://gist.github.com/rspeare/77061e6e317896be29c6de9a85db301d)
denom = (2.0*(1.0+np.cosh(log_regression.decision_function(X))))
denom = np.tile(denom,(X.shape[1],1)).T
# Fisher Information Matrix
F_ij = np.dot((X/denom).T,X)
## Inverse Information Matrix
Cramer_Rao = np.linalg.inv(F_ij) 
sigma_estimates = np.sqrt(np.diagonal(Cramer_Rao))
# z-score for eaach model coefficient
z_scores = log_regression.coef_[0]/sigma_estimates 
# two tailed test for p-values
p_values = [stat.norm.sf(abs(x))*2 for x in z_scores] 

print("p-value: {}".format(p_values[0]))

# final plot

plt.figure(figsize=(12, 6))
ax = plt.gca()
sns.regplot(x='Incentive', y='Target', data=df_incentive, logistic=True, ax = ax)
plt.xlabel('Productivity Incentive (Euros/Day)')
plt.ylabel('Probability of meeting the productivity target')
plt.show()
