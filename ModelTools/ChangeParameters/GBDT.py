#-*-coding:utf8-*-
import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import GridSearchCV
from sklearn import metrics
from pandas import DataFrame
from sklearn.metrics import roc_curve
reload(sys)
sys.setdefaultencoding('utf-8')


train = pd.read_csv("train")
public = pd.read_csv("public")
train_x = train[[x for x in train.columns if x != 'TARGET']]
train_y = train['TARGET']

# 切分为测试集和训练集，比例0.3
X_train, X_test, y_train, y_test = train_test_split(train_x, train_y, test_size=0.3)

def param_test1():
    param_test1 = {
     'n_estimators': range(100, 1800, 200),
    }
    gsearch1 = GridSearchCV(
            estimator=GradientBoostingClassifier(
                    learning_rate=0.1,
                    min_samples_split=300,
                    min_samples_leaf=20,
                    max_depth=8,
                    max_features='sqrt',
                    subsample=0.8,
                    random_state=10),
            param_grid=param_test1,
            scoring='roc_auc',
            iid=False,
            cv=5)
    gsearch1.fit(X_train, y_train)
    print gsearch1.cv_results_, gsearch1.best_params_, gsearch1.best_score_

#param_test1()

def param_test2():
    param_test2 = {
     'max_depth': range(3, 14, 2),
     'min_samples_split': range(100, 801, 200)
    }
    gsearch2 = GridSearchCV(
            estimator=GradientBoostingClassifier(
                    learning_rate=0.1,
                    n_estimators=300,
                    min_samples_leaf=20,
                    max_features='sqrt',
                    subsample=0.8,
                    random_state=10),
            param_grid=param_test2,
            scoring='roc_auc',
            iid=False,
            cv=5)
    gsearch2.fit(X_train, y_train)
    print gsearch2.cv_results_, gsearch2.best_params_, gsearch2.best_score_

#param_test2()

def param_test3():
    param_test3 = {
     'min_samples_leaf': range(60, 101, 10),
     'min_samples_split': range(100, 801, 200)
    }
    gsearch3 = GridSearchCV(
            estimator=GradientBoostingClassifier(
                    learning_rate=0.1,
                    n_estimators=300,
                    max_depth=7,
                    max_features='sqrt',
                    subsample=0.8,
                    random_state=10),
            param_grid=param_test3,
            scoring='roc_auc',
            iid=False,
            cv=5)
    gsearch3.fit(X_train, y_train)
    print gsearch3.cv_results_, gsearch3.best_params_, gsearch3.best_score_

#param_test3()

def param_test4():
    param_test4 = {
     'max_features': range(7, 20, 2)
    }
    gsearch4 = GridSearchCV(
            estimator=GradientBoostingClassifier(
                    learning_rate=0.1,
                    n_estimators=300,
                    max_depth=7,
                    min_samples_leaf=70,
                    min_samples_split=700,
                    subsample=0.8,
                    random_state=10),
            param_grid=param_test4,
            scoring='roc_auc',
            iid=False,
            cv=5)
    gsearch4.fit(X_train, y_train)
    print gsearch4.cv_results_, gsearch4.best_params_, gsearch4.best_score_

#param_test4()

def param_test5():
    param_test5 = {
    'subsample':[0.6, 0.7, 0.75, 0.8, 0.85, 0.9]
    }
    gsearch5 = GridSearchCV(
            estimator=GradientBoostingClassifier(
                    learning_rate=0.1,
                    n_estimators=300,
                    max_depth=8,
                    min_samples_leaf=70,
                    min_samples_split=700,
                    max_features=11,
                    random_state=10),
            param_grid=param_test5,
            scoring='roc_auc',
            iid=False,
            cv=5)
    gsearch5.fit(X_train, y_train)
    print gsearch5.cv_results_, gsearch5.best_params_, gsearch5.best_score_

#param_test5()

def param_test6():
    gbc = GradientBoostingClassifier(
                    learning_rate=0.05,
                    n_estimators=600,
                    max_depth=8,
                    min_samples_leaf=70,
                    min_samples_split=700,
                    max_features=11,
                    subsample=0.9,
                    random_state=10)
    gbc.fit(X_train, y_train)
    y_pred = gbc.predict(X_test)
    y_predprob = gbc.predict_proba(X_test)[:, 1]
    print "Accuracy : %.4g" % metrics.accuracy_score(y_test, y_pred)
    print "AUC Score (Train): %f" % metrics.roc_auc_score(y_test, y_predprob)

#param_test6()

def param_test7():
    gbc = GradientBoostingClassifier(
                    learning_rate=0.01,
                    n_estimators=3000,
                    max_depth=8,
                    min_samples_leaf=70,
                    min_samples_split=700,
                    max_features=11,
                    subsample=0.9,
                    random_state=10)
    gbc.fit(X_train, y_train)
    y_pred = gbc.predict(X_test)
    y_predprob = gbc.predict_proba(X_test)[:, 1]
    print "Accuracy : %.4g" % metrics.accuracy_score(y_test, y_pred)
    print "AUC Score (Train): %f" % metrics.roc_auc_score(y_test, y_predprob)

#param_test7()

def param_test8():
    gbc = GradientBoostingClassifier(
                    learning_rate=0.025,
                    n_estimators=1200,
                    max_depth=8,
                    min_samples_leaf=70,
                    min_samples_split=700,
                    max_features=11,
                    subsample=0.9,
                    random_state=10)
    gbc.fit(X_train, y_train)
    y_pred = gbc.predict(X_test)
    y_predprob = gbc.predict_proba(X_test)[:, 1]
    print "Accuracy : %.4g" % metrics.accuracy_score(y_test, y_pred)
    print "AUC Score (Train): %f" % metrics.roc_auc_score(y_test, y_predprob)

