#-*-coding:utf8-*-

"""
通过流水线的方式构建模型
"""

#整体数据预处理步骤
def Deal_Feature(deal_steps):
    from sklearn.preprocessing import Imputer
    from sklearn.preprocessing import MinMaxScaler
    step = []
    for step_name, index in deal_steps.items():
        if step_name == 'Imputer':
            #新建计算缺失值的对象
            step1 = ('Imputer', Imputer())
            step.append(step1)
        elif step_name == 'MinMaxScaler':
            #新建无量纲化对象
            step3 = ('MinMaxScaler', MinMaxScaler())
            step.append(step3)
        elif step_name == 'SelectKBest':
            #新建卡方校验选择特征的对象
            step4 = ('SelectKBest', index[0])
            step.append(step4)
        elif step_name == 'reduce_dim':
            #新建PCA降维的对象
            step5 = ('reduce_dim', index[0])
            step.append(step5)
    return step


#搜索最好的参数训练模型
def search_best_parameter(pipeline, param_grid, train_x, train_y):
    from sklearn.model_selection import GridSearchCV
    grid_search = GridSearchCV(pipeline, param_grid, cv=5, scoring='accuracy')
    grid_search.fit(train_x, train_y)
    best_parameters = grid_search.best_estimator_.get_params()
    return best_parameters

#构建Pipeline
def build_pipline(train_x, train_y, test_classifiers, deal_steps):
    from sklearn.pipeline import Pipeline
    import Parameters
    #新建逻辑回归的对象，其为待训练的模型作为流水线的最后一步
    classifiers = Parameters.getClassifiers()
    #存放参数
    model_best_parameters = {}
    for classifier in test_classifiers:
        clf = classifiers[classifier]()
        step6 = ('Model', clf)
        step = Deal_Feature(deal_steps)
        step.append(step6)
        pipeline = Pipeline(steps=step)
        #搜索最好的模型训练参数
        param_grid = Parameters.getParameters(classifier)
        #print classifier, param_grid
        print '开始训练'
        best_parameters = search_best_parameter(pipeline, param_grid, train_x, train_y)
        model_best_parameters[classifier] = best_parameters

    return model_best_parameters