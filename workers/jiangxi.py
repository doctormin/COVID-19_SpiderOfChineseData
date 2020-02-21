#36
#By Yimin Zhao
import requests
from bs4 import BeautifulSoup
import re

jiangxi = 'http://hc.jiangxi.gov.cn/xwzx/wjxw/'         #卫健委的url
info_pattern = re.compile(r'.*江西省新.*冠.*肺炎.*疫情.*情况')  


#找到通报疫情的url
def find_url(web_address):
    #获取网页信息
    while(1):
        try:
            res = requests.get(web_address,timeout=(5, 10))
            flag = 1
            break
        except:
            print("retry")
            flag=0
    res.encoding = 'utf-8'
    
    soup = BeautifulSoup(res.text, features = 'html.parser')      #结构化处理 

    #print(soup.find_all(name='ul',attrs={'class':'List_list'}))
    for element in soup.find_all(name='ul',attrs = {'class':'List_list'}):
        for info in element.find_all('a'):
            info_title = info.get_text()      #获取通报的标题
            if(info_pattern.match(info_title)):
                return(info.get('href'))
        

        
info_url = 'http://hc.jiangxi.gov.cn'+find_url(jiangxi)
print(info_url)


def get_data(web_address):
    #获取网页信息
    while(1):
        try:
            res = requests.get(web_address,timeout=2)
            flag=1
            break
        except:
            print("retry")
            flag=0
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')      #结构化处理
    for element in soup.find_all(name='div',attrs = {'id':'Zoom'}):
        print(element.get_text())
        f = open(r"./Data/36.txt", mode ='w', encoding ="utf-8")
        f.write(element.get_text())
        f.close() 
                    
if __name__ == '__main__':
    print('begin')
    get_data(info_url)
    print('finish')
    


