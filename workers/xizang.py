#!/usr/bin/env python
# coding: utf-8

# In[3]:


# 54
# By Yimin Zhao
import re
from selenium import webdriver

xizang = 'http://wjw.xizang.gov.cn/xwzx/wsjkdt/'  # 卫健委的url
info_pattern = re.compile(r'.*西藏.*新.*冠.*疫情.*')

# 找到通报疫情的url
driver = webdriver.Chrome()
driver.get(xizang)  # /html/body/div[2]/div/div[2]/div[2]/div/div[2]/ul[1]/li
nodes = driver.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div/div[2]/ul')
is_matched = False
for node1 in nodes:
    lis = node1.find_elements_by_xpath('.//li')
    for node in lis:
        title = node.find_element_by_xpath('.//a').text
        print(title)
        if info_pattern.match(title):
            print("matched!")
            is_matched = True
            info_title = title
            info_url = node.find_element_by_xpath('.//a').get_attribute('href')
            break
    if is_matched:
        break
driver.get(info_url)
info_content = driver.find_element_by_xpath('/html/body/div[3]/div[3]/div[1]').text.strip()
print(info_content)
f = open(r"./Data/54.txt", mode='w', encoding="utf-8")
f.write(info_content)
f.close()
driver.close()
