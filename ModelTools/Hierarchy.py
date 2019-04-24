#-*-coding:utf8-*-
"""
做层次聚类
"""
import sys
from scipy.cluster.hierarchy import ward, dendrogram
import matplotlib.pyplot as plt
reload(sys)
sys.setdefaultencoding('utf-8')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['font.family']='sans-serif'
plt.rcParams['axes.unicode_minus'] = False


def Myhierarchy(mx, titles, save_pig_path):
    """
    :param mx: 相似度矩阵
    :param titles: 特征名称
    """
    linkage_matrix = ward(mx)
    plt.subplots(figsize=(15, 20))
    dendrogram(linkage_matrix, orientation="left", labels=titles);
    plt.tick_params(axis= 'x', which='both', bottom='off', top='off', labelbottom='off')
    plt.tight_layout()
    plt.savefig(save_pig_path, dpi=200)

def AgglomerativeClustering(mx, n_clusters):
    from sklearn.cluster import AgglomerativeClustering
    model = AgglomerativeClustering(n_clusters=n_clusters, affinity='euclidean', memory=None, connectivity=mx, compute_full_tree='auto', linkage='ward', pooling_func=None)
    return model

def affinity_propagation_clustering(best_parameters={}):
    from sklearn.cluster import affinity_propagation
    if len(best_parameters) > 0:
        model = affinity_propagation(S=best_parameters['Model__S'], preference=best_parameters['Model__preference'], convergence_iter=best_parameters['Model__convergence_iter'], max_iter=best_parameters['Model__max_iter'], damping=best_parameters['Model__damping'], copy=best_parameters['Model__copy'], verbose=best_parameters['Model__verbose'], return_n_iter=best_parameters['Model__return_n_iter'])
    else:
        model = affinity_propagation()
    return model

#MeanShift
def MeanShift_clustering(best_parameters={}):
    from sklearn.cluster import MeanShift
    if len(best_parameters) > 0:
        model = MeanShift(bandwidth=best_parameters['Model__bandwidth'], seeds=best_parameters['Model__seeds'], bin_seeding=best_parameters['Model__bin_seeding'], min_bin_freq=best_parameters['Model__min_bin_freq'], cluster_all=best_parameters['Model__cluster_all'], n_jobs=best_parameters['Model__n_jobs'])
    else:
        model = MeanShift()
    return model

#DBSCANClustering
def DBSCAN_clustering(best_parameters={}):
    from sklearn.cluster import DBSCAN
    if len(best_parameters) > 0:
        model = DBSCAN(eps=best_parameters['Model__eps'], min_samples=best_parameters['Model__min_samples'], metric=best_parameters['Model__metric'], metric_params=best_parameters['Model__metric_params'], algorithm=best_parameters['Model__algorithm'], leaf_size=best_parameters['Model__leaf_size'], p=best_parameters['Model__p'], n_jobs=best_parameters['Model__n_jobs'])
    else:
        model = DBSCAN()
    return model