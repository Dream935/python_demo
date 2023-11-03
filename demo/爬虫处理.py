import pandas as pd
import matplotlib.pyplot as plt
from snownlp import SnowNLP
import jieba
import jieba.analyse

# 读取数据集
df = pd.read_csv('data.csv')

# 统计用户评论数排名前10的用户
top_users = df['用户名'].value_counts().head(10)
print(top_users)

# 统计各个评分等级的评论数量占比
rating_counts = df['评分'].value_counts(normalize=True)
print(rating_counts)

# 统计每天的评论数，并绘制折线图
df['评论时间'] = pd.to_datetime(df['评论时间'])
daily_counts = df.resample('D', on='评论时间').size()
plt.plot(daily_counts)
plt.show()

# 对评论内容进行情感分析，得出正面评论数量和负面评论数量占比
sentiments = df['评论内容'].apply(lambda x: SnowNLP(x).sentiments)
positive_count = (sentiments > 0.5).sum()
negative_count = (sentiments < 0.5).sum()
total_count = len(sentiments)
print('正面评论占比：', positive_count / total_count)
print('负面评论占比：', negative_count / total_count)

# 对评论内容进行关键词提取，得出最常出现的关键词
content = ''.join(df['评论内容'].tolist())
keywords = jieba.analyse.extract_tags(content, topK=10)
print(keywords)