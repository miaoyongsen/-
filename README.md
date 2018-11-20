# 爬取链家
import requests
from bs4 import BeautifulSoup
#
#page_number = 100
#for i in range(page_number)：

url = 'https://sh.lianjia.com/ershoufang/pg/'
header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Safari/605.1.15'
}
html = requests.get(url,headers = header).text #以文本形式返回网页源代码
#print(html)


soup = BeautifulSoup(html,'html.parser')  #解析器
#print(soup)
infos = soup.find('ul',{'class':'sellListContent'}).find_all('li')
#print(infos)

with open(r'/Users/amiao/Desktop/链家.csv','a',encoding='utf-8') as f:
    num = 1
    for info in infos:
        name = info.find('div',{'class':'title'}).find('a').get_text()
        print(name)
        print = info.find('div',{'class':'priceInfo'}).find('div',{'class':'totalPrice'}).find('span').get
        address = info.find('div',{'class':'address'}).find('div',{'class':'houseInto'}).find('a').get.text()
        f.write("{},{},{}\n".format(name,price,address))
