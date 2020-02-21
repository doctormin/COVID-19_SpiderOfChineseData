#!/usr/bin/env python
# coding: utf-8

# In[1]:


#21
#By Yimin Zhao
import requests
from bs4 import BeautifulSoup
import re

liaoning = 'http://wsjk.ln.gov.cn/wst_wsjskx/'         #卫健委的url
info_pattern = re.compile(r'.*辽宁.*新.*冠.*疫情.*情况.*')  


#找到通报疫情的url
def find_url(web_address):
    #获取网页信息
    while(1):
        try:
            headers = {"user-agent": "Mizilla/5.0"}
            res = requests.get(web_address,timeout=(5, 10), headers = headers)
            flag = 1
            break
        except:
            print("retry")
            flag=0
    res.encoding = 'gb2312'
    soup = BeautifulSoup(res.text, features = 'html.parser')      #结构化处理 
    #print(soup)
    
    for element in soup.find_all(name='div',attrs = {'class':'jgsz_right_con'}):
        for info in element.find_all('a'):
            info_title = info.get_text()      #获取通报的标题
            #print(repr(info_title))
            if(info_pattern.match(info_title)):
                return(info.get('href'))
                
info_url = 'http://wsjk.ln.gov.cn/wst_wsjskx' + find_url(liaoning)[1:]
print(info_url)


# In[2]:


def get_data(web_address):
    #获取网页信息
    while(1):
        try:
            headers = {"user-agent": "Mizilla/5.0"}
            res = requests.get(web_address,timeout=2, headers = headers)
            flag=1
            break
        except:
            print("retry")
            flag=0
    res.encoding = 'gb2312'
    soup = BeautifulSoup(res.text, 'html.parser')      #结构化处理
    for element in soup.find_all(name='div',attrs = {'class':'TRS_PreAppend'}):
        print(element.get_text())
        f = open(r"./Data/21.txt", mode ='w', encoding ="utf-8")
        f.write(element.get_text())
        f.close() 
                    
if __name__ == '__main__':
    print('begin')
    get_data(info_url)
    print('finish')
    


# In[2]:








