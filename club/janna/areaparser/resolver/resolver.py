# --*-- coding:utf-8 --*--
import requests
from bs4 import BeautifulSoup
from club.janna.areaparser.entity.AreaEntity import *
from club.janna.areaparser.service.AreaService import *
import urllib3
import time

'''
解析器
'''
def resolve(url, baseUrl, level = 0, pcode = '', headers={}, basePath='',log=None):
    if not url or not baseUrl:
        log.error('没有下一级区域了,url=%s, pcode=%s' % (url, pcode))
        return
    # areaService = AreaService()
    remoteUrl = baseUrl + basePath + url
    try:
        time.sleep(0.1)
        wb_data = requests.get(remoteUrl, headers=headers, timeout=30)
    except (requests.exceptions.Timeout, requests.exceptions.ConnectionError):
        log.error('请求超时！url=%s' % remoteUrl)
        time.sleep(30)
        return
    except (urllib3.exceptions.MaxRetryError, urllib3.exceptions.NewConnectionError):
        log.error('重试测试过多，请求失败！url=%s' % remoteUrl)
        time.sleep(30)
        return
    if wb_data.status_code != 200:
        log.error('访问地址错误！url=%s' % remoteUrl)
        return
    soup = BeautifulSoup(wb_data.content, 'lxml')
    wb_data.close()
    areaList = soup.select('body > table:nth-of-type(2) > tbody > tr:nth-of-type(1) > td > table > tbody > tr:nth-of-type(2) > td > table > tbody > tr > td > table > tr.%s' % getClassNameByLevel(level))
    areas = resolveAreaList(areaList, log)
    # print(areas)
    areaService = AreaService(showSql=True, log=log)
    for area in areas:
        if area:
            areaService.save(AreaEntity(area['code'], area['name'], pcode, remoteUrl))
            if level < 4:
                # level + 1 > 2, 当大于二级时，basepath改变
                if level > 1:
                    cBasePath = url[0 : url.index('/') + 1]
                else:
                    cBasePath = ''
                resolve(area['url'], baseUrl , level + 1, area['code'], headers, basePath = basePath + cBasePath, log=log)


def resolveAreaList(areaList, log):
    areas = []
    for area in areaList:
        areaAs = area.select('td > a')
        if areaAs and len(areaAs) == 2:
            areas.append({
                'url': areaAs[0].get('href'),
                'code': areaAs[0].text,
                'name': areaAs[1].text
            })
        else:
           areaAs = area.select('td')
           if areaAs and len(areaAs) == 3:
               areas.append({
                   'code': areaAs[0].text,
                   'name': areaAs[2].text
               })
           else:
               if log:
                  log.error('解析错误，格式不对：area=%s' % area)
               print('解析错误，格式不对：area=%s' % area)
    return areas

'''
根据级别获取css类
'''
def getClassNameByLevel(level):
    if level == 0:
        return 'provincetr'
    elif level == 1:
        return 'citytr'
    elif level == 2:
        return 'countytr'
    elif level == 3:
        return 'towntr'
    elif level == 4:
        return 'villagetr'
    else:
        return ''
