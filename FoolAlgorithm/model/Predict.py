#-*-coding:utf8-*-

import sys
import DealData
import PipLineModel
from sklearn.pipeline import make_pipeline
import Model
import SetParameters
from pandas import DataFrame
reload(sys)
sys.setdefaultencoding('utf-8')

def Myclassifier():
    #读取文件的路径、设置作为预测变量的列名、降维方法、维数、作为预测变量分割数据比例、算法类型
    #par_th = "E:\\workplace\\.metadata\\.me_tcat85\\webapps\\FoolAlgorithm\\PredictUpload\\PredictParameter.txt"
    par_path1 = sys.argv[1]
    par_path2 = sys.argv[2]
    predictPath = sys.argv[3]
    par_path = par_path1 + par_path2+".txt"
    re_path = par_path1.replace('Par_', 'Re_')+par_path2 + ".csv"
    path, y_name, select_method, dims, data_ratio, test_classifiers = SetParameters.getTrainAlgorithm(par_path)
    data = DealData.read_data(path)
    train_x, test_x, train_y, test_y = DealData.get_train_test(data, y_name, data_ratio)
    print dims, select_method
    SelectKBest = Model.getFeature(dims, select_method)
    deal_steps = {'reduce_dim': [SelectKBest]}
    #构建Pipeline, 搜索最优的参数
    print test_classifiers
    classifier, best_parameters, auc = PipLineModel.build_pipline_dim(par_path, train_x, train_y, test_classifiers, deal_steps)
    classifiers = Model.getClassifiers()
    filter = None
    if select_method is not None:
        #做降维处理
        filter = Model.getFeature(dims, select_method)
    else:
        pass
    clf = classifiers[classifier](best_parameters)
    if filter != None:
        model = make_pipeline(filter, clf)
    else:
        model = clf
    model.fit(train_x, train_y)
    #做预测
    #predictPath = "E:\\workplace\\.metadata\\.me_tcat85\\webapps\\FoolAlgorithm\\PredictUpload\\public"
    x_name = [x for x in data.columns if x != y_name]
    #获取预测数据
    test = DealData.read_data(predictPath)
    test_x = test[x_name]

    #利用选用的模型进行训练和预测
    predict = model.predict(test_x)
    proba = model.predict_proba(test_x)

    #处理训练结果
    result = DataFrame(test_x)
    result['FORTARGET'] = predict
    result['PROB'] = [round(i, 4) for i in proba[:, 1]]
    result.to_csv(re_path, encoding='utf-8')


if __name__ == '__main__':
    Myclassifier()