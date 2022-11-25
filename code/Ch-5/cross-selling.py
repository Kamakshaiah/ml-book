import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#!pip install imblearn

from sklearn.metrics import accuracy_score, f1_score,auc
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier

df= pd.read_csv('/content/train_data.csv') 
df.shape
df.head()

df.isna()

# plots

sns.countplot(ax=axes[0,0],x='Gender',hue='Response',data=df,palette="mako") 
sns.countplot(ax=axes[0,1],x='Driving_License',hue='Response',data=df,palette="mako") 
sns.countplot(ax=axes[1,0],x='Previously_Insured',hue='Response',data=df,palette="mako") 
sns.countplot(ax=axes[1,1],x='Vehicle_Age',hue='Response',data=df,palette="mako")

sns.countplot(x='Vehicle_Damage',hue='Response',data=df,palette="mako")

Response = df.loc[:,"Response"].value_counts().rename('Count')
plt.xlabel("Response")
plt.ylabel('Count')
sns.barplot(Response.index , Response.values,palette="mako")

sns.displot(df['Age'])
sns.distplot(df['Annual_Premium'])

# data processing

def data_prep(df):
    df= df.drop(columns=['id','Policy_Sales_Channel','Vintage'])
    df=pd.get_dummies(df,columns=['Gender'] ,prefix='Gender')
    df=pd.get_dummies(df,columns=['Vehicle_Damage'] ,prefix='Damage')
    df=pd.get_dummies(df,columns=['Driving_License'] ,prefix='License')
    df=pd.get_dummies(df,columns=['Previously_Insured'] ,prefix='prev_insured')
    df["Age"] = pd.cut(df['Age'], bins=[0, 29, 35, 50, 100])
    df['Age']= df['Age'].cat.codes
    df['Annual_Premium'] = pd.cut(df['Annual_Premium'], bins=[0, 30000, 35000,40000, 45000, 50000, np.inf])
    df['Annual_Premium']= df['Annual_Premium'].cat.codes
    df['Vehicle_Age'] =df['Vehicle_Age'].map({'< 1 Year': 0, '1-2 Year': 1, '> 2 Years': 2})
    df.drop(columns=['Region_Code'],inplace= True)
    return df

df1=data_prep(df)

Features= ['Age','Vehicle_Age','Annual_Premium',"Gender_Female","Gender_Male","Damage_No","Damage_Yes", "License_0","License_1" ,"prev_insured_0", "prev_insured_1"]

# train-test-split

from sklearn.model_selection import train_test_split 
X_train, X_test, Y_train, Y_test = train_test_split(df1[Features],df1['Response'], test_size = 0.3, random_state = 101)
X_train.shape,X_test.shape

from imblearn.under_sampling import RandomUnderSampler
RUS = RandomUnderSampler(sampling_strategy=.5,random_state=3,)
X_train,Y_train  = RUS.fit_resample(df1[Features],df1['Response'])

def performance_met(model,X_train,Y_train,X_test,Y_test):
    acc_train=accuracy_score(Y_train, model.predict(X_train))
    f1_train=f1_score(Y_train, model.predict(X_train))
    acc_test=accuracy_score(Y_test, model.predict(X_test))
    f1_test=f1_score(Y_test, model.predict(X_test))
    print("train score: accuracy:{} f1:{}".format(acc_train,f1_train))
    print("test score: accuracy:{} f1:{}".format(acc_test,f1_test))

# logistic reg.

model = LogisticRegression()
model.fit(X_train,Y_train) 
performance_met(model,X_train,Y_train,X_test,Y_test)

#Decision Tree

model_DT=DecisionTreeClassifier(random_state=1) 
model_DT.fit(X_train,Y_train) 
performance_met(model_DT,X_train,Y_train,X_test,Y_test)

#Random forest
Forest= RandomForestClassifier(random_state=1) 
Forest.fit(X_train,Y_train) 
performance_met(Forest,X_train,Y_train,X_test,Y_test)

# Hyperparameter tuning

rf= RandomForestClassifier(random_state=1)

parameters = {
    'bootstrap': [True],
    'max_depth': [20, 25],
    'min_samples_leaf': [3, 4],
    'min_samples_split': [100,300],
}

grid_search_1 = GridSearchCV(rf, parameters, cv=3, verbose=2, n_jobs=-1)
grid_search_1.fit(X_train, Y_train)
performance_met(grid_search_1,X_train,Y_train,X_test,Y_test)
