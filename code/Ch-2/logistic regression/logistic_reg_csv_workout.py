dataset = pd.read_csv('D:\\Work\\Books\\Python\\current-proj\\ML\\datasets\\logistic.csv')

# indexing
len(dataset)
dataset.columns
dataset.head()
dataset.head(2)
dataset['x1']
dataset[['x1','x2']]
dataset[['x1', 'x2', 'x3', 'x4']]
dataset['y'].astype('category').cat.categories

# setting index col
sl_no = range(29)
list(sl_no)
len(sl_no)
dataset['sl_no'] = sl_no

dataset.head()
dataset.set_index('sl_no', inplace=True)
dataset.head()

# indexing rows
dataset.iloc[0]
dataset.iloc[1]
dataset.iloc[1:3]

# fitting LR

data = dataset[['x1', 'x2', 'x3', 'x4']]
target = dataset['y']
target.astype('category').cat.categories

fit1 = LogisticRegressionCV(cv=5, random_state=True).fit(data, target)
fit1.score(data, target)

fit1.predict(data.iloc[0:2])
fit1.predict_proba(data.iloc[0:2])
