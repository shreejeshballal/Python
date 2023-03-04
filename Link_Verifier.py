import requests, bs4
page = requests.get("Your website link here from where the urls are to be extracted")

soup = bs4.BeautifulSoup(page.text,features="lxml")
links = soup.select('a')
urls = []
for i in links:
    x = i.get('href')
    if x and x[0] =='h':
        urls.appenSd(x)

for url in urls:
    res = requests.get(url)
    if res.status_code != requests.codes.ok:
        print('{0} is a broken link. Response: 404 Not Found'.format(url))