#-*-coding:utf8-*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def read_data(path):
    """
    :param path: 文件路径，读取数据文件要带有列名
    :return: DataFrame格式的数据集
    """
    import pandas as pd
    data = pd.read_csv(path, sep='	', header=0)
    return data

def getFeature(data, column_name):
    """
    计算特征
    :param data: DataFrame格式的数据集；column_name：需要增加的列名称列表
    :return: data: DataFrame格式的数据集，在原来的数据集上增加列
    """
    import GetFeature
    #Feature的格式为[{},{},...],每个字典里面放的是每个index对应增加列的特征值
    Feature = GetFeature.getF(data)
    #columns的格式是[[],[],...],每个子列表都将存放一个增加的列的数据
    columns = [[] for i in xrange(0, len(Feature))]
    #给每一列赋值
    for index in data.index:
        for j in xrange(0, len(Feature)):
            columns[j].append(Feature[j].get(index))
    #给增加列赋予列名称
    for k, name in zip(xrange(0, len(columns)), column_name):
        data[name] = columns[k]
    return data

def get_train_test(data, x_name, y_name, type='sample2'):
    """
    原始数据分割
    :param data: DataFrame格式的数据集；type：数据分割的方式；x_name，y_name用来选择训练集和测试集的列名称
    :return: 训练集和测试集
    """
    if type == 'sample1':
        train = data.sample(int(len(data)*0.7))
        test = data.sample(int(len(data)*0.3))
    elif type == 'sample2':
        train = data[0:int(len(data)*0.7)]
        test = data[int(len(data)*0.7):len(data)]

    train_x = train[x_name].values
    test_x = test[x_name].values
    train_y = train[y_name].values
    test_y = test[y_name].values

    return train_x, test_x, train_y, test_y

def DataFrame_array(data):
    """
    DataFrmae格式直接获得的维数不对，预测变量的维数转换
    :param data: 预测变量数据
    :return: 转换后的预测变量数据
    """
    narry_data = []
    for row in data:
        narry_data.append(row[0])

    return  narry_data

