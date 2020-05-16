#线性回归预测数据
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import datasets, linear_model
import pymongo
from pandas.io.json import json_normalize
import wordcloud

client = pymongo.MongoClient('mongodb://localhost:27017/')
dblist = client.list_database_names()
db = client['admin']
table = db['Scrapy']
frame = pd.DataFrame(list(table.find()))
cols = frame[['date', 'blue']]
regr = linear_model.LinearRegression()
regr.fit(frame[['num']],frame[['blue']])
predict_outcome = regr.predict(np.array(2020035).reshape(1, -1))
predictions = {
    'intercept':regr.intercept_,
    'coefficient':regr.coef_,
    'predicted_value':predict_outcome
}
print(predictions)

# plt.scatter(frame[['num']].values.astype(int), frame[['blue']].values.astype(int))
# plt.show()

# plt.plot(frame[['blue']].values.astype(int))
# plt.ylabel('some numbers')
# plt.show()

# 创建词云对象
w = wordcloud.WordCloud()
# 调用词云对象的generate方法，将文本传入
#np.squeeze去除多余的维度(即[])
numlist = np.squeeze(frame[['blue']].values.tolist())
w.fit_words(dict(numlist))
plt.imshow(w)
plt.show()

print('end')