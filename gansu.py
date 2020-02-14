#!/usr/bin/env python
# coding: utf-8

# In[1]:


#62
#By Yimin Zhao
import re
from selenium import webdriver

gansu = 'http://wsjk.gansu.gov.cn/channel/11218/index.html'         #卫健委的url
info_pattern = re.compile(r'.*甘肃.*新.*冠.*病例.*')

#找到通报疫情的url
driver = webdriver.Chrome()
driver.get(gansu)
nodes = driver.find_elements_by_xpath('/html/body/div[2]/div[2]/div[2]/ul/li')
for node in nodes:
      title = node.find_element_by_xpath('.//a').text
      print(title)
      if info_pattern.match(title):
        print("matched!")
        info_title = title
        info_url = node.find_element_by_xpath('.//a').get_attribute('href')
        break
driver.get(info_url)
info_content = driver.find_element_by_xpath('//*[@id="contents"]').text.strip()
print(info_content)
f = open(r"D:/IIoT/20年寒假-疫情爬虫/Data/62.txt", mode ='w', encoding ="utf-8")
f.write(info_content)
f.close()
driver.close()

