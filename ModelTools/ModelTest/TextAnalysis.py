# coding:utf-8

"""
文本分析常用函数：
1、给原始语料库分词去停用词；
2、加载语料库
3、计算TF-IDF
4、构建词语相似度模型
5、加载词语相似度模型
6、计算词语之间的相似度矩阵
7、利用词语的相似度做层次聚类分析
8、利用词语的相似度做Kmeans聚类分析
9、计算整个句子的相似度
10、提取文本中的中文/字母/数字
"""


import sys
import gensim
import codecs
import jieba.posseg as pseg
import jieba
import math
import re
from gensim import corpora, models
reload(sys)
sys.setdefaultencoding('utf-8')

#给原始语料库分词去停用词
def tokenization(text, stopwords_path):
    #构建停用词表
    stopwords_path = stopwords_path
    stopwords = codecs.open(stopwords_path, 'r', encoding='utf8').readlines()
    stopwords = [w.strip() for w in stopwords]
    #结巴分词后标记的词性
    stop_flag = ['x', 'c', 'u', 'd', 'p', 't', 'uj', 'm', 'f', 'r']
    result = []
    words = pseg.cut(text)
    for word, flag in words:
        if flag not in stop_flag and word not in stopwords:
            result.append(word)
    return result

#加载语料库
def TextLoader(path, stopwords_path='Alrealy'):
    input = codecs.open(path, 'r', encoding='utf-8')
    lines = input.readlines()
    if stopwords_path == 'Alrealy':
        for line in lines:
            segments = line.split(' ')
            yield segments
    else:
        for line in lines:
            segments = tokenization(line, stopwords_path)
            yield segments

#计算TF-IDF
def getTF_IDF(segments):
    #获取语料库
    corpus = []
    for token in segments:
        corpus.append(tokenization(token))
    #建立一个词袋模型
    dictionary = corpora.Dictionary(corpus)
    doc_vectors = [dictionary.doc2bow(text) for text in corpus]
    tfidf = models.TfidfModel(doc_vectors)
    tfidf_vectors = tfidf[doc_vectors]
    return tfidf_vectors

#构建词语相似度模型
def WordSimilaryModel(sentences, size, min_count, model_savePath):
    model = gensim.models.Word2Vec(sentences, size=size, min_count=min_count)
    model.save(model_savePath)

#加载词语相似度模型
def getWordSimilaryModel(model_Path):
    model = gensim.models.Word2Vec.load(model_Path)
    return model

#计算词语之间的相似度矩阵
def getSimilaryMatrix(words, model_Path, word_min_count):
    model = gensim.models.Word2Vec.load(model_Path)
    mx = []
    for word1 in words:
        m = []
        for word2 in words:
            if len(word1) > word_min_count and len(word2) > word_min_count:
                try:
                    m.append(model.similarity(word1, word2))
                except:
                    continue
        if len(m) != 0:
            mx.append(m)
    return mx

#利用词语的相似度做层次聚类分析
def WordHierarchyClustering(mx, words, pig_save_path):
    from scipy.cluster.hierarchy import ward, dendrogram
    import matplotlib.pyplot as plt
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['font.family']='sans-serif'
    plt.rcParams['axes.unicode_minus'] = False

    linkage_matrix = ward(mx)
    plt.subplots(figsize=(15, 20))
    dendrogram(linkage_matrix, orientation="left", labels=words);

    plt.tick_params(axis= 'x', which='both', bottom='off', top='off', labelbottom='off')
    plt.tight_layout()
    plt.savefig(pig_save_path, dpi=200)
    plt.show()

#利用词语的相似度做Kmeans聚类分析
def WordKmeansClustering(mx, words, num_clusters, model_result_path):
    from sklearn.cluster import KMeans
    num_clusters = num_clusters
    km = KMeans(n_clusters=num_clusters)
    km.fit(mx)
    cluster_labels = km.labels_.tolist()
    word = {}
    for (w, c) in zip(words, cluster_labels):
        if not word.has_key(c):
            word[c] = w
        else:
            word[c] = word.get(c) + ' ' + w
    fil = open(model_result_path, 'w')
    for cluster_label, wds in word.items():
        line = cluster_label + ',' + wds
        fil.write(line)
        fil.write('\n')
    fil.close()

#计算整个句子的相似度
def get_similarity(sentence1, sentence2):
    sentence1 = sentence1.replace(',', '')
    sentence2 = sentence2.replace(',', '')
    words1 = list(jieba.cut(sentence1))
    words2 = list(jieba.cut(sentence2))
    words = list(set(words1 + words2))
    vector1 = [float(words1.count(word)) for word in words]
    vector2 = [float(words2.count(word)) for word in words]
    vector3 = [vector1[x]*vector2[x] for x in xrange(len(vector1))]
    vector4 = [1 for num in vector3 if num > 0.]
    co_occur_num = sum(vector4)
    if abs(co_occur_num) <= 1e-12:
        return 0.
    denominator = math.log(float(len(words1))) + math.log(float(len(words2)))
    if abs(denominator) < 1e-12:
        return 0.
    return co_occur_num / denominator

#提取文本中的中文/字母/数字
def translate(text):
    # 处理前进行相关的处理，包括转换成Unicode等
    text = text.strip().decode('utf-8', 'ignore')
    # 中文的编码范围是：\u4e00到\u9fa5
    p = re.compile(ur'[^a-zA-Z0-9\u4e00-\u9fa5]')
    zh = " ".join(p.split(text)).strip()
    outText = ",".join(zh.split())
    return outText



