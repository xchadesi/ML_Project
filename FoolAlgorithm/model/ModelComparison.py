#-*-coding:utf8-*-

"""
常用算法的调用对比(评估参数、ROC曲线)
"""

import time
from sklearn import metrics
import Model
from sklearn.pipeline import make_pipeline
from scipy import interp
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import roc_curve, auc

def ClassifierComparison(classifier, best_parameters, deal_name_steps, train_x, train_y, test_x, test_y):

    #设置需要比较的算法类型
    classifiers = Model.getClassifiers()
    filter = None
    for step_name, method in deal_name_steps.items():
        if method is not None:
            #做降维处理
            filter = Model.getFeature(best_parameters['dim_n_components'], method)
        else:
            pass

    print('******************* %s ********************' % classifier)
    start_time = time.time()
    #调用模型
    clf = classifiers[classifier](best_parameters)
    if filter != None:
        model = make_pipeline(filter, clf)
    else:
        model = clf
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

def GetResult(classifier, best_parameters, deal_name_steps, x_name, y_name):

    #设置需要比较的算法类型
    classifiers = Model.getClassifiers()
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
            pass

    print('******************* %s ********************' % classifier)
    #调用模型
    clf = classifiers[classifier](best_parameters)
    if filter2 != None:
        model = make_pipeline(filter1, filter2, clf)
    else:
        model = make_pipeline(filter1, clf)

    path1 = 'train'
    path2 = 'public'

    import DealData
    #训练数据
    data = DealData.read_data(path1)

    train_x, test_no_xuse, train_y, test_no_yuse = DealData.get_train_test(data, x_name, y_name, type='sample2')

    #测试数据
    test = DealData.read_data(path2)
    test_x = test[x_name]

    #利用选用的模型进行训练和预测
    model.fit(train_x, train_y)
    predict = model.predict(test_x)
    proba = model.predict_proba(test_x)

    #处理训练结果
    EID = test['EID']
    from pandas import DataFrame
    d = DataFrame(test_x)
    d['EID'] = EID
    d['FORTARGET'] = predict
    d['PROB'] = [round(i, 4) for i in proba[:, 1]]
    result = d[['EID', 'FORTARGET', 'PROB']]
    result.to_csv('evaluation_public', encoding='utf-8')
    print '获取结果完毕！'




