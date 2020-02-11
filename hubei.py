#!/usr/bin/env python
# coding: utf-8

# In[2]:


import re
from selenium import webdriver
hubei = 'http://wjw.hubei.gov.cn/fbjd/dtyw/'         #卫健委的url
info_pattern = re.compile(r'.*湖北.*新.*冠.*疫情.*')
#找到通报疫情的url
driver = webdriver.Chrome()
driver.get(hubei)
print(driver.page_source)
nodes = driver.find_elements_by_xpath('//*[@id="share"]/li')
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

