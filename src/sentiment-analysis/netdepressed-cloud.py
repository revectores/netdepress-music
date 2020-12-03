from snownlp import SnowNLP
import pandas as pd

doc = pd.read_csv(r"..\data\comments.csv")
doc = doc.copy()
row_num, col_num = doc.shape
for i in range(row_num):
    text = doc['content'].loc[i]
    doc['emotion'].loc[i] = SnowNLP(text).sentiments

doc.to_csv('..\data\comments.csv', index=False, encoding='utf-8')



