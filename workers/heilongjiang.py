#23
#By Yimin Zhao
import requests
from bs4 import BeautifulSoup
import urllib.request
import xlsxwriter
import time
import re

heilongjiang = 'http://wsjkw.hlj.gov.cn/index.php/Home/Zwgk/all/typeid/42'         #卫健委的url
info_pattern = re.compile(r'最新疫情通报')  


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
    
    for element in soup.find_all(name='div',attrs = {'class':'wenzhanglist'}):
        for info in element.find_all('a'):
            info_title = info.get_text()      #获取通报的标题
            if(info_pattern.match(info_title)):
                return(info.get('href'))
        

        
info_url = 'http://wsjkw.hlj.gov.cn' + find_url(heilongjiang)
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
    for element in soup.find_all(name='div',attrs = {'class':'danye'} ):
        print(element.get_text())
        f = open(r"./Data/23.txt", mode ='w', encoding ="utf-8")
        f.write(element.get_text())
        f.close() 
                    
if __name__ == '__main__':
    print('begin')
    get_data(info_url)
    print('finish')


