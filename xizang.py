#!/usr/bin/env python
# coding: utf-8

# In[3]:


#54
#By Yimin Zhao
import re
from selenium import webdriver

xizang = 'http://wjw.xizang.gov.cn/xwzx/wsjkdt/'         #卫健委的url
info_pattern = re.compile(r'.*西藏.*新.*冠.*疫情.*')

#找到通报疫情的url
driver = webdriver.Chrome()
driver.get(xizang)
nodes = driver.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div/div[2]/ul[1]/li')
for node in nodes:
      title = node.find_element_by_xpath('.//a').text
      print(title)
      if info_pattern.match(title):
        print("matched!")
        info_title = title
        info_url = node.find_element_by_xpath('.//a').get_attribute('href')
        break
driver.get(info_url)
info_content = driver.find_element_by_xpath('/html/body/div[3]/div[3]/div[1]').text.strip()
print(info_content)
f = open(r"D:/IIoT/20年寒假-疫情爬虫/Data/54.txt", mode ='w', encoding ="utf-8")
f.write(info_content)
f.close() 
driver.close()

