from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
import time



baseurl = 'https://www.instagram.com/explore/tags/'
plusurl = input('검색할태그를 입력하세요 : ' )
url = baseurl + quote_plus(plusurl)

driver=webdriver.Chrome(executable_path="../webdriver/chromedriver.exe")
driver.get(url)

time.sleep(5)

html =driver.page_source
soup= BeautifulSoup(html,"html.parser")

insta =soup.select('.v1Nh3.kIKUG._bz0w')#원하는 태그안에 있는 정보를 가져와서 저장, 다가져온거임

for i in insta:
    sup = i.a['href']
    link= 'https://www.instagram.com'+ sup
    driver.get(link)

    time.sleep(5)
    sub = driver.page_source
    html= BeautifulSoup(sub,'html.parser')
    like1 = str(html.find_all(attrs={'class': 'Nm9Fw'}))
    like=[]
    if (like1=='[]'):
        like = '0'
    elif (like1.find('span')==1):
        like = like1.split('좋아요')[1].split('개')[0]
    elif (like1.find('span')!=1):
        like = like1.split('<span>')[1].split('</span>')[0]
    print(like)