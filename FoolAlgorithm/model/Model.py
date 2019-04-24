#-*-coding:utf8-*-
"""
数据变换、特征选择、算法函数的集合
"""
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#特征选择
def getFeature(n, method):
    from sklearn.feature_selection import SelectKBest
    if method == 'chi2':
        from sklearn.feature_selection import chi2
        filter = SelectKBest(chi2, k=n)

    elif method == 'VarianceThreshold':
        #参数threshold为方差的阈值
        from sklearn.feature_selection import VarianceThreshold
        filter = VarianceThreshold(threshold=n)

    elif method == 'pearsonr':
        from scipy.stats import pearsonr
        import array
        #第一个参数为计算评估特征是否好的函数，该函数输入特征矩阵和目标向量，输出二元组（评分，P值）的数组，数组第i项为第i个特征的评分和P值
        filter = SelectKBest(lambda X, Y: array(map(lambda x:pearsonr(x, Y), X.T)).T, k=n)

    elif method == 'PCA':
        from sklearn.decomposition import PCA
        filter = PCA(n_components=n)

    elif method == 'LDA':
        from sklearn.lda import LDA
        filter = LDA(n_components=n)

    elif method == 'MINE':
        from minepy import MINE

        def mic(x, y):
            m = MINE()
            m.compute_score(x, y)
            return (m.mic(), 0.5)
        #由于MINE的设计不是函数式的，定义mic方法将其为函数式的，返回一个二元组，二元组的第2项设置成固定的P值0.5
        filter = SelectKBest(lambda X, Y: array(map(lambda x:mic(x, Y), X.T)).T, k=n)

    elif method == 'RFE':
        from sklearn.feature_selection import RFE
        from sklearn.linear_model import LogisticRegression
        filter = RFE(estimator=LogisticRegression(), n_features_to_select=2)

    elif method == 'LR':
        from sklearn.feature_selection import SelectFromModel
        from sklearn.linear_model import LogisticRegression
        #带L1惩罚项的逻辑回归作为基模型的特征选择
        SelectFromModel(LogisticRegression(penalty="l1", C=0.1))

    elif method == 'GBDT':
        from sklearn.feature_selection import SelectFromModel
        from sklearn.ensemble import GradientBoostingClassifier
        #GBDT作为基模型的特征选择
        SelectFromModel(GradientBoostingClassifier())
    else:
        print '您输入的特征选择参数有误！'

    return filter




#BernoulliRBM_classifier
def BernoulliRBM_classifier(best_parameters={}):
    from sklearn.neural_network import BernoulliRBM
    if len(best_parameters) > 0:
        model = BernoulliRBM(n_components=best_parameters['Model__n_components'], learning_rate=best_parameters['Model__learning_rate'],
                             batch_size=best_parameters['Model__batch_size'], n_iter=best_parameters['Model__n_iter'],
                             verbose=best_parameters['Model__verbose'], random_state=best_parameters['Model__random_state'])
    else:
        model = BernoulliRBM()
    return model

#MLPC_classifier
def MLPC_classifier(best_parameters={}):
    from sklearn.neural_network import MLPClassifier
    if len(best_parameters) > 0:
        model = MLPClassifier(solver=best_parameters['Model__solver'], alpha=best_parameters['Model__alpha'],
                              hidden_layer_sizes=best_parameters['Model__hidden_layer_sizes'], random_state=best_parameters['Model__random_state'])
    else:
        model = MLPClassifier()
    return model

# AdaBoost Classifier
def AdaBoost_classifier(best_parameters={}):
    from sklearn.ensemble import AdaBoostClassifier
    if len(best_parameters) > 0:
        model = AdaBoostClassifier(n_estimators=best_parameters['Model__n_estimators'])
    else:
        model = AdaBoostClassifier()
    return model

#Bagging Classifier
def Bagging_classifier(best_parameters={}):
    from sklearn.ensemble import BaggingClassifier
    from sklearn.neighbors import KNeighborsClassifier
    if len(best_parameters) > 0:
        model = BaggingClassifier(KNeighborsClassifier(), max_samples=best_parameters['Model__max_samples'], max_features=best_parameters['Model__max_features'])
    else:
        model = BaggingClassifier()
    return model

