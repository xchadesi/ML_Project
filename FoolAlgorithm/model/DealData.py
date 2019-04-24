#-*-coding:utf8-*-

import sys
from sklearn.model_selection import train_test_split
reload(sys)
sys.setdefaultencoding('utf-8')

def read_data(path):
    import pandas as pd
    data = pd.read_csv(path, sep=',', header=0)
    return data

def get_train_test(data, y_name, data_radio=0.3):

    x_train = data[[x for x in data.columns if x != y_name]]
    y_train = data[y_name]
    train_x, test_x, train_y, test_y = train_test_split(x_train, y_train, test_size=data_radio, random_state=0)

    return train_x, test_x, train_y, test_y