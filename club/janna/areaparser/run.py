from bs4 import BeautifulSoup
import requests

'''
2016年统计用区划代码
'''
url = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2016/'
'''
请求头
'''
headers = { "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding":"gzip, deflate",
            "Accept-Language":"zh-CN,zh;q=0.8",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36"
            }
wb_data = requests.get(url, headers = headers)

soup = BeautifulSoup(wb_data.content, 'lxml')
'''
选择目录（首页的超链接）
'''
areaIndexs = soup.select('body > table:nth-of-type(2) > tbody > tr:nth-of-type(1) > td > table > tbody > tr:nth-of-type(2) > td > table > tbody > tr > td > table > tr.provincetr > td > a')

# print(areaIndexs)

indexs = []
for areaIndex in areaIndexs:
    data = {
        'url': areaIndex.get("href"),
        'name': areaIndex.text
    }
    indexs.append(data)

print(indexs)