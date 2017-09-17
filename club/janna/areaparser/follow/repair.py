from bs4 import BeautifulSoup
from club.janna.areaparser.resolver.resolver import resolve
from club.janna.areaparser.logger.Logger import *
import time

# 轮数
r = 2

# 日志
log = Logger('../../../../log/repair%s.log' % r, level='debug')
startTime = time.time()
log.info('-----------------start time: %s---------------------' % time.asctime(time.localtime(startTime)))

# 请求头
headers = { "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding":"gzip, deflate",
            "Accept-Language":"zh-CN,zh;q=0.8",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36"
            }
# 2016年统计用区划代码
baseUrl = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2016/'

def repair(errorpoint, baseUrl, headers, log):
    if not errorpoint:
        log.error('errorpoint=%s' % errorpoint)
        return
    # print(errorpoint)
    url = errorpoint.replace(baseUrl, '', 1)
    urlArr = url.split('/')
    level = len(urlArr)
    basePath = ''
    if level > 2:
        for i in range(level - 2):
            basePath += urlArr[i]
            basePath += '/'
    if basePath:
        url = url.replace(basePath, '', 1)
    resolve(url, baseUrl, level=level, pcode='repair', headers=headers, basePath=basePath, log=log)

data = open('../../../../data/error%s.data' % r, 'r', encoding='utf8')

while True:
    line = data.readline()
    if not line:
        print('处理完毕！')
        endTime = time.time()
        log.info('-----------------end time: %s---------------------' % time.asctime(time.localtime(endTime)))
        print('用时 %f 秒' % ((endTime - startTime) / 1000.0))
        break
    try:
        url = line[line.index('url='):len(line) - 1].replace('url=', '', 1)
    except ValueError:
        print('解析url出错line=%s' % line)
        log.error('解析url出错line=%s' % line)
    repair(url, baseUrl, headers, log)