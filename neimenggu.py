#!/usr/bin/env python
# coding: utf-8

# In[1]:


#15
#By Yimin Zhao
import requests
from bs4 import BeautifulSoup
import re

jilin = 'http://wjw.nmg.gov.cn/ztlm/2016n/xxgzbdgrdfyyqfk/yqtb/index.shtml'         #卫健委的url
info_pattern = re.compile(r'.*内蒙古.*新.*疫情.*')  

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
    res.encoding = 'utf-8'
    
    soup = BeautifulSoup(res.text, features = 'html.parser')      #结构化处理 
    for element in soup.find_all(name='div',attrs = {'class':'gjsz_lb_content'}):
        for info in element.find_all('a'):
            info_title = info.get_text().strip()      #获取通报的标题
            if(info_pattern.match(info_title)):
                return(info.get('href'))
           
info_url = 'http://wjw.nmg.gov.cn' + find_url(jilin)
print(info_url)


# In[2]:


def get_data(web_address):
    #获取网页信息
    while(1):
        try:
            headers = {"user-agent": "Mizilla/5.0"}
            res = requests.get(web_address,timeout=(5, 10), headers = headers)
            flag=1
            break
        except:
            print("retry")
            flag=0
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')      #结构化处理
    for element in soup.find_all(name='div',attrs = {'class':'position1-text2'} ):
        print(element.get_text())
        f = open(r"D:/IIoT/20年寒假-疫情爬虫/Data/15.txt", mode ='w', encoding ="utf-8")
        f.write(element.get_text())
        f.close() 
                    
if __name__ == '__main__':
    print('begin')
    get_data(info_url)
    print('finish')


# In[2]:




