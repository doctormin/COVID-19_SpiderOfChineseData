#!/usr/bin/env python
# coding: utf-8
#11
#By Yimin Zhao
import requests
from bs4 import BeautifulSoup
import re
from selenium import webdriver

beijing = 'http://wjw.beijing.gov.cn/xwzx_20031/wnxw/'         #卫健委的url
info_pattern1 = re.compile(r'.*北京.*新.*冠.*疫情通报.*')  
info_pattern2 = re.compile(r'.*新增.*例.*')
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
    #print(soup)
    for element in soup.find_all(name='div',attrs = {'class':'weinei_left_con'}):
        for info in element.find_all('a'):
            info_title = info.get_text()      #获取通报的标题
            print(repr(info_title))
            if info_pattern1.match(info_title.strip()) or info_pattern2.match(info_title.strip()):
                return info.get('href')
                
info_url = 'http://wjw.beijing.gov.cn/xwzx_20031/wnxw' + find_url(beijing)[1:]
print(info_url)


# In[2]:


def get_data(web_address):
    #获取网页信息
    driver = webdriver.Chrome()
    driver.get(info_url)
    info_content = driver.find_element_by_xpath('//*[@id="zoom"]/div').text.strip()
    print(info_content)
    f = open(r"/Data/11.txt", mode ='w', encoding ="utf-8")
    f.write(info_content)
    f.close()
    driver.close()
                    
if __name__ == '__main__':
    print('begin')
    get_data(info_url)
    print('finish')
    






