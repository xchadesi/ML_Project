#-*-coding:utf8-*-
import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_curve
from sklearn.preprocessing import OneHotEncoder
reload(sys)
sys.setdefaultencoding('utf-8')


train = pd.read_csv("train1")

train_x = train[[x for x in train.columns if x != 'TARGET']]
train_y = train['TARGET']

# 切分为测试集和训练集，比例0.5
X_train, X_test, y_train, y_test = train_test_split(train_x, train_y, test_size=0.5)
# 将训练集切分为两部分，一部分用于训练GBDT模型，另一部分输入到训练好的GBDT模型生成GBDT特征，然后作为LR的特征。这样分成两部分是为了防止过拟合。
X_train, X_train_lr, y_train, y_train_lr = train_test_split(X_train, y_train, test_size=0.5)

# 调用GBDT分类模型。
grd = GradientBoostingClassifier(
                    learning_rate=0.025,
                    n_estimators=1600,
                    max_depth=8,
                    min_samples_leaf=70,
                    min_samples_split=700,
                    max_features=11,
                    subsample=1.0,
                    random_state=10)

# 调用one-hot编码。
grd_enc = OneHotEncoder()

# 调用LR分类模型。
grd_lm = LogisticRegression(penalty='l1',
                            class_weight='balanced',
                            solver='liblinear',
                            multi_class='ovr')


'''使用X_train训练GBDT模型，后面用此模型构造特征'''
grd.fit(X_train, y_train)

# fit one-hot编码器
grd_enc.fit(grd.apply(X_train)[:, :, 0])

'''
使用训练好的GBDT模型构建特征，然后将新的特征输入到LR模型训练。
'''
grd_lm.fit(grd_enc.transform(grd.apply(X_train_lr)[:, :, 0]), y_train_lr)
# 用训练好的LR模型多X_test做预测
y_pred_grd_lm = grd_lm.predict_proba(grd_enc.transform(grd.apply(X_test)[:, :, 0]))[:, 1]
# 根据预测结果输出
fpr_grd_lm, tpr_grd_lm, _ = roc_curve(y_test, y_pred_grd_lm)
print fpr_grd_lm, tpr_grd_lm

def PlotRoc(Algorithm, PR, TR):
    #import matplotlib.pyplot as plt
    from sklearn.metrics import auc
    roc_auc = auc(PR, TR)
    print roc_auc
    # plt.title("ROC curve of %s (AUC = %.4f)" % (Algorithm, roc_auc))
    # plt.xlabel("False Positive Rate")
    # plt.ylabel("True Positive Rate")
    # plt.ylim(0.0, 1.0)
    # plt.xlim(0.0, 1.0)
    # plt.plot(PR, TR)
    # plt.show()


PlotRoc('GBDT+LR', fpr_grd_lm, tpr_grd_lm)

#train1----0.621489562495
#train----0.622887818147