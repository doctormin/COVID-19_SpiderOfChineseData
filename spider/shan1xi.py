#!/usr/bin/env python
# coding: utf-8

# In[1]:


#14
#By Yimin Zhao
import requests
from bs4 import BeautifulSoup
import re
shan1xi = 'http://wjw.shanxi.gov.cn/xingfew/index.hrh'         #卫健委的url
info_pattern = re.compile(r'.*山西.*新.*冠.*疫情.*情况.*')  

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
    
    for element in soup.find_all(name='div',attrs = {'class':'demo-right'}):
        for info in element.find_all('a'):
            info_title = info.get_text().strip()
            print(info_title)#获取通报的标题
            if(info_pattern.match(info_title)):
                return(info.get('href'))
                
info_url = find_url(shan1xi)
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
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')      #结构化处理
    for element in soup.find_all(name='div',attrs = {'class':'ze-art'}):
        print(element.get_text())
        f = open(r"/Data/14.txt", mode ='w', encoding ="utf-8")
        f.write(element.get_text())
        f.close() 
                    
if __name__ == '__main__':
    print('begin')
    get_data(info_url)
    print('finish')
    


# In[2]:





