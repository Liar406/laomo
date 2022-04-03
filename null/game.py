import requests
import time
from bs4 import BeautifulSoup
import re
def searchby():
  url="http://eea.whu.edu.cn/rcpy/bkspy.htm"
  response=requests.get(url)
  response.encoding='etf-8'
  soup=BeautifulSoup(response.text,'html.parser')
  res=soup.find_all('p')
  for string in res:
    tmp=re.search("保研",str(string))
    if tmp:
      print(tmp)
if __name__=='__main__': 
  while True:
    searchby()
    time.sleep(5)