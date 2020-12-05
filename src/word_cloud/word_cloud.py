import jieba
import pandas as pd
import re
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter


stopwords_paths = ['hit_stopwords.txt', 'cn_stopwords.txt',
                   'baidu_stopwords.txt', 'scu_stopwords.txt']  #  停用词路径


def generate_stopwords(words_list):
    for i in stopwords_paths:   # 保存停用词表
        file = open(i, encoding="utf8")
        try:
            stopwords_text = file.read()
        finally:
            file.close()  # 关闭资源
        words_list += stopwords_text.split("\n")
    return words_list


def preprocessing(doc, music_id):
    text = []
    final_text = []
    row_num, col_num = doc.shape
    for i in range(row_num):  # 正则匹配中文
        if doc['music_id'].loc[i] == music_id:
            for j in re.findall(r'[\u4e00-\u9fa5]*', doc['content'].loc[i]):
                if j != '':
                    text.append(j)

    cut_words = map(lambda s: list(jieba.cut(s)), text)
    for i in list(cut_words):
        for j in i:
            if j not in stopwords:
                final_text.append(j)
    return final_text


stopwords = []
generate_stopwords(stopwords)   #  生成停用词表

data = pd.read_csv(r'../data/comments.csv')
listType = data[u'music_id'].unique()   #  获取所有音乐id
for i in list(listType):
    word_count = Counter(preprocessing(data,i))
    wc = WordCloud(font_path='STZHONGS.TTF',
                   background_color='White', max_words=50,)
    wc.generate_from_frequencies(dict(word_count))  # 根据给定词频生成词云
    wc.to_file('../data/word_cloud/%s.png' % str(i))  # 保存的图片命名为music_id
