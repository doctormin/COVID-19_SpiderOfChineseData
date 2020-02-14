#!/usr/bin/env python
# coding: utf-8

# In[3]:


#53
#By Yimin Zhao
import requests
from bs4 import BeautifulSoup
import re

yunnan = 'http://ynswsjkw.yn.gov.cn/wjwWebsite/web/col?id=UU157976428326282067&pId=UU145102906505319731&cn=xxgzbd&pcn=ztlm&pid=UU145102906505319731&page=1'         #卫健委的url
info_pattern = re.compile(r'云南.*新.*冠.*肺炎.*疫情.*情况')  


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
    
    for element in soup.find_all(name='div',attrs = {'class':'theSimilar'}):
        for info in element.find_all('a'):
            info_title = info.get_text()      #获取通报的标题
            if(info_pattern.match(info_title)):
                return(info.get('href'))
                
info_url = 'http://ynswsjkw.yn.gov.cn' + find_url(yunnan)
print(info_url)


# In[4]:


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
    for element in soup.find_all(name='div',attrs = {'id':'content'} ):
        print(element.get_text())
        f = open(r"D:/IIoT/20年寒假-疫情爬虫/Data/53.txt", mode ='w', encoding ="utf-8")
        f.write(element.get_text())
        f.close() 
                    
if __name__ == '__main__':
    print('begin')
    get_data(info_url)
    print('finish')




