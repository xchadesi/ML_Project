#-*-coding:utf8-*-

"""
常用算法的调用对比(评估参数、ROC曲线)
"""

import time
from sklearn import metrics
import pickle as pickle
import Model
from sklearn.pipeline import make_pipeline
import Parameters
from scipy import interp
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import roc_curve, auc

def ClassifierComparison(classifier, best_parameters, deal_name_steps, save_path, train_x, train_y, test_x, test_y):

    #设置模型的保存地址
    model_save_file = save_path+classifier

    #设置需要比较的算法类型
    classifiers = Parameters.getClassifiers()
    filter1, filter2 = None, None
    for step_name, method in deal_name_steps.items():
        if step_name == 'Imputer':
            #缺失值处理
            train_x = Model.changeFeature(train_x, method)
            test_x = Model.changeFeature(test_x, method)
        elif step_name == 'MinMaxScaler':
            #数据无量纲处理
            train_x = Model.changeFeature(train_x, method)
            test_x = Model.changeFeature(test_x, method)
        elif step_name == 'SelectKBest' :
            #做特征选择
            filter1 = Model.getFeature(best_parameters['SelectKBest__k'], method)
        elif step_name == 'reduce_dim':
            #做降维处理
            filter2 = Model.getFeature(best_parameters['reduce_dim__n_components'], method)
        else:
            print '您输入的数据预处理参数有误！'

    print('******************* %s ********************' % classifier)
    start_time = time.time()
    #调用模型
    clf = classifiers[classifier](best_parameters)
    if filter2 != None:
        model = make_pipeline(filter1, filter2, clf)
    else:
        model = make_pipeline(filter1, clf)
    model.fit(train_x, train_y)
    print('training took %fs!' % (time.time() - start_time))
    #预测
    predict = model.predict(test_x)
    #模型评估参数
    precision = metrics.precision_score(test_y, predict)
    recall = metrics.recall_score(test_y, predict)
    print('precision: %.2f%%, recall: %.2f%%' % (100 * precision, 100 * recall))
    accuracy = metrics.accuracy_score(test_y, predict)
    print('accuracy: %.2f%%' % (100 * accuracy))

    #画ROC曲线，并求AUC值
    proba = model.predict_proba(test_x)
    fpr, tpr, thresholds = roc_curve(test_y, proba[:, 1])
    mean_tpr = 0.0
    mean_fpr = np.linspace(0, 1, 500)
    #对mean_tpr在mean_fpr处进行插值
    mean_tpr += interp(mean_fpr, fpr, tpr)
    mean_tpr[0] = 0.0
    roc_auc = auc(fpr, tpr)
    plt.plot(fpr, tpr)
    plt.title("ROC curve of %s (AUC = %.4f)" % (classifier, roc_auc))
    plt.show()

    if model_save_file != None:
        pickle.dump(model, open(model_save_file, 'a'))

def ClusteringComparison(classifier, best_parameters, deal_name_steps, save_path, test_x):

    #设置模型的保存地址
    model_save_file = save_path+classifier

    #设置需要比较的算法类型
    classifiers = Parameters.getClassifiers()
    filter1, filter2 = None, None
    for step_name, method in deal_name_steps.items():
        if step_name == 'Imputer':
            #缺失值处理
            test_x = Model.changeFeature(test_x, method)
        elif step_name == 'MinMaxScaler':
            #数据无量纲处理
            test_x = Model.changeFeature(test_x, method)
        elif step_name == 'SelectKBest':
            #做特征选择
            filter1 = Model.getFeature(best_parameters['SelectKBest__k'], method)
        elif step_name == 'reduce_dim':
            #做降维处理
            filter2 = Model.getFeature(best_parameters['reduce_dim__n_components'], method)
        else:
            print '您输入的数据预处理参数有误！'

    print('******************* %s ********************' % classifier)
    start_time = time.time()

    k_scores1 = []
    k_scores2 = []
    for k in best_parameters['Model__n_clusters']:
        #调用模型
        clf = classifiers[classifier](k, best_parameters)
        if filter2 != None:
            model = make_pipeline(filter1, filter2)
        else:
            model = make_pipeline(filter1)
        print('training took %fs!' % (time.time() - start_time))
        #预测
        #test_x = model.fit_transform(test_x)
        predict = clf.fit_predict(test_x)
        #模型评估参数
        precision1 = metrics.calinski_harabaz_score(test_x, predict)
        precision2 = metrics.silhouette_score(test_x, predict)
        print "聚类数据%s" % k
        print "外部数据协方差%s" % precision1
        print "内部数据协方差%s" % precision2
        k_scores1.append(precision1)
        k_scores2.append(precision2)

    plt.subplot(2, 1, 1)
    plt.plot(k_scores1)
    plt.subplot(2, 1, 2)
    plt.plot(k_scores2)
    plt.show()

    if model_save_file != None:
        pickle.dump(model, open(model_save_file, 'a'))