# MultinomialNB_classifier
def MultinomialNB_classifier(best_parameters={}):
    from sklearn.naive_bayes import MultinomialNB
    if len(best_parameters) > 0:
        model = MultinomialNB(alpha=best_parameters['Model__alpha'])
    else:
        model = MultinomialNB()
    return model

# GaussianNB  Classifier
def GaussianNB_classifier(best_parameters={}):
    from sklearn.naive_bayes import GaussianNB
    if len(best_parameters) > 0:
        model = GaussianNB(priors=best_parameters['Model__priors'])
    else:
        model = GaussianNB()
    return model

# BernoulliNB Classifier
def BernoulliNB_classifier(best_parameters={}):
    from sklearn.naive_bayes import BernoulliNB
    if len(best_parameters) > 0:
        model = BernoulliNB(alpha=best_parameters['Model__alpha'])
    else:
        model = BernoulliNB()
    return model

# KNN Classifier
def knn_classifier(best_parameters={}):
    from sklearn.neighbors import KNeighborsClassifier
    if len(best_parameters) > 0:
        model = KNeighborsClassifier(n_neighbors=best_parameters['Model__n_neighbors'])
    else:
        model = KNeighborsClassifier()
    return model

# Logistic Regression Classifier
def logistic_regression_classifier(best_parameters={}):
    from sklearn.linear_model import LogisticRegression
    if len(best_parameters) > 0:
        model = LogisticRegression(penalty=best_parameters['Model__penalty'], solver=best_parameters['Model__solver'])
    else:
        model = LogisticRegression()
    return model

# Random Forest Classifier
def random_forest_classifier(best_parameters={}):
    from sklearn.ensemble import RandomForestClassifier
    if len(best_parameters) > 0:
        model = RandomForestClassifier(n_estimators=best_parameters['Model__n_estimators'])
    else:
        model = RandomForestClassifier()
    return model

# Decision Tree Classifier
def decision_tree_classifier(best_parameters={}):
    from sklearn import tree
    if len(best_parameters) > 0:
        model = tree.DecisionTreeClassifier()
    else:
        model = tree.DecisionTreeClassifier()
    return model

# GBDT(Gradient Boosting Decision Tree) Classifier
def gradient_boosting_classifier(best_parameters={}):
    from sklearn.ensemble import GradientBoostingClassifier
    if len(best_parameters) > 0:
        model = GradientBoostingClassifier(learning_rate=best_parameters['Model__learning_rate'], n_estimators=best_parameters['Model__n_estimators'], max_depth=best_parameters['Model__max_depth'], min_samples_split=best_parameters['Model__min_samples_split'], min_samples_leaf=best_parameters['Model__min_samples_leaf'], max_features=best_parameters['Model__max_features'], subsample=best_parameters['Model__subsample'])
    else:
        model = GradientBoostingClassifier()
    return model

# SVM Classifier
def svm_classifier(best_parameters={}):
    from sklearn.svm import SVC
    if len(best_parameters) > 0:
        model = SVC(kernel=best_parameters['Model__kernel'], gamma=best_parameters['Model__gamma'],  C=best_parameters['Model__C'], probability=True)
    else:
        model = SVC()
    return model

#交叉验证，返回最好的参数
def cross_validation(model, param_grid, train_x, train_y):
    from sklearn.model_selection import GridSearchCV
    grid_search = GridSearchCV(model, param_grid, cv=5)
    grid_search.fit(train_x, train_y)
    best_parameters = grid_search.best_estimator_.get_params()
    return best_parameters

def getClassifiers():
    classifiers = {
        'MLPC': MLPC_classifier,
        'AdaBoost': AdaBoost_classifier,
        'LR': logistic_regression_classifier,
        'RF': random_forest_classifier,
        'SVM': svm_classifier,
        'GBDT': gradient_boosting_classifier,
        'Bagging': Bagging_classifier,
        'KNN': knn_classifier,
        'DT': decision_tree_classifier,
        'GNB': GaussianNB_classifier,
        'MNB': MultinomialNB_classifier,
        'BNB': BernoulliNB_classifier
    }
    return classifiers