#param_test8()

def param_test9():
    gbc = GradientBoostingClassifier(
                    learning_rate=0.01,
                    n_estimators=2000,
                    max_depth=8,
                    min_samples_leaf=70,
                    min_samples_split=700,
                    max_features=11,
                    subsample=0.9,
                    random_state=10)
    gbc.fit(X_train, y_train)
    y_pred = gbc.predict(X_test)
    y_predprob = gbc.predict_proba(X_test)[:, 1]
    print "Accuracy : %.4g" % metrics.accuracy_score(y_test, y_pred)
    print "AUC Score (Train): %f" % metrics.roc_auc_score(y_test, y_predprob)

#param_test9()

def param_test10():
    gbc = GradientBoostingClassifier(
                    learning_rate=0.01,
                    n_estimators=1600,
                    max_depth=8,
                    min_samples_leaf=70,
                    min_samples_split=700,
                    max_features=11,
                    subsample=0.9,
                    random_state=10)
    gbc.fit(X_train, y_train)
    y_pred = gbc.predict(X_test)
    y_predprob = gbc.predict_proba(X_test)[:, 1]
    print "Accuracy : %.4g" % metrics.accuracy_score(y_test, y_pred)
    print "AUC Score (Train): %f" % metrics.roc_auc_score(y_test, y_predprob)

#param_test10()

def param_test11():
    gbc = GradientBoostingClassifier(
                    learning_rate=0.01,
                    n_estimators=1300,
                    max_depth=8,
                    min_samples_leaf=70,
                    min_samples_split=700,
                    max_features=11,
                    subsample=0.9,
                    random_state=10)
    gbc.fit(X_train, y_train)
    y_pred = gbc.predict(X_test)
    y_predprob = gbc.predict_proba(X_test)[:, 1]
    print "Accuracy : %.4g" % metrics.accuracy_score(y_test, y_pred)
    print "AUC Score (Train): %f" % metrics.roc_auc_score(y_test, y_predprob)

#param_test11()

def param_test12():
    gbc = GradientBoostingClassifier(
                    learning_rate=0.025,
                    n_estimators=1400,
                    max_depth=8,
                    min_samples_leaf=70,
                    min_samples_split=700,
                    max_features=11,
                    subsample=0.9,
                    random_state=10)
    gbc.fit(X_train, y_train)
    y_pred = gbc.predict(X_test)
    y_predprob = gbc.predict_proba(X_test)[:, 1]
    print "Accuracy : %.4g" % metrics.accuracy_score(y_test, y_pred)
    print "AUC Score (Train): %f" % metrics.roc_auc_score(y_test, y_predprob)

#param_test12()

def param_test13():
    gbc = GradientBoostingClassifier(
                    learning_rate=0.025,
                    n_estimators=2000,
                    max_depth=8,
                    min_samples_leaf=70,
                    min_samples_split=700,
                    max_features=11,
                    subsample=0.9,
                    random_state=10)
    gbc.fit(X_train, y_train)
    y_pred = gbc.predict(X_test)
    y_predprob = gbc.predict_proba(X_test)[:, 1]
    print "Accuracy : %.4g" % metrics.accuracy_score(y_test, y_pred)
    print "AUC Score (Train): %f" % metrics.roc_auc_score(y_test, y_predprob)

param_test13()

# y_pred_grd_lm = grd_lm.predict_proba(grd.apply(X_test)[:, :, 0])[:, 1]
# # 根据预测结果输出
# fpr_grd_lm, tpr_grd_lm, _ = roc_curve(y_test, y_pred_grd_lm)
# print fpr_grd_lm, tpr_grd_lm

def PlotRoc(Algorithm, PR, TR):
    import matplotlib.pyplot as plt
    from sklearn.metrics import auc
    roc_auc = auc(PR, TR)
    plt.title("ROC curve of %s (AUC = %.4f)" % (Algorithm, roc_auc))
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.ylim(0.0, 1.0)
    plt.xlim(0.0, 1.0)
    plt.plot(PR, TR)
    plt.show()


#PlotRoc('GBDT+LR', fpr_grd_lm, tpr_grd_lm)

def GetResult(model, public):

    #利用选用的模型进行训练和预测
    predict = model.predict(public)
    proba = model.predict_proba(public)

    #处理训练结果
    EID = public['EID']
    print len(public)
    print len(proba)
    print len(predict)
    d = DataFrame(public)
    d['EID'] = EID
    d['FORTARGET'] = predict
    d['PROB'] = [round(i, 4) for i in proba[:, 1]]
    result = d[['EID', 'FORTARGET', 'PROB']]
    result.to_csv('evaluation_public', encoding='utf-8')

def param_test():
    gbc = GradientBoostingClassifier(
                    learning_rate=0.01,
                    n_estimators=2000,
                    max_depth=8,
                    min_samples_leaf=70,
                    min_samples_split=700,
                    max_features=11,
                    random_state=10)
    gbc.fit(X_train, y_train)
    y_pred = gbc.predict(X_test)
    y_predprob = gbc.predict_proba(X_test)[:, 1]
    print "Accuracy : %.4g" % metrics.accuracy_score(y_test, y_pred)
    print "AUC Score (Train): %f" % metrics.roc_auc_score(y_test, y_predprob)
    GetResult(gbc, public)

#param_test()
