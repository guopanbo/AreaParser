# --*-- coding:utf-8 --*--

from bs4 import BeautifulSoup
from club.janna.areaparser.resolver.resolver import resolve
from club.janna.areaparser.logger.Logger import *
import requests
import time

# 第几轮
r = 1

# 日志
log = Logger('../../../../log/resume%s.log' % r, level='debug')
startTime = time.time()
log.info('-----------------start time: %s---------------------' % time.asctime(time.localtime(startTime)))

# 2016年统计用区划代码
url = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2016/'

startUrl = '46.html'

# 请求头
headers = { "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding":"gzip, deflate",
            "Accept-Language":"zh-CN,zh;q=0.8",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36"
            }
wb_data = requests.get(url, headers = headers)

soup = BeautifulSoup(wb_data.content, 'lxml')
wb_data.close()

def indexof(indexs, url):
    if not indexs:
        return 0
    for i in range(len(indexs)):
        if indexs[i]['url'] == url:
            return i
    return 0
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

# 需要重新解析的地区列表
indexs = indexs[indexof(indexs, startUrl):len(indexs)]
try:
    for index in indexs:
        resolve(index['url'], url, level=1, pcode=index['name'], headers=headers, log=log)
except RuntimeError as re:
    print(re)
    log.error(re)
    log.error('程序出错退出！')
    print('程序出错退出！')
else:
    print('解析完毕！')
    endTime = time.time()
    log.info('-----------------end time: %s---------------------' % time.asctime(time.localtime(endTime)))
    print('用时 %f 秒' % ((endTime - startTime) / 1000.0))