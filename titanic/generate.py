import numpy as np
import pandas as pd
import statistics
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import cross_val_score
from sklearn.externals import joblib

def compute_score(cfl, X, y):
    xval = cross_val_score(cfl, X, y, cv=5)
    return statistics.mean(xval)

df = pd.read_csv('./titanic.csv')

df = df[['age', 'sex', 'pclass', 'survived', 'embarked', 'fare']]

df = df.replace('male', 0)
df = df.replace('female', 1)

df['age'] = df['age'].fillna(df['age'].mean())
df['fare'] = df['fare'].fillna(df['fare'].mean())
df['is_child'] = df.age < 8

df['embarked'] = df['embarked'].fillna(1)
df['embarked'] = df['embarked'].replace('S', 0)
df['embarked'] = df['embarked'].replace('C', 1)
df['embarked'] = df['embarked'].replace('Q', 2)

features = df[['is_child', 'sex', 'pclass', 'embarked', 'fare']]
target   = df['survived']

X_train, X_test, y_train, y_test = train_test_split(features, target, test_size = 0.30)

rf = RandomForestClassifier()
rf.fit(X_train, y_train)

y_predicted = rf.predict(X_test)
outcome = pd.DataFrame(confusion_matrix(y_predicted, y_test), index = ['Not survived', 'Survived'], columns = ['Not survived', 'Survived'])
score = compute_score(rf, X_test, y_test)

print(score, outcome)
joblib.dump(rf, 'RandomForest.pkl')

passenger = [[1, 1, 1, 1, 1]]
print(rf.predict(passenger))
