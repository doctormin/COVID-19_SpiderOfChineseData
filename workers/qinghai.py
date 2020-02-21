#!/usr/bin/env python
# coding: utf-8
#63
# In[2]:
#qinghai
#By Yimin Zhao
import requests
from bs4 import BeautifulSoup
import re
from selenium import webdriver

qinghai = 'https://wsjkw.qinghai.gov.cn/zhxw/xwzx/index.html'         #卫健委的url
info_pattern = re.compile(r'.*青海.*新.*冠.*疫情情况')

#找到通报疫情的url
driver = webdriver.Chrome()
driver.get(qinghai)
nodes = driver.find_elements_by_xpath('/html/body/div[2]/div/div/div[1]/div[2]/div[2]/ul/li')
for node in nodes:
      title = node.find_element_by_xpath('./a[2]').text
      print(title)
      if info_pattern.match(title.strip()):
        print("matched!")
        info_title = title
        info_url = node.find_element_by_xpath('./a[2]').get_attribute('href')
        break
driver.get(info_url)
info_content = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/table/tbody/tr[2]/td').text.strip()
print(info_content)
f = open(r"./Data/63.txt", mode = 'w', encoding = "utf-8")
f.write(info_content)
f.close()
driver.close()





