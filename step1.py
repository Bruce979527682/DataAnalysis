import pymongo
import matplotlib.pyplot as plt
import numpy as np
from pandas.io.json import json_normalize
client = pymongo.MongoClient('mongodb://localhost:27017/')
dblist = client.list_database_names()
db = client['admin']
data = db['Scrapy'].find()
rows = json_normalize(data)
print('end')
