#!/usr/bin/env python
# coding: utf-8

# In[2]:
#31
#By Yimin Zhao
import requests
from bs4 import BeautifulSoup
import re
from selenium import webdriver
shanghai = 'http://wsjkw.sh.gov.cn/xwfb/index.html'         #卫健委的url
info_pattern1 = re.compile(r'.*新增.*例.*')
info_pattern2 = re.compile(r'.*例.*出院.*')
info_pattern3 = re.compile(r'.*上海公布.*病例.*')

#找到通报疫情的url
driver = webdriver.Chrome()
driver.get(shanghai)
print(driver.page_source)
nodes = driver.find_elements_by_xpath('//*[@id="main"]/div[2]/div/ul')
for node in nodes:
      title = node.find_element_by_xpath('a').text
      print(title)
      if info_pattern1.match(title.strip()) or info_pattern2.match(title.strip()) or info_pattern3.match(title.strip()):
        print("matched!")
        info_title = title
        info_url = node.find_element_by_xpath('a').get_attribute('href')
        break
driver.get(info_url)
info_content = driver.find_element_by_xpath('//*[@class="page_content Clear"]').text.strip()
print(info_content)
f = open(r"./Data/31.txt", mode = 'w', encoding = "utf-8")
f.write(info_content)
f.close()
driver.close()





