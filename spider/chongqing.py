#50
#By Yimin Zhao
import requests
from bs4 import BeautifulSoup
import urllib.request
import xlsxwriter
import time
import re

chongqing = 'http://wsjkw.cq.gov.cn/yqxxyqtb/'         #卫健委的url
info_pattern = re.compile(r'.*重庆.*新.*疫情.*')

#找到通报疫情的url
def find_url(web_address):
    #获取网页信息
    while(1):
        try:
            res = requests.get(web_address,timeout=(5, 10))
            flag = 1
            break
        except:
            print("retry")
            flag=0
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, features = 'html.parser')      #结构化处理 
    for element in soup.find_all(name='div',attrs = {'class':'newslist'}):
        #print(element)
        for info in element.find_all('a'):
            for title in info.find_all(name = 'span', attrs = {'class':'span-title'}):
                #print(title)
                info_title = title.get_text().strip()
                #print(repr(info_title))     #获取通报的标题
                #print(repr(info_pattern))
                #print(info_pattern.match(info_title))
                if(info_pattern.match(info_title)):
                    return(info.get('href'))        
info_url = 'http://wsjkw.cq.gov.cn' + find_url(chongqing)
print(info_url)


def get_data(web_address):
    #获取网页信息
    while(1):
        try:
            res = requests.get(web_address,timeout=2)
            flag=1
            break
        except:
            print("retry")
            flag=0
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')      #结构化处理
    for element in soup.find_all(name='div',attrs = {'class':'uedit'} ):
        print(element.get_text())
        f = open(r"/Data/50.txt", mode ='w', encoding ="utf-8")
        f.write(element.get_text())
        f.close() 
                    
if __name__ == '__main__':
    print('begin')
    get_data(info_url)
    print('finish')


