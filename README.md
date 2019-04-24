# ML_Project
前期做过的一些机器学习项目整理

## FoolAlgorithm

这个项目是刚接触机器学习的时候，尝试利用pipline对常用机器学习算法建立统一的流程，实现如下功能：<br>
1、算法参数调节；<br>
2、数据特征选择；<br>
3、结果预测；<br>

前端网站是用jsp写的，向后端传递参数、调用python模型运行的结果。<br>
后端在sklearn的基础上，直接调用相关算法模型，然后利用GridSearchCV搜索最优参数，运行时间稍微长点，也算是最简单的AutoML了哈。<br>
后端模型设置了如下几种算法：MLPC、AdaBoost、LR、RF、SVM、GBDT、Bagging、KNN、DT、GNB等。<br>

<img src="https://github.com/xchadesi/ML_Project/blob/master/FoolAlgorithm/lgo.png" />
<img src="https://github.com/xchadesi/ML_Project/blob/master/FoolAlgorithm/11.PNG" />
<img src="https://github.com/xchadesi/ML_Project/blob/master/FoolAlgorithm/22.png" />
<img src="https://github.com/xchadesi/ML_Project/blob/master/FoolAlgorithm/33.png" />
<img src="https://github.com/xchadesi/ML_Project/blob/master/FoolAlgorithm/44.png" />
<img src="https://github.com/xchadesi/ML_Project/blob/master/FoolAlgorithm/55.png" />
<img src="https://github.com/xchadesi/ML_Project/blob/master/FoolAlgorithm/66.png" />

