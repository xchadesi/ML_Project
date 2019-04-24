#-*-coding:utf8-*-
"""
定义各种类型的参数
"""
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def getParameters(classifier):

    param_svm = [{
        'SelectKBest__k': [4],
        'reduce_dim__n_components': [2, 3],
        'Model__gamma': [1e-3, 1e-4],
        'Model__kernel': ['rbf', 'linear'],
        'Model__C': [1, 10, 100, 1000]
    }]

    param_gnb = [{
            'SelectKBest__k': [4],
            'reduce_dim__n_components': [2, 3],
            'Model__priors': [None]
        }]

    param_bnb = [{
            'SelectKBest__k': [4],
            'reduce_dim__n_components': [2, 3],
            'Model__alpha': [0.1, 0.01, 0.001]
        }]

    param_mnb = [{
            'SelectKBest__k': [4],
            'reduce_dim__n_components': [2, 3],
            'Model__alpha': [0.1, 0.01, 0.001]
        }]

    param_knn = [{
            'SelectKBest__k': [4],
            'reduce_dim__n_components': [2, 3],
            'Model__n_neighbors': [3, 4]
        }]

    param_lr = [{
            'SelectKBest__k': [4],
            'reduce_dim__n_components': [2, 3],
            'Model__penalty': ['l2'],
            'Model__solver': ['liblinear', 'lbfgs', 'newton-cg', 'sag']

        }]

    param_rf = [{
            'SelectKBest__k': [4],
            'reduce_dim__n_components': [2, 3],
            'Model__n_estimators': [3, 4]
        }]

    param_gbdt = [{
            'SelectKBest__k': [4],
            'reduce_dim__n_components': [2, 3],
            'Model__n_estimators': [3, 4]
        }]

    param_dt = [{
            'SelectKBest__k': [4],
            'reduce_dim__n_components': [2, 3],
        }]

    param_mlpc = [{
            'SelectKBest__k': [4],
            'reduce_dim__n_components': [2, 3],
            'Model__solver': ['lbfgs'],
            'Model__alpha': [1e-5],
            'Model__hidden_layer_sizes': [(5, 2)],
            'Model__random_state': [1],
        }]

    param_adaboost = [{
            'SelectKBest__k': [4],
            'reduce_dim__n_components': [2, 3],
            'Model__n_estimators': [100]
        }]

    param_bagging = [{
            'SelectKBest__k': [4],
            'reduce_dim__n_components': [2, 3],
            'Model__max_samples': [0.5],
            'Model__max_features': [0.5],
        }]

    param_brbm = [{
            'SelectKBest__k': [4],
            'reduce_dim__n_components': [2, 3],
            'Model__n_components': [256],
            'Model__learning_rate': [0.1],
            'Model__batch_size': [10],
            'Model__n_iter': [10],
            'Model__verbose': [0],
            'Model__random_state': [1],
        }]

    param_kmeans = {
            'SelectKBest__k': 4,
            'reduce_dim__n_components': 2,
            'Model__init': 'k-means++',
            'Model__n_clusters': range(2, 20, 1),
            'Model__n_init': 10,
        }

    param_mbKMeans = {
            'SelectKBest__k': 4,
            'reduce_dim__n_components': 2,
            'Model__init': 'k-means++',
            'Model__n_clusters': range(2, 20, 1),
            'Model__n_init': 10,
            'Model__batch_size': 1000,
            'Model__verbose': 0,
            'Model__init_size': 1000
        }

    param_MeanShift = {
            'SelectKBest__k': 4,
            'reduce_dim__n_components': 2,
            'Model__bandwidth': None,
            'Model__seeds': None,
            'Model__bin_seeding': False,
            'Model__min_bin_freq': 1,
            'Model__cluster_all': True,
            'Model__n_jobs': 1
        }

    param_Spectral = {
            'SelectKBest__k': 4,
            'reduce_dim__n_components': 2,
            'Model__n_clusters': range(2, 20, 1),
            'Model__eigen_solver': None,
            'Model__random_state': None,
            'Model__n_init': 10,
            'Model__gamma': 1.0,
            'Model__affinity': 'rbf',
            'Model__n_neighbors': 10,
            'Model__eigen_tol': 0.0,
            'Model__assign_labels': 'kmeans',
            'Model__degree': 3,
            'Model__coef0': 1,
            'Model__kernel_params': None,
            'Model__n_jobs': 1
        }

    param_Birch = {
            'SelectKBest__k': 4,
            'reduce_dim__n_components': 2,
            'Model__threshold': 0.01,
            'Model__branching_factor': 50,
            'Model__n_clusters': range(2, 20, 1),
            'Model__compute_labels': True,
            'Model__copy': True
        }

    param_DBSCAN = {
            'SelectKBest__k': 4,
            'reduce_dim__n_components': 2,
            'Model__eps': 0.5,
            'Model__min_samples': 5,
            'Model__metric': 'euclidean',
            'Model__metric_params': None,
            'Model__algorithm': 'auto',
            'Model__leaf_size': 30,
            'Model__p': None,
            'Model__n_jobs': 1
        }

    param_AP = {
            'SelectKBest__k': 4,
            'reduce_dim__n_components': 2,
            'Model__S': None,
            'Model__preference': None,
            'Model__convergence_iter': 15,
            'Model__max_iter': 200,
            'Model__damping': 0.5,
            'Model__copy': True,
            'Model__verbose': False,
            'Model__return_n_iter': False
        }

    Parameters = {
            'MeanShift': param_MeanShift,
             'Spectral': param_Spectral,
                'Birch': param_Birch,
               'DBSCAN': param_DBSCAN,
                   'AP': param_AP,
             'mbKMeans': param_mbKMeans,
               'KMeans': param_kmeans,
                 'BRBM': param_brbm,
                 'MLPC': param_mlpc,
             'AdaBoost': param_adaboost,
              'Bagging': param_bagging,
                  'GNB': param_gnb,
                  'MNB': param_mnb,
                  'BNB': param_bnb,
                  'KNN': param_knn,
                   'LR': param_lr,
                   'RF': param_rf,
                   'DT': param_dt,
                  'SVM': param_svm,
                 'GBDT': param_gbdt}

    return Parameters[classifier]

def getClassifiers():
    import Model
    classifiers = {
        'MeanShift': Model.MeanShift_clustering,
        'Spectral': Model.Spectral_clustering,
        'Birch': Model.Birch_clustering,
        'DBSCAN': Model.DBSCAN_clustering,
        'AP': Model.affinity_propagation_clustering,
        'mbKMeans': Model.MiniBatchKMeans_clustering,
        'KMeans': Model.KMeans_clustering,
        'BRBM': Model.BernoulliRBM_classifier,
        'MLPC': Model.MLPC_classifier,
        'AdaBoost': Model.AdaBoost_classifier,
        'Bagging': Model.Bagging_classifier,
        'GNB': Model.GaussianNB_classifier,
        'MNB': Model.MultinomialNB_classifier,
        'BNB': Model.BernoulliNB_classifier,
        'KNN': Model.knn_classifier,
        'LR': Model.logistic_regression_classifier,
        'RF': Model.random_forest_classifier,
        'DT': Model.decision_tree_classifier,
        'SVM': Model.svm_classifier,
        'CV': Model.cross_validation,
        'GBDT': Model.gradient_boosting_classifier}

    return classifiers