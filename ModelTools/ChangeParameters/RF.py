#-*-coding:utf8-*-
import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.model_selection import GridSearchCV

reload(sys)
sys.setdefaultencoding('utf-8')

train = pd.read_csv("train")
predictors = [x for x in train.columns if x != 'TARGET']
target = ['TARGET']
x_train, x_test, y_train, y_test = train_test_split(train[predictors],train[target], test_size=0.3, random_state=1729)

def rf():
    rf0 = RandomForestClassifier(oob_score=True, random_state=10)
    rf0.fit(x_train, y_train)
    print rf0.oob_score_
    y_predprob = rf0.predict_proba(x_test)[:, 1]
    print "AUC Score (Train): %f" % metrics.roc_auc_score(y_test, y_predprob)

def rf1():
    param_test1 = {'n_estimators': range(10, 71, 10)}
    gsearch1 = GridSearchCV(estimator=RandomForestClassifier(min_samples_split=100,
                                                             min_samples_leaf=20, max_depth=8, max_features='sqrt', random_state=10),
                            param_grid=param_test1, scoring='roc_auc', cv=5)
    gsearch1.fit(x_train, y_train)
    gsearch1.cv_results_, gsearch1.best_params_, gsearch1.best_score_

def rf2():
    param_test2 = {'max_depth': range(3, 14, 2), 'min_samples_split': range(50, 201, 20)}
    gsearch2 = GridSearchCV(estimator=RandomForestClassifier(n_estimators=60,
                                                             min_samples_leaf=20, max_features='sqrt', oob_score=True, random_state=10),
                            param_grid=param_test2, scoring='roc_auc', iid=False, cv=5)
    gsearch2.fit(x_train, y_train)
    gsearch2.cv_results_, gsearch2.best_params_, gsearch2.best_score_

def rf3():
    param_test3 = {'min_samples_split': range(80, 150, 20), 'min_samples_leaf': range(10, 60, 10)}
    gsearch3 = GridSearchCV(estimator=RandomForestClassifier(n_estimators=60, max_depth=13,
                                      max_features='sqrt',oob_score=True, random_state=10),
       param_grid=param_test3, scoring='roc_auc',iid=False, cv=5)
    gsearch3.fit(x_train, y_train)
    gsearch3.cv_results_, gsearch3.best_params_, gsearch3.best_score_

def rf4():
    param_test4 = {'max_features': range(3, 11, 2)}
    gsearch4 = GridSearchCV(estimator=RandomForestClassifier(n_estimators=60, max_depth=13, min_samples_split=120,
                                      min_samples_leaf=20, oob_score=True, random_state=10),
       param_grid=param_test4, scoring='roc_auc', iid=False, cv=5)
    gsearch4.fit(x_train, y_train)
    gsearch4.cv_results_, gsearch4.best_params_, gsearch4.best_score_