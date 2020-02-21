#!/usr/bin/env python
# coding: utf-8

# In[3]:
#32

import re
from selenium import webdriver

driver = webdriver.Chrome() # Switch to Chrome if necessary

# In[4]:


url = 'http://wjw.jiangsu.gov.cn/col/col7290/index.html'
info_pattern = re.compile(r'.*江苏.*病例')
info_url = ''
info_title = ''


# In[5]:


driver.get(url)
nodes = driver.find_elements_by_xpath('//*[@id="222741"]/div/li')
for node in nodes:
    title = node.find_element_by_xpath('a').text.strip()
    if info_pattern.match(title):
        info_title = title
        info_url = node.find_element_by_xpath('a').get_attribute('href')
        break


# In[9]:


driver.get(info_url)
ps = driver.find_elements_by_xpath('//*[@id="barrierfree_container"]/div[6]/div[1]/p')
contents = list(map(lambda p:p.text.strip(), ps))
info_content = '\n'.join(contents)


# In[10]:

print(info_title)
print(info_url)
print(info_content)
f = open(r"../Data/32.txt", mode='w', encoding="utf-8")
f.write(info_content)
f.close()
driver.close()