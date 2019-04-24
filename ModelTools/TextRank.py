#-*-coding:utf8-*-

"""
对关键词计算TextRank排序
"""

import networkx as nx
import numpy as np

def combine(word_list, window = 2):
    """构造在window下的单词组合，用来构造单词之间的边。
    Keyword arguments:
    word_list  --  list of str, 由单词组成的列表。
    windows    --  int, 窗口大小。
    """
    if window < 2: window = 2
    for x in xrange(1, window):
        if x >= len(word_list):
            break
        word_list2 = word_list[x:]
        res = zip(word_list, word_list2)
        for r in res:
            yield r

class AttrDict(dict):
    """Dict that can get attribute by dot"""
    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self

def sort_words(vertex_source, edge_source, window = 2, pagerank_config = {'alpha': 0.85,}):
    """将单词按关键程度从大到小排序
    Keyword arguments:
    vertex_source   --  一维维列表，列表的元素是单词，这些单词用来构造pagerank中的节点
    edge_source     --  一维列表，列表的元素是单词，根据单词位置关系构造pagerank中的边
    window          --  一个句子中相邻的window个单词，两两之间认为有边
    pagerank_config --  pagerank的设置
    """
    sorted_words = []
    word_index = {}
    index_word = {}
    words_number = 0
    #给每个word添加一个对应的id作为标识
    for word_list in vertex_source:
        for word in word_list:
            if not word_index.has_key(word):
                word_index[word] = words_number
                index_word[words_number] = word
                words_number += 1

    #构建单词共现矩阵
    graph = np.zeros((words_number, words_number))
    for word_list in edge_source:
        for w1, w2 in combine(word_list, window):
            if w1 in word_index and w2 in word_index:
                index1 = word_index[w1]
                index2 = word_index[w2]
                graph[index1][index2] = 1.0
                graph[index2][index1] = 1.0

    nx_graph = nx.from_numpy_matrix(graph)
    scores = nx.pagerank(nx_graph, **pagerank_config)
    sorted_scores = sorted(scores.items(), key = lambda item: item[1], reverse=True)
    for index, score in sorted_scores:
        item = AttrDict(word=index_word[index], weight=score)
        sorted_words.append(item)

    return sorted_words

def get_keywords(sorted_words, num = 6, word_min_len = 1):
        """获取最重要的num个长度大于等于word_min_len的关键词。
        Return:关键词列表。
        """
        result = []
        count = 0
        for item in sorted_words:
            if count >= num:
                break
            if len(item.word) >= word_min_len:
                result.append(item)
                count += 1
        return result

def get_keyphrases(text,words_no_filter,sorted_words, keywords_num = 12, min_occur_num = 2):
    """获取关键短语。
    获取 keywords_num 个关键词构造的可能出现的短语，要求这个短语在原文本中至少出现的次数为min_occur_num。
    Return:关键短语的列表。
    """
    keywords_set = set([item.word for item in get_keywords(sorted_words, num=keywords_num, word_min_len = 1)])
    keyphrases = set()
    for word in keywords_set:
        for wd in keywords_set:
            phrases = word+wd
            if text.count(phrases) >= min_occur_num:
                keyphrases.add(phrases)
    return keyphrases