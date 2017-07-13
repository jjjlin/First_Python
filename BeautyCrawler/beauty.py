import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
headers = {	
'User-Agen' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36(KHTML,like Gecko)Chrome/59.0.3071.115 Safari/537.36'
}

res = requests.get('https://www.ptt.cc/bbs/Beauty/M.1499883205.A.471.html', headers=headers)

#print(res.text)

soup = BeautifulSoup(res.text, 'html.parser')

images = soup.select('a[href^=http://i.imgur]')

#print(images)

for image in images:
	print(image['href'])
	filename = image['href'].split('/')[3]
	img = urlopen(image['href'])
	with open('./images/' + str(filename), 'wb') as f:
		f.write(img.read())





		
	