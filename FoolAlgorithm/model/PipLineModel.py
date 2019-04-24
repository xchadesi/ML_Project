#-*-coding:utf8-*-

"""
通过流水线的方式构建模型
"""
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
import Model
import SetParameters

#整体数据预处理步骤
def Deal_Feature(deal_steps):
    step = []
    for step_name, index in deal_steps.items():
        if index[0] is not None:
            #新建降维的对象
            step1 = ('reduce_dim', index[0])
            step.append(step1)
    return step

#搜索最好的参数训练模型
def search_best_parameter(pipeline, param_grid, train_x, train_y):
    grid_search = GridSearchCV(pipeline, param_grid, cv=5, scoring='roc_auc')
    grid_search.fit(train_x, train_y)
    best_parameters = grid_search.best_estimator_.get_params()
    #print DataFrame(grid_search.cv_results_)
    return best_parameters, grid_search

#构建Pipeline
def build_pipline(par_th, re_path, train_x, train_y, test_classifiers, deal_steps):
    #为待训练的模型作为流水线的最后一步
    classifiers = Model.getClassifiers()
    #存放参数
    model_best_parameters = {}
    line = ''
    #fil = open("E:\\workplace\\.metadata\\.me_tcat85\\webapps\\FoolAlgorithm\\AlgorithmUpload\\AlgorithmResult.txt", 'w')
    fil = open(re_path, 'w')
    for classifier in test_classifiers:
        clf = classifiers[classifier]()
        step2 = ('Model', clf)
        step = Deal_Feature(deal_steps)
        step.append(step2)
        pipeline = Pipeline(steps=step)
        #搜索最好的模型训练参数
        #path = "E:\\workplace\\.metadata\\.me_tcat85\\webapps\\FoolAlgorithm\\AlgorithmUpload\\AlgorithmParameter.txt"
        param_grid = SetParameters.getParameters(par_th, classifier)
        #print classifier, param_grid
        #print 'Start train!'
        best_parameters, grid_search= search_best_parameter(pipeline, param_grid, train_x, train_y)
        model_best_parameters[classifier] = best_parameters
        print grid_search.best_params_, grid_search.best_score_

        #保存最优搜索结果
        for key, value in (grid_search.best_params_).items():
            line = line + key + ',' + str(value) + '*'
        line = line + classifier + ',' + str(grid_search.best_score_) + '#'
    fil.write(line)
    fil.close()

    return model_best_parameters

#构建Pipeline
def build_pipline_dim(par_path, train_x, train_y, test_classifiers, deal_steps):
    #为待训练的模型作为流水线的最后一步
    classifiers = Model.getClassifiers()
    classifier = test_classifiers[0]
    clf = classifiers[classifier]()
    step2 = ('Model', clf)
    step = Deal_Feature(deal_steps)
    step.append(step2)
    pipeline = Pipeline(steps=step)
    #搜索最好的模型训练参数
    #path = "E:\\workplace\\.metadata\\.me_tcat85\\webapps\\FoolAlgorithm\\DimUpload\\DimParameter.txt"
    param_grid = SetParameters.getParameters(par_path, classifier)
    #print classifier, param_grid
    #print '开始训练'
    best_parameters, grid_search= search_best_parameter(pipeline, param_grid, train_x, train_y)
    print grid_search.best_params_, grid_search.best_score_
    return classifier, best_parameters, grid_search.best_score_