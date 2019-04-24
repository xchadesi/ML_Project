#-*-coding:utf8-*-

"""
计算用户特征,每个index的特征都会在一个字典中
每个特征写一个函数
每个函数内部可以自由修改，但返回值必须是满足条件的字典
"""

import pandas as pd

def getF1(data):
    user = data
    result = {}
    for index, fw, fn in zip(user.index, user['wb_follow'], user['wb_fans']):
        if int(fn) != 0:
            fw_fan = float(fw)/int(fn)
        else:
            fw_fan = float(fw)
        result[index] = fw_fan

    return result

def getF(data):
    Feature = []
    Feature.append(getF1(data))

    return Feature