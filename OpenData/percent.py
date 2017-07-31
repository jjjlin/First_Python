import requests
import json
import matplotlib.pyplot as plt

url = 'http://data.fda.gov.tw/cacheData/35_3.json'

res = requests.get(url)

items = json.loads(res.text)

data = [0, 0]

for item in items:
	if item[6]['負責人性別']  == '男':
		data[0] += 1
	elif item[6]['負責人性別']  == '女':
		data[1] += 1

labels = ['man', 'woman']

plt.pie(data, labels=labels, autopct='%1.1f%%')
plt.show()
