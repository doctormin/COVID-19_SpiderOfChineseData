#!/usr/bin/env python
# coding: utf-8

# In[23]:
#33
#By Bugen Zhao
import re
from selenium import webdriver
driver = webdriver.Chrome() # Switch to Chrome if necessary
# In[34]:
url = 'http://www.zjwjw.gov.cn/col/col1202101/index.html'
info_pattern = re.compile(r'.*浙江.*新.*冠.*疫情.*情况')
info_url = ''
info_title = ''
# In[35]:
driver.get(url)
nodes = driver.find_elements_by_xpath('//*[@id="4978845"]/div/li')
for node in nodes:
    title = node.find_element_by_xpath('a').text.strip()
    if info_pattern.match(title):
        info_title = title
        info_url = node.find_element_by_xpath('a').get_attribute('href')
        break
# In[36]:
driver.get(info_url)
info_content = driver.find_element_by_xpath('//*[@id="zoom"]').text.strip()
# In[38]:
print(info_title)
print(info_url)
print(info_content)
f = open(r"D:/IIoT/20年寒假-疫情爬虫/Data/33.txt", mode ='w', encoding ="utf-8")
f.write(info_content)
f.close()
driver.close()

