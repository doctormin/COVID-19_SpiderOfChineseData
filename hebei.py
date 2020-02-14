#!/usr/bin/env python
# coding: utf-8

# In[1]:


#13
#By Yimin Zhao
import requests
from bs4 import BeautifulSoup
import urllib.request
import xlsxwriter
import time
import re
heilongjiang = 'http://wsjkw.hebei.gov.cn/index.do?templet=new_list&cid=14&page=1'         #卫健委的url
info_pattern = re.compile(r'\n.*河北省.*新.*冠.*疫情.*')  

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
    
    for element in soup.find_all(name='td',attrs = {'class':'sy_new_list'}):
        for info in element.find_all('a'):
            info_title = info.get_text()      #获取通报的标题
            #print(repr(info_title))
            if(info_pattern.match(info_title)):
                return(info.get('href'))
                
info_url = 'http://wsjkw.hebei.gov.cn/' + find_url(heilongjiang)
print(info_url)


# In[2]:


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
    for element in soup.find_all(name='div',attrs = {'class':'con_wz'} ):
        print(element.get_text())
        f = open(r"D:/IIoT/20年寒假-疫情爬虫/Data/13.txt", mode ='w', encoding ="utf-8")
        f.write(element.get_text())
        f.close() 
                    
if __name__ == '__main__':
    print('begin')
    get_data(info_url)
    print('finish')


# In[2]:




