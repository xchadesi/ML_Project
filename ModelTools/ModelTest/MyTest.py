#-*-coding:utf8-*-

import sys
import DealData
import PipLineModel
import ModelComparison
import Model
import Parameters

reload(sys)
sys.setdefaultencoding('utf-8')


def Myclassifier():
    #读取数据
    path = 'data.txt'
    data = DealData.read_data(path)

    #计算特征
    column_name = ['fwn']
    data = DealData.getFeature(data, column_name)

    #数据分割
    x_name = ['wb_profile', 'wb_follow', 'wb_fans', 'fwn']
    y_name = ['user_recon']
    train_x, test_x, train_y, test_y = DealData.get_train_test(data, x_name, y_name, type='sample2')

    #DataFrame数据格式转换
    train_y = DealData.DataFrame_array(train_y)
    test_y = DealData.DataFrame_array(test_y)

    #设置需要比较的算法类型
    test_classifiers = ['Bagging', 'AdaBoost', 'MLPC', 'GNB', 'BNB', 'KNN', 'LR', 'RF', 'DT', 'SVM', 'GBDT']
    #设置处理步骤
    select_method = 'chi2'
    reduce_method = 'PCA'
    K = 4
    N = 2
    SelectKBest = Model.getFeature(K, select_method)
    reduce_dim = Model.getFeature(N, reduce_method)
    deal_steps = {'Imputer': [], 'MinMaxScaler': [], 'SelectKBest': [SelectKBest], 'reduce_dim': [reduce_dim]}
    deal_name_steps = {'Imputer': 'Imputer', 'MinMaxScaler': 'MinMaxScaler', 'SelectKBest': select_method}

    #设置模型的保存地址
    save_path = 'F:\\Data\\test_data\\'

    #构建Pipeline
    model_best_parameters = PipLineModel.build_pipline(train_x, train_y, test_classifiers, deal_steps)
    for model, best_parameters in model_best_parameters.items():
        #print model, best_parameters
        #根据最优参数构建训练模型
        ModelComparison.ClassifierComparison(model, best_parameters, deal_name_steps, save_path, train_x, train_y, test_x, test_y)


def Myclustering():
    #读取数据
    path = 'data.txt'
    data = DealData.read_data(path)

    #计算特征
    column_name = ['fwn']
    data = DealData.getFeature(data, column_name)

    #数据分割
    x_name = ['wb_profile', 'wb_follow', 'wb_fans', 'fwn']
    test_x = data[x_name]
    #设置需要比较的算法类型
    test_classifiers = ['Birch']
    #设置处理步骤
    select_method = 'chi2'
    deal_name_steps = {'MinMaxScaler': 'MinMaxScaler', 'SelectKBest': select_method}

    #设置模型的保存地址
    save_path = 'F:\\Data\\test_data\\'

    #根据参数构建训练模型
    for classifier in test_classifiers:
        model_best_parameters = Parameters.getParameters(classifier)
        ModelComparison.ClusteringComparison(classifier, model_best_parameters, deal_name_steps, save_path, test_x)

if __name__ == '__main__':
    Myclustering()
