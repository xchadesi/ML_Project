#-*-coding:utf8-*-
"""
通用的LogisticRegression框架
"""
import sys
import pandas as pd
import numpy as np
from scipy import sparse
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
reload(sys)
sys.setdefaultencoding('utf-8')

# 1. load data
df_train = pd.DataFrame()
df_test = pd.DataFrame()
y_train = df_train['label'].values

# 2. process data
ss = StandardScaler()

# 3. feature engineering/encoding
# 3.1 For Labeled Feature
enc = OneHotEncoder()
feats = ["creativeID", "adID", "campaignID"]
for i, feat in enumerate(feats):
    x_train = enc.fit_transform(df_train[feat].values.reshape(-1, 1))
    x_test = enc.fit_transform(df_test[feat].values.reshape(-1, 1))
    if i == 0:
        X_train, X_test = x_train, x_test
    else:
        X_train, X_test = sparse.hstack((X_train, x_train)), sparse.hstack((X_test, x_test))

# 3.2 For Numerical Feature
# It must be a 2-D Data for StandardScalar, otherwise reshape(-1, len(feats)) is required
feats = ["price", "age"]

x_train = ss.fit_transform(df_train[feats].values)
x_test = ss.fit_transform(df_test[feats].values)
X_train, X_test = sparse.hstack((X_train, x_train)), sparse.hstack((X_test, x_test))

# model training
lr = LogisticRegression()
lr.fit(X_train, y_train)
proba_test = lr.predict_proba(X_test)[:, 1]