#!/usr/bin/env python
# coding: utf-8

# In[2]:


#65
#By Yimin Zhao
import re
from selenium import webdriver

xinjiang = 'http://www.xjhfpc.gov.cn/ztzl/fkxxgzbdfygz/yqtb.htm'         #卫健委的url
info_pattern = re.compile(r'.*新疆.*新.*冠.*疫情.*')

#找到通报疫情的url
driver = webdriver.Chrome()
driver.get(xinjiang)
nodes = driver.find_elements_by_xpath('//*[@id="fhj2zt1-03"]/div/table/tbody/tr')
for node in nodes:
      title = node.find_element_by_xpath('.//a').text
      print(title)
      if info_pattern.match(title):
        print("matched!")
        info_title = title
        info_url = node.find_element_by_xpath('.//a').get_attribute('href')
        break
driver.get(info_url)
info_content = driver.find_element_by_xpath('//*[@id="vsb_content_1029"]').text.strip()
print(info_content)
f = open(r"D:\IIoT\20年寒假-疫情爬虫\Data\65.txt", mode = 'w', encoding = "utf-8")
f.write(info_content)
f.close() 

