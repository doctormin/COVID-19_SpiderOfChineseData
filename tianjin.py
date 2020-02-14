#!/usr/bin/env python
# coding: utf-8

# In[3]:


#12
#By Yimin Zhao
import re
from selenium import webdriver

tianjin = 'http://wsjk.tj.gov.cn/col/col87/index.html'         #卫健委的url
info_pattern1 = re.compile(r'.*天津.*新增.*新.*冠.*')
info_pattern2 = re.compile(r'.*天津.*新.*冠.*疫情.*情况.*')

#找到通报疫情的url
driver = webdriver.Chrome()
driver.get(tianjin)
nodes = driver.find_elements_by_xpath('//*[@id="259"]/div/li')
for node in nodes:
      title = node.find_element_by_xpath('.//a').text
      print(title)
      if info_pattern2.match(title):
        print("matched!")
        info_title = title
        info_url = node.find_element_by_xpath('.//a').get_attribute('href')
        break
driver.get(info_url)
info_content = driver.find_element_by_xpath('//*[@class="page_content Clear"]').text.strip()
print(info_content)
f = open(r"D:/IIoT/20年寒假-疫情爬虫/Data/12.txt", mode ='w', encoding ="utf-8")
f.write(info_content)
f.close()
driver.close()

