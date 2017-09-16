# --*-- coding:utf-8 --*--

'''
区域实体类
'''
class AreaEntity:
    def __init__(self, code, name, pcode, url):
        self.code = code
        self.name = name
        self.pcode = pcode
        self.url = url

    def getCode(self):
        return self.code

    def getName(self):
        return self.name

    def getPcode(self):
        return self.pcode

    def getUrl(self):
        return self.url