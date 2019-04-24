#-*-coding:utf8-*-

"""
通过设定不同阈值来评估模型
"""

import sys

#配置信息
reload(sys)
sys.setdefaultencoding('utf-8')

#计算AOC，并画出ROC曲线
def PlotRoc(PR, TR):
    import matplotlib.pyplot as plt
    from sklearn.metrics import auc
    roc_auc = auc(PR, TR)
    plt.title("ROC curve of %s (AUC = %.4f)" % ('svm', roc_auc))
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.ylim(0.0, 1.0)
    plt.xlim(0.0, 1.0)
    plt.plot(PR, TR)
    plt.show()

#根据预测结果和实际结果比较分析，获得结果的真正率、假正率以及ROC曲线
def AnalysisResult(func, threshold, data):
    data.columns = ['id', 'result']
    TR = []
    PR = []
    for th in threshold:
        result = func(threshold=th)
        TP = 0
        FP = 0
        FN = 0
        for id, res in result.items():
            recon = data[data.id == id]['result']
            if res == 1 and recon.values[0] == 1:
                TP += 1
            if res == 1 and recon.values[0] == 0:
                FP += 1
            if res == 0 and recon.values[0] == 1:
                FN += 1
        print '精确率：%s' % str(TP/float(TP+FP))
        print '召回率：%s' % str(TP/float(TP+FN))
        print '综合F1值: %s' % str(2*TP/float(FP+FN+2*TP))

        TR.append(TP/float(TP+FN))
        PR.append(FP/float(FP+FN))
    #AOC曲线
    PlotRoc(PR, TR)

