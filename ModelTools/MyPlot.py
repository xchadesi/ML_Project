#-*-coding:utf8-*-

"""
常用的画图函数
"""

from pandas import DataFrame, Series
import numpy as np
import matplotlib.pyplot as plt
import sys
from matplotlib.font_manager import FontProperties

#配置信息
reload(sys)
sys.setdefaultencoding('utf-8')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['axes.unicode_minus'] = False
zfont = FontProperties(fname=r'c:\windows\fonts\simsun.ttc', size=12)

#画柱状图
def MyBar(data, legend, xlabel, ylabel, title, xticks):
    se = Series(data)
    se = se.sort_values(ascending=False)
    plt.xlabel(xlabel, fontproperties=zfont)
    plt.ylabel(ylabel, fontproperties=zfont)
    plt.title(title, fontproperties=zfont)
    a = np.array(range(0, len(xticks), 1))
    bar_width = 0.2
    plt.bar(a, se.values, width=0.2, align='center', color='b', alpha=0.8, edgecolor='white')
    plt.bar(a+bar_width, se.values, width=0.2, align='center', color='r', alpha=0.8, edgecolor='white')
    plt.xticks(size='small', rotation=30, fontproperties=zfont)
    plt.legend(legend, loc='upper right')
    plt.grid(color='#95a5a6', linestyle='--', linewidth=1, axis='y', alpha=0.4)
    plt.xticks(a, xticks)
    x = np.arange(len(se.index))
    y = np.array(list(se.values))
    for a, b in zip(x, y):
        plt.text(a, b+0.05, '%.0f' % b, ha='center', va='bottom', fontsize=8)
    plt.show()

#多条形图
def MyManyBar(data, legend, xlabel, ylabel, title, xticks):
    plt.xlabel(xlabel, fontproperties=zfont)
    plt.ylabel(ylabel, fontproperties=zfont)
    plt.title(title, fontproperties=zfont)
    a = np.array(range(0, len(xticks), 1))
    bar_width = 0.0
    color = ['r', 'b', 'y', 'g', 'p', 's', 'c']
    for d, col in zip(data, color):
        se = Series(d)
        se = se.sort_values(ascending=False)
        plt.bar(a+bar_width, se.values, width=0.2, align='center', color=col, alpha=0.8, edgecolor='white')
        x = np.arange(len(se.index))+bar_width
        y = np.array(list(se.values))
        for c, d in zip(x, y):
            plt.text(c, d+0.05, '%.0f' % d, ha='center', va='bottom', fontsize=8)
        bar_width += 0.2

    plt.xticks(size='small', rotation=30, fontproperties=zfont)
    plt.legend(legend, loc='upper right')
    plt.grid(color='#95a5a6', linestyle='--', linewidth=1, axis='y', alpha=0.4)
    plt.xticks(a+0.2, xticks)
    plt.show()

#多条形图
def MyManyBarh(data, legend, xlabel, ylabel, title, xticks):
    plt.xlabel(xlabel, fontproperties=zfont)
    plt.ylabel(ylabel, fontproperties=zfont)
    plt.title(title, fontproperties=zfont)
    a = np.array(range(0, len(xticks), 1))
    color = ['r', 'b', 'y']
    se = Series(data[0])
    se = se.sort_values(ascending=False)
    plt.bar(a, se.values, width=0.2, align='center', color='y', alpha=0.8, edgecolor='white')
    tag = se.values
    for d, col in zip(data[1:], color):
        se = Series(d)
        se = se.sort_values(ascending=False)
        plt.bar(a, se.values, width=0.2, align='center', color=col, alpha=0.8, edgecolor='white', bottom=tag)

    plt.xticks(size='small', rotation=30, fontproperties=zfont)
    plt.legend(legend, loc='upper right')
    plt.grid(color='#95a5a6', linestyle='--', linewidth=1, axis='y', alpha=0.4)
    plt.xticks(a, xticks)
    plt.show()

#画条形图
def MyBarh(data, legend, xlabel, ylabel, title, yticks):
    se = Series(data)
    se = se.sort_values(ascending=False)
    plt.xlabel(xlabel, fontproperties=zfont)
    plt.ylabel(ylabel, fontproperties=zfont)
    plt.title(title, fontproperties=zfont)
    a = np.array(range(0, len(xticks), 1))
    plt.barh(a, se.values, height=0.35, align='center', color='b', alpha=0.8, edgecolor='white')
    plt.yticks(size='small', rotation=30, fontproperties=zfont)
    plt.legend(legend, loc='upper right')
    plt.grid(color='#95a5a6', linestyle='--', linewidth=1, axis='y', alpha=0.4)
    plt.yticks(a, yticks)
    x = np.arange(len(se.index))
    y = np.array(list(se.values))
    for a, b in zip(y, x):
        plt.text(a+0.1, b-0.1, '%.0f' % b, ha='center', va='bottom', fontsize=8)
    #plt.ylim(0,1000)
    plt.show()

