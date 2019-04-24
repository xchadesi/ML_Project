#-*-coding:utf8-*-

import sys
import DealData
import PipLineModel
import Model
import SetParameters
reload(sys)
sys.setdefaultencoding('utf-8')


#读取文件的路径、设置作为预测变量的列名、降维方法、作为预测变量分割数据比例、需要比较的算法类型
#par_path = "E:\\workplace\\.metadata\\.me_tcat85\\webapps\\FoolAlgorithm\\AlgorithmUpload\\AlgorithmParameter.txt"
par_path1 = sys.argv[1]
par_path2 = sys.argv[2]
par_th = par_path1 + par_path2 + ".txt"
re_path = par_path1.replace('Par_', 'Re_')+par_path2 + ".txt"
#print par_th
#print re_path
path, y_name, select_method, dims, data_ratio, test_classifiers = SetParameters.getTrainAlgorithm(par_th)
if select_method != 'No':
    #print dims, select_method
    SelectKBest = Model.getFeature(dims, select_method)
    deal_steps = {'reduce_dim': [SelectKBest]}
else:
    deal_steps = {'reduce_dim': None}

def Myclassifier():
    data = DealData.read_data(path)
    train_x, test_x, train_y, test_y = DealData.get_train_test(data, y_name, data_ratio)

    #构建Pipeline, 搜索最优的参数
    #print '开始搜索'
    PipLineModel.build_pipline(par_th, re_path, train_x, train_y, test_classifiers, deal_steps)

if __name__ == '__main__':
    Myclassifier()