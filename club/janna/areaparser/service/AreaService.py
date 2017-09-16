# --*-- coding:utf-8 --*--
import pymysql.cursors

class AreaService:
    def __init__(self, showSql = False, log = None):
        # 连接数据库
        self.connect = pymysql.Connect(
            host='localhost',
            port=3306,
            user='test',
            passwd='test',
            db='test',
            charset='utf8'
        )
        self.cursor = self.connect.cursor()
        self.saveSql = u'insert into area values(\'%s\', \'%s\', \'%s\', \'%s\');'
        self.getByNameSql = 'select * from area where name like \'%s\''

        self.showSql = showSql
        self.log = log
    '''
    保存区域
    '''
    def save(self, areaEntity):
        if not areaEntity:
            print('参数错误' + areaEntity)
            return False
        sql = self.saveSql % (areaEntity.getCode(), areaEntity.getName(), areaEntity.getPcode(), areaEntity.getUrl())
        if self.showSql:
            print(sql)
        if self.log:
            self.log.write(sql + '\n')
        try:
            self.cursor.execute(sql.encode('utf-8'))
            self.connect.commit()
        except pymysql.err.IntegrityError:
            if self.log:
                self.log.write(sql + '\n')
            print('此区域编码已存在：%s' % areaEntity.getCode())
        return True

    def getByName(self, name):
        if not name:
            print('参数错误' + name)
            return
        self.cursor.execute(self.getByNameSql % name)