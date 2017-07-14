import requests
from bs4 import BeautifulSoup

payload = {
	'from': '/bbs/Gossiping/index.html',
	'yes': 'yes'
}

headers = {	
	'User-Agen' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36(KHTML,like Gecko)Chrome/59.0.3071.115 Safari/537.36'
}

rs = requests.Session()

rs.post('https://www.ptt.cc/ask/over18', data=payload, headers=headers)
res = rs.get('https://www.ptt.cc/bbs/Gossiping/index.html', headers=headers)


soup = BeautifulSoup(res.text, 'html.parser')


items = soup.select('.r-ent')
#class 選擇器用句點 '.'  如果是ID則用'＃'字號 

for item in items:
	print('日期{}'.format(item.select('.date')[0].text), '作者:'+(item.select('.author')[0].text),
		item.select('.title')[0].text)