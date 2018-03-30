# source https://whatamilookingatblog.wordpress.com/2017/05/19/machine-learning-exercise-using-the-kaggle-titanic-dataset-random-forest/

from flask import Flask
from flask_cors import CORS
from flask import request

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.externals import joblib

app = Flask(__name__)
CORS(app)

rf = joblib.load('RandomForest.pkl')
#Model ['is_child', 'Sex', 'Pclass', 'Embarked', 'Fare']

@app.route("/titanic/passenger", methods=["POST"])
def titanic():
    age       = int(request.form['age'])
    is_child  = True if age < 8 else False
    sex       = int(request.form['sex'])
    pclass    = int(request.form['pclass'])
    embarked  = int(request.form['embarked'])
    fare      = float(request.form['fare'])
    passanger = [[is_child, sex, pclass, embarked, fare]]
#    print(passanger)
    return rf.predict_proba(passanger)[0][1].astype('str')
