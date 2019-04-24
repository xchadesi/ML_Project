#-*-coding:utf8-*-
"""
定义各种类型的参数
"""
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def getTrainDim(path):
    fil = open(path, 'r')
    line = fil.readline()
    parameters = line.split('*')
    must_pars = parameters[0].split(',')
    filePath = must_pars[0]
    y_name = must_pars[1]
    data_ratio = float(must_pars[2])
    select_method= must_pars[3]
    max_dims = int(must_pars[4])
    min_dims = int(must_pars[5])
    int_dims = int(must_pars[6])
    Algorithm = []
    for i in xrange(1, len(parameters)):
        pars = parameters[i].split('#')
        Algorithm.append(pars[0])
    #print filePath, y_name, select_method, max_dims, min_dims, int_dims, data_ratio, Algorithm
    return filePath, y_name, select_method, max_dims, min_dims, int_dims, data_ratio, Algorithm

def getTrainAlgorithm(path):
    fil = open(path, 'r')
    line = fil.readline()
    parameters = line.split('*')
    must_pars = parameters[0].split(',')
    filePath = must_pars[0]
    y_name = must_pars[1]
    data_ratio = float(must_pars[2])
    select_method= must_pars[3]
    dims = int(must_pars[4])
    Algorithm = []
    for i in xrange(1, len(parameters)):
        pars = parameters[i].split('#')
        Algorithm.append(pars[0])
    #print filePath, y_name, select_method, dims, data_ratio, Algorithm
    return filePath, y_name, select_method, dims, data_ratio, Algorithm


def getParameters(path, classifier):
    fil = open(path, 'r')
    line = fil.readline()
    #print line
    parameters = line.split('*')
    must_pars = parameters[0].split(',')
    par = {}

    for i in xrange(1, len(parameters)):
        #print parameters[i]
        pars = parameters[i].split('#')
        par[pars[0]] = {}
        for j in xrange(1, len(pars)-1):
            p = pars[j].split(',')
            par[pars[0]][p[0]] = []
            for x in p[1:]:
                #是否有小数点
                if '.' in x or 'e-' in x:
                    par[pars[0]][p[0]].append(float(x))
                #是否是没有填写，使用默认
                elif x == '':
                    del(par[pars[0]][p[0]])
                #有些参数必须是整数
                elif x.isdigit():
                    par[pars[0]][p[0]].append(int(x))
                else:
                    par[pars[0]][p[0]].append(x)

    #print par
    return par[classifier]

#getTrainDim()