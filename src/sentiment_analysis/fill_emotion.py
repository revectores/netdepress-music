from pathlib import Path

import pandas as pd
from snownlp import SnowNLP



def fill_emotion():
    comments_csv_path = Path('.') / '../data/comments.csv'
    doc = pd.read_csv(comments_csv_path)
    doc = doc.copy()
    row_num, col_num = doc.shape
    for i in range(row_num):
        text = doc['content'].loc[i]
        doc['emotion'].loc[i] = SnowNLP(text).sentiments

    doc.to_csv(comments_csv_path, index=False, encoding='utf-8')


if __name__ == '__main__':
    fill_emotion()