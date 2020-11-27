# NetDepress Music

### 1. Introduction

This project aims to analyse the factors that influence the emotion of comments from NetEase(NetDepress) Music.







### 2. Table Columns

(1) Table `music`

| Column Name |   Type    |                Description                 |
| :---------: | :-------: | :----------------------------------------: |
|     id      |    int    |                                            |
|    name     |    str    |                                            |
|    types    | list[str] |                type labels                 |
|    words    |    str    | words of song, sentences are split by `\n` |
|   emotion   |  double   |  emotion value of the words of song (0-1)  |

(2) Table `comment`

| Column Name |  Type  |            Description             |
| :---------: | :----: | :--------------------------------: |
|     id      |  int   |                                    |
|  music_id   |  int   |                                    |
|   user_id   |  int   |                                    |
|   content   |  str   |                                    |
|   is_hot    |  bool  |                                    |
| liked_count |  int   |                                    |
|   emotion   | double | emotion value of the comment (0-1) |







### 3. Visualization Graphs

1. Comment count-clock graph (line chart) for comments from [each type | all types].
2. Comment count-date graph (line chart) for comments from [each type | all types].
3. Average Emotion Level graph (bar chart) for comments from [each type | all types]. The average of all comments is represented as a horizontal dotted line.
4. Emotion-clock graph (line chart) for comments from [each type | all types].
5. Emotion-date graph (line chart) for comments from [each type | all types]. Mark the social events that have significant impact on the emotion curve if possible.
6. Relevance between emotion of words of song and its comments (scatter plot).

The curve that represents feature about comments from all types should be emphasized.

> 1. [不同类型歌曲|所有歌曲]下评论数随一天内的时间变化曲线.
> 2. [不同类型歌曲|所有歌曲]下评论数随日期变化的曲线.
> 3. [不同类型歌曲|所有歌曲]下评论平均情绪条形图. 所有歌曲的平均情绪以一条虚水平线表示.
> 4. [不同类型歌曲|所有歌曲]下评论平均情绪随一天内的时间变化曲线.
> 5. [不同类型歌曲|所有歌曲]下评论平均情绪随日期变化的曲线. (如果可行的话)在曲线上标注出对于歌曲评论情绪变化产生重大影响的社会事件.
> 6. 歌词情绪和评论评论情绪相关性的散点图.
>
> 代表所有评论特征的曲线应强调显示.


