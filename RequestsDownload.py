import requests


res = requests.get("")
res.raise_for_status()


newFile = open('RomeoJulient.txt','wb')

for chunk in res.iter_content(10000):
    newFile.write(chunk)

newFile.close()