#画饼图
def MyPie(data, legend, title):
    se = Series(data)
    colors = ['red', 'yellowgreen', "#99CC01", "#FFFF01", "#0000FE", "#FE0000", "#A6A6A6", "#D9E021", '#FFF16E', '#0D8ECF', '#FA4D3D', '#D2D2D2', '#FFDE45', '#9b59b6']
    explode = (0.05, 0)
    plt.pie(se.values, labels=se.index, autopct='%1.1f%%', explode=explode, colors=colors, labeldistance=1.1,
            shadow=False, startangle=90, pctdistance=0.6)
    plt.title(title, fontproperties=zfont)
    plt.axis('equal')
    plt.legend(legend)
    plt.show()

#画气泡图
def MyScat(x, y, z, xlabel, ylabel, title,):
    colors = ['red', 'yellowgreen', "#99CC01", "#FFFF01", "#0000FE", "#FE0000", "#A6A6A6", "#D9E021", '#FFF16E', '#0D8ECF', '#FA4D3D', '#D2D2D2', '#FFDE45', '#9b59b6']
    plt.scatter(x, y, s=z, color=colors, alpha=0.6)
    plt.xlabel(xlabel, fontproperties=zfont)
    plt.ylabel(ylabel, fontproperties=zfont)
    plt.title(title, fontproperties=zfont)
    plt.show()

#画散点图
def MyScatter(x, y, xlabel, ylabel, title):
    colors = ['red', 'yellowgreen', "#99CC01", "#FFFF01", "#0000FE", "#FE0000", "#A6A6A6", "#D9E021", '#FFF16E', '#0D8ECF', '#FA4D3D', '#D2D2D2', '#FFDE45', '#9b59b6']
    plt.scatter(x, y, color=colors, alpha=0.6)
    plt.xlabel(xlabel, fontproperties=zfont)
    plt.ylabel(ylabel, fontproperties=zfont)
    plt.title(title, fontproperties=zfont)
    plt.show()

#画折线图
def MyCurve(x, y, xlabel, ylabel, title, xticks):
    fig = plt.figure()
    fig.add_subplot(111)
    #图表字体为华文细黑，字号为15
    plt.rc('font', family='STXihei', size=15)
    #创建折线图，数据源为按月贷款均值，标记点，标记线样式，线条宽度，标记点颜色和透明度
    plt.plot(x, y, color='#99CC01', linewidth=3, markeredgewidth=3, markeredgecolor='#99CC01', alpha=0.8)
    #plt.plot(x, y)
    #添加x轴标签
    plt.xlabel(xlabel)
    #添加y周标签
    plt.ylabel(ylabel)
    #添加图表标题
    plt.title(title)
    #添加图表网格线，设置网格线颜色，线形，宽度和透明度
    plt.grid(color='#95a5a6',linestyle='--', linewidth=1, axis='y', alpha=0.4)
    #设置数据分类名称
    #a = np.array(range(0, len(xticks), 1))
    plt.xticks(x, xticks)
    #输出图表
    plt.show()

#画箱线图
def mybox(data, xlabel, title):
    #图表字体为华文细黑，字号为15
    plt.rc('font', family='STXihei', size=15)
    #创建箱线图，数据源为贷款来源，设置横向显示
    plt.boxplot(data, 1, 'rs', vert=False)
    #添加x轴标题
    plt.xlabel(xlabel)
    #添加图表标题
    plt.title(title)
    #设置背景网格线的颜色，样式，尺寸和透明度
    plt.grid(color='#95a5a6', linestyle='--', linewidth=1, axis='both', alpha=0.4)
    #显示图表
    plt.show()

#直方图
def myHist(data, xlabel, ylabel, title):
    #图表字体为华文细黑，字号为15
    plt.rc('font', family='STXihei', size=15)
    #创建直方图，数据源为贷款金额，将数据分为8等份显示，设置颜色和显示方式，透明度等
    plt.hist(data, 8, normed=1, histtype='stepfilled', facecolor='#99CC01', rwidth=0.9,alpha=0.6, edgecolor='white')
    #添加x轴标题
    plt.xlabel(xlabel)
    #添加y轴标题
    plt.ylabel(ylabel)
    #添加图表标题
    plt.title(title)
    #设置背景网格线的颜色，样式，尺寸和透明度
    plt.grid(color='#95a5a6',linestyle='--', linewidth=1,axis='y',alpha=0.4)
    #显示图表
    plt.show()

# x = [[1,2,3,4],[5,6,7,8],[1,1,1,1]]
# y = [1,3]
# z = [100,380]
# xlabel = 'x'
# ylabel = 'y'
# xticks = ('1月','2月','3月','4月')
# title = '月'
# legend =['月','ee']
# MyManyBarh(x, legend, xlabel, ylabel, title, xticks)
