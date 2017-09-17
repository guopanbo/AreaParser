
class Logger:
    def __init__(self, level='info'):
        self.logfile = open('../../../log/run.log', 'a',encoding='utf8')
        self.level = level

    def __del__(self):
        self.logfile.flush()
        self.logfile.close()

    def error(self, s):
        if self.logfile and (self.level.lower() == 'error' or self.level.lower() == 'info' or self.level.lower() == 'debug'):
            self.logfile.write('\n[ERROR]%s' % s)
            self.logfile.flush()
        else:
            print('日志配置错误，level=%s' % self.level)

    def info(self, s):
        if self.logfile and (self.level.lower() == 'info' or self.level.lower() == 'debug'):
            self.logfile.write('\n[INFO]%s' % s)
            self.logfile.flush()
        else:
            print('日志配置错误，level=%s' % self.level)

    def debug(self, s):
        if self.logfile and self.level.lower() == 'debug':
            self.logfile.write('\n[DEBUG]%s' % s)
            self.logfile.flush()
        else:
            print('日志配置错误，level=%s' % self.level)