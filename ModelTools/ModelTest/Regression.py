#-*-coding:utf8-*-
"""
做回归分析
"""
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

Model = None

#最小二乘回归（OLS）
# from sklearn import linear_model
# Model = linear_model.LinearRegression()
#
# #岭回归（Ridge Regression）
# from sklearn import linear_model
# Model = linear_model.Ridge (alpha = .5)
#
# #核岭回归（Kernel ridge regression）
# from sklearn.kernel_ridge import KernelRidge
# Model = KernelRidge(kernel='rbf', alpha=0.1, gamma=10)
#
# #支持向量机回归（SVR）
# from sklearn import svm
# Model = svm.SVR()
#
# #套索回归（Lasso）
# from sklearn import linear_model
# Model = linear_model.Lasso(alpha = 0.1)
#
# #弹性网络回归（Elastic Net）
# from sklearn.linear_model import ElasticNet
# Model = ElasticNet(random_state=0)
#
# #贝叶斯回归（Bayesian Regression）
# from sklearn import linear_model
# Model = linear_model.BayesianRidge()
#
# #稳健回归（Robustness regression）
# from sklearn import linear_model
# Model = linear_model.RANSACRegressor()
#
# #多项式回归（Polynomial regression——多项式基函数回归）
# from sklearn.preprocessing import PolynomialFeatures
# Model = PolynomialFeatures(degree=2)
#
# #高斯过程回归（Gaussian Process Regression）
# #偏最小二乘回归（PLS）
# from sklearn.cross_decomposition import PLSCanonical
# Model = PLSCanonical(algorithm='nipals', copy=True, max_iter=500, n_components=2,scale=True, tol=1e-06)
#
# #典型相关分析（CCA）
# from sklearn.cross_decomposition import CCA
# Model = CCA(n_components=2)

if __name__ == '__main__':
    pass