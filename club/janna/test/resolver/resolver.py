# --*-- coding:utf-8 --*--

from club.janna.areaparser.resolver.resolver import resolve

'''
测试 resolve
'''
headers = { "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding":"gzip, deflate",
            "Accept-Language":"zh-CN,zh;q=0.8",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36"
            }
resolve('11.html', 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2016/', level=1, pcode = '北京市', headers = headers)