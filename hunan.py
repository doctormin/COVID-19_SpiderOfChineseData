#!/usr/bin/env python
# coding: utf-8

# In[1]:


#-*- coding: utf-8 -*-
#43 
#By Yimin Zhao
import requests
from bs4 import BeautifulSoup
import urllib.request
import xlsxwriter
import time
import re
hunan = 'http://wjw.hunan.gov.cn/wjw/xxgk/gzdt/zyxw_1/index.html'         #卫健委的url
info_name = re.compile(r'湖南省新.*冠.*疫情.*发布')             #每次通告名称相同

#找到通报疫情的url
def find_url(web_address):
    #获取网页信息
    while(1):
        try:
            res = requests.get(web_address,timeout=(5, 10))
            flag=1
            break
        except:
            print("retry")
            flag=0
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')      #结构化处理
    #print(res.text)
    for element in soup.find_all(name='tbody',attrs = {'class':'table_list_st'}):
        for info in element.find_all('a'):
            info_title = info.get_text().strip() 
            print(info_title)#获取通报的标题
            if(info_name.match(info_title)):
                return(info.get('href'))
        

        
info_url = 'http://wjw.hunan.gov.cn'+find_url(hunan)
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
    
    for element in soup.find_all(name='div',attrs = {'class':'main_con_zw'}):
        print(element.get_text())
        f = open(r"D:\IIoT\20年寒假-疫情爬虫\Data\43.txt", mode = 'w', encoding = "utf-8")
        f.write(element.get_text())
        f.close() 
                    
if __name__ == '__main__':
    print('begin')
    get_data(info_url)
    print('finish')
    


# In[2]:




