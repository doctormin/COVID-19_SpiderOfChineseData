#!/usr/bin/env python
# coding: utf-8

# In[1]:


#52
#By Yimin Zhao
import re
from selenium import webdriver

tianjin = 'http://www.gzhfpc.gov.cn/xwzx_500663/zwyw/'         #卫健委的url
info_pattern = re.compile(r'.*贵州.*新.*冠.*疫情.*')

driver = webdriver.Chrome()
driver.get(tianjin)
nodes = driver.find_elements_by_xpath('//*[@class="right_list f_r f14"]/dl/dd/ul/li')
for node in nodes:
      title = node.find_element_by_xpath('a').text
      #print(title)
      if info_pattern.match(title):
        #print("matched!")
        info_title = title
        info_url = node.find_element_by_xpath('a').get_attribute('href')
        break
driver.get(info_url)
info_content = driver.find_element_by_xpath('//*[@id="Zoom"]/div').text.strip()
print(info_content)
f = open(r"D:\IIoT\20年寒假-疫情爬虫\Data\52.txt", mode = 'w', encoding = "utf-8")
f.write(info_content)
f.close()
driver.close()

