#-*-coding:utf8-*-

import sys
import DealData
import PipLineModel
import Model
import SetParameters
reload(sys)
sys.setdefaultencoding('utf-8')

def Myclassifier():
    #读取文件的路径、设置作为预测变量的列名、降维方法、最大维数、最小维数、维数间隔、作为预测变量分割数据比例、算法类型
    #par_path = "E:\\workplace\\.metadata\\.me_tcat85\\webapps\\FoolAlgorithm\\DimUpload\\DimParameter.txt"
    par_path1 = sys.argv[1]
    par_path2 = sys.argv[2]
    par_path = par_path1 + par_path2+".txt"
    re_path = par_path1.replace('Par_', 'Re_')+par_path2 + ".txt"
    path, y_name, select_method, max_dims, min_dims, int_dims, data_ratio, test_classifiers = SetParameters.getTrainDim(par_path)
    data = DealData.read_data(path)
    train_x, test_x, train_y, test_y = DealData.get_train_test(data, y_name, data_ratio)
    line = ''
    for dim in xrange(min_dims, max_dims,int_dims):
        print dim, select_method
        SelectKBest = Model.getFeature(dim, select_method)
        deal_steps = {'reduce_dim': [SelectKBest]}
        #构建Pipeline, 搜索最优的参数
        classifier, best_parameters, auc = PipLineModel.build_pipline_dim(par_path, train_x, train_y, test_classifiers, deal_steps)
        line = line + str(dim) + ',' + str(auc) + '#'
    fil = open(re_path, 'w')
    print line
    fil.write(line)
    fil.close()

if __name__ == '__main__':
    Myclassifier()