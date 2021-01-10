from pathlib import Path
import pandas as pd
from snownlp import SnowNLP
from senta import Senta


def fill_emotion():
    my_senta = Senta()
    my_senta.init_model(model_class="ernie_1.0_skep_large_ch", task="sentiment_classify", use_cuda=False)
    comments_csv_path = Path('.') / '../data/comments.csv'
    doc = pd.read_csv(comments_csv_path)
    doc = doc.copy()
    row_num, col_num = doc.shape
    for i in range(row_num):
        text = doc['content'].loc[i]
        doc['emotion'].loc[i] = int(my_senta.predict(text)[0][1] == "positive")

    doc.to_csv(comments_csv_path, index=False, encoding='utf-8')


if __name__ == '__main__':
    fill_emotion()