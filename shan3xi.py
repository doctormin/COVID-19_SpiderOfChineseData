#61
#By Yimin Zhao
import requests
import re
from selenium import webdriver

shan3xi = 'http://sxwjw.shaanxi.gov.cn/col/col9/index.html'         #卫健委的url
info_pattern = re.compile(r'陕西新增.*例新.*累计.*')  

driver = webdriver.Chrome()
driver.get(shan3xi)
nodes = driver.find_elements_by_xpath('//*[@id="572"]/div/li')
for node in nodes:
      title = node.find_element_by_xpath('a').text
      print(title)
      if info_pattern.match(title):
        print("matched!")
        info_title = title
        info_url = node.find_element_by_xpath('a').get_attribute('href')
        break
driver.get(info_url)
info_content = driver.find_element_by_xpath('//*[@id="zoom"]').text.strip()
print(info_content)
f = open(r"D:\IIoT\20年寒假-疫情爬虫\Data\61.txt", mode = 'w', encoding = "utf-8")
f.write(info_content)
f.close()
driver.close()

