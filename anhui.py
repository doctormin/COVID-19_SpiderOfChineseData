#34
#By Yimin Zhao
#-*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import urllib.request
import xlsxwriter
import time
import re
anhui = 'http://wjw.ah.gov.cn/news_list_450_1.html'         #卫健委的url
info_pattern = re.compile(r'.月.*日安徽省报告新型冠状病毒肺炎疫情情况')  


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
    
    for element in soup.find_all(name='div',attrs = {'class':'list'}):
        for info in element.find_all('a'):
            info_title = info.get_text()      #获取通报的标题
            if(info_pattern.match(info_title)):
                return(info.get('href'))
        
        
info_url = 'http://wjw.ah.gov.cn/'+find_url(anhui)
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
    for element in soup.find_all(name='div',attrs = {'class':'ar-artcon', 'id':'art_content'} ):
        print(element.get_text())
        f = open(r"D:\IIoT\20年寒假-疫情爬虫\Data\34.txt", mode = 'w', encoding = "utf-8")
        f.write(element.get_text())
        f.close()                    
if __name__ == '__main__':
    print('begin')
    get_data(info_url)
    print('finish')
    


