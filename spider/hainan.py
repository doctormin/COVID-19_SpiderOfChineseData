#!/usr/bin/env python
# coding: utf-8

# In[3]:


#46
#By Yimin Zhao
import requests
from bs4 import BeautifulSoup
import urllib.request
import xlsxwriter
import time
import re

hainan = 'http://wst.hainan.gov.cn/yqfk/'         #卫健委的url

def get_data(info_url):
     #获取网页信息
    while(1):
        try:
            res = requests.get(info_url,timeout=2)
            flag=1
            break
        except:
            print("retry")
            flag=0
    res.encoding = 'utf-8'
    f = open(r"/Data/46.txt", mode ='w', encoding ="utf-8")
    soup = BeautifulSoup(res.text, 'html.parser')      #结构化处理
    for elements in soup.find_all(name = 'cite'):
        print(elements.get_text())
        f.write(elements.get_text())
        f.write("\n")
    f.write("\n从上到下分别是确诊人数、重症人数、死亡人数、出院人数")
    f.close()
    '''
    for elements in soup.find_all(name = 'a',attrs = {'class':'x-admin-backlog-body-center'}):
        info = elements.find_all(name = 'cite')
        print(elements.find_all(name = 'h3'))
        if(type == '确诊人数'): quezheng = info.get_text()
        if(type == '重症人数'): zhongzheng = info.get_text() 
        if(type == '死亡人数'): siwang = info.get_text()
        if(type == '出院人数'): chuyuan = info.get_text()
    #print(quezheng, zhongzheng, siwang, chuyuan)
    '''
if __name__ == '__main__':
    print('begin')
    get_data(hainan)
    print('从上到下分别是确诊人数、重症人数、死亡人数、出院人数')
    print('finish')


# In[3]:





# In[3]:




