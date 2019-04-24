#-*-coding:utf8-*-
import sys
import pandas as pd
from sklearn.model_selection import train_test_split
import xgboost as xgb
from sklearn.metrics import roc_curve
from sklearn import metrics
import matplotlib.pyplot as plt
from sklearn.metrics import auc
from sklearn.model_selection import GridSearchCV

reload(sys)
sys.setdefaultencoding('utf-8')

train = pd.read_csv("train")
predictors = [x for x in train.columns if x != 'TARGET']
target = 'TARGET'
x_train, x_test, y_train, y_test = train_test_split(train[predictors], train[target].values, test_size=0.3, random_state=1729)

def PlotRoc(Algorithm, PR, TR):
    roc_auc = auc(PR, TR)
    plt.title("ROC curve of %s (AUC = %.4f)" % (Algorithm, roc_auc))
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.ylim(0.0, 1.0)
    plt.xlim(0.0, 1.0)
    plt.plot(PR, TR)
    plt.show()

#调优子估计器数目
def param_test():
    param_test = {
     'n_estimators': range(100, 1800, 200),
    }
    xgb1 = xgb.XGBClassifier(
             learning_rate=0.1,
             max_depth=5,
             min_child_weight=5,
             gamma=0,
             subsample=1.0,
             colsample_bytree=0.8,
             objective='binary:logistic',
             nthread=3,
             seed=27)

    gsearch1 = GridSearchCV(estimator=xgb1, param_grid=param_test, scoring='roc_auc', iid=False, cv=5)
    gsearch1.fit(x_train, y_train)
    print gsearch1.cv_results_, gsearch1.best_params_, gsearch1.best_score_

#param_test()


def param_test1():
    param_test1 = {
     'max_depth': range(3, 10, 2),
     'min_child_weight': range(1, 6, 2)
    }
    gsearch1 = GridSearchCV(
            estimator=xgb.XGBClassifier(
                    learning_rate=0.1,
                    n_estimators=300,
                    max_depth=5,
                    min_child_weight=5,
                    gamma=0,
                    subsample=1.0,
                    colsample_bytree=0.8,
                    objective='binary:logistic',
                    nthread=4,
                    seed=27),
            param_grid=param_test1,
            scoring='roc_auc',
            iid=False, cv=5)
    gsearch1.fit(x_train, y_train)
    print gsearch1.cv_results_, gsearch1.best_params_, gsearch1.best_score_

#param_test1()

def param_test3():
    param_test3 = {
     'gamma':[i/10.0 for i in range(0, 5)]
    }
    gsearch3 = GridSearchCV(
            estimator=xgb.XGBClassifier(
                    learning_rate=0.1,
                    n_estimators=140,
                    max_depth=5,
                    min_child_weight=3,
                    gamma=0,
                    subsample=1.0,
                    colsample_bytree=0.8,
                    objective='binary:logistic',
                    nthread=4,
                    seed=27),
            param_grid=param_test3,
            scoring='roc_auc',
            iid=False, cv=5)
    gsearch3.fit(x_train, y_train)
    print gsearch3.cv_results_, gsearch3.best_params_, gsearch3.best_score_

#param_test3()

def param_test4():
    param_test4 = {
     'subsample':[i/10.0 for i in range(6, 10)],
     'colsample_bytree':[i/10.0 for i in range(6, 10)]
    }
    gsearch4 = GridSearchCV(
            estimator=xgb.XGBClassifier(
                    learning_rate=0.1,
                    n_estimators=300,
                    max_depth=5,
                    min_child_weight=3,
                    gamma=0.3,
                    subsample=1.0,
                    colsample_bytree=0.8,
                    objective='binary:logistic',
                    nthread=4,
                    seed=27),
            param_grid=param_test4,
            scoring='roc_auc',
            iid=False, cv=5)
    gsearch4.fit(x_train, y_train)
    print gsearch4.cv_results_, gsearch4.best_params_, gsearch4.best_score_

#param_test4()

def param_test6():
    param_test6 = {
     'reg_alpha':[1e-5, 1e-2, 0.1, 1, 100]
    }
    gsearch6 = GridSearchCV(
            estimator=xgb.XGBClassifier(
                    learning_rate=0.1,
                    n_estimators=300,
                    max_depth=5,
                    min_child_weight=3,
                    gamma=0.3,
                    subsample=0.8,
                    colsample_bytree=0.8,
                    objective='binary:logistic',
                    nthread=4,
                    seed=27),
            param_grid=param_test6,
            scoring='roc_auc',
            iid=False, cv=5)
    gsearch6.fit(x_train, y_train)
    print gsearch6.cv_results_, gsearch6.best_params_, gsearch6.best_score_

#param_test6()


def param_test7():
    param_test7 = {
     'reg_alpha':[0, 1e-5, 0.001, 0.005, 0.01]
    }
    gsearch7 = GridSearchCV(
            estimator=xgb.XGBClassifier(
                    learning_rate=0.1,
                    n_estimators=300,
                    max_depth=5,
                    min_child_weight=3,
                    gamma=0.3,
                    subsample=0.8,
                    colsample_bytree=0.8,
                    objective='binary:logistic',
                    nthread=4,
                    seed=27),
            param_grid=param_test7,
            scoring='roc_auc',
            iid=False, cv=5)
    gsearch7.fit(x_train, y_train)
    print gsearch7.cv_results_, gsearch7.best_params_, gsearch7.best_score_

#param_test7()

def param_test8():
    param_test8 = {
     'reg_lambda':[0, 1e-5, 1e-2, 0.1, 1, 100]
    }
    gsearch8 = GridSearchCV(
            estimator=xgb.XGBClassifier(
                    learning_rate=0.1,
                    reg_alpha=1e-5,
                    n_estimators=300,
                    max_depth=5,
                    min_child_weight=3,
                    gamma=0.3,
                    subsample=0.8,
                    colsample_bytree=0.8,
                    objective='binary:logistic',
                    nthread=4,
                    seed=27),
            param_grid=param_test8,
            scoring='roc_auc',
            iid=False, cv=5)
    gsearch8.fit(x_train, y_train)
    print gsearch8.cv_results_, gsearch8.best_params_, gsearch8.best_score_

#param_test8()

def PlotRoc(Algorithm, PR, TR):
    roc_auc = auc(PR, TR)
    plt.title("ROC curve of %s (AUC = %.4f)" % (Algorithm, roc_auc))
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.ylim(0.0, 1.0)
    plt.xlim(0.0, 1.0)
    plt.plot(PR, TR)
    plt.show()

#最后，降低学习率，增加子估计器的数量
def param_test9():
    xlf = xgb.XGBClassifier(
            learning_rate=0.025,
            n_estimators=1200,
            reg_alpha=1e-5,
            reg_lambda=0.01,
            max_depth=5,
            min_child_weight=3,
            gamma=0.3,
            subsample=0.8,
            colsample_bytree=0.8,
            objective='binary:logistic',
            nthread=4,
            seed=27)
    xlf.fit(x_train, y_train)
    y_predprob = xlf.predict_proba(x_test)[:, 1]
    print "AUC Score (Train): %f" % metrics.roc_auc_score(y_test, y_predprob)

param_test9()

