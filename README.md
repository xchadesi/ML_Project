# ML_Project
前期做过的一些机器学习项目整理

## 一、FoolAlgorithm

这个项目是刚接触机器学习的时候，尝试利用pipline对常用机器学习算法建立统一的流程，实现如下功能：<br>
1、算法参数调节；<br>
2、数据特征选择；<br>
3、结果预测；<br>

前端网站是用jsp写的，向后端传递参数、调用python模型运行的结果。<br>
后端在sklearn的基础上，直接调用相关算法模型，然后利用GridSearchCV搜索最优参数，运行时间稍微长点，也算是最简单的AutoML了哈。<br>
后端模型设置了如下几种算法：MLPC、AdaBoost、LR、RF、SVM、GBDT、Bagging、KNN、DT、GNB等。<br>

<img src="https://github.com/xchadesi/ML_Project/blob/master/FoolAlgorithm/lgo.png" height=300, width=600/>
<img src="https://github.com/xchadesi/ML_Project/blob/master/FoolAlgorithm/11.png" height=300, width=600/>
<img src="https://github.com/xchadesi/ML_Project/blob/master/FoolAlgorithm/22.png" height=300, width=600/>
<img src="https://github.com/xchadesi/ML_Project/blob/master/FoolAlgorithm/33.png" height=300, width=600/>
<img src="https://github.com/xchadesi/ML_Project/blob/master/FoolAlgorithm/44.png" height=300, width=600/>
<img src="https://github.com/xchadesi/ML_Project/blob/master/FoolAlgorithm/55.png" height=300, width=600/>
<img src="https://github.com/xchadesi/ML_Project/blob/master/FoolAlgorithm/66.png" height=300, width=600/>

## 二、ModelTools

常用的工具模块，包括上面FoolAlgorithm中用到的一些数据预处理、分类模型等，还包括：<br>
1、常用文本分析、textRank等；<br>
2、数据库连接；<br>
3、画图；<br>
4、常用回归分析；<br>
5、常用聚类等；<br>
