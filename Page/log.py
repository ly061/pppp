import sys,time,os,logging
log_path = r"C:\Users\yan.liu\PycharmProjects\pppp\Page"

class Log:

    def __init__(self):
        #文件的命名
        self.logname = os.path.join(log_path,'log.txt')
        self.log = logging.getLogger()
        self.log.setLevel(logging.INFO)
        # 日志输出格式
        # self.formatter = logging.Formatter('[%(asctime)s] - %(filename)s] - %(levelname)s: %(message)s')
        self.formatter = logging.Formatter('%(message)s')

    def __console(self,level,message):
        #创建一个FileHandler, 用于写在本地
        fh = logging.FileHandler(self.logname,'a',encoding ='utf-8')
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        self.log.addHandler(fh)
        #创建一个StreamHandler,用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.log.addHandler(ch)
        if level == 'info':
            self.log.info(message)
        elif level == 'debug':
            self.log.debug(message)
        elif level == 'warning':
            self.log.warning(message)
        elif level == 'error':
            self.log.error(message)
        # 这两行代码是为了避免日志输出重复问题
        self.log.removeHandler(ch)
        self.log.removeHandler(fh)
        # 关闭打开的文件
        fh.close()

    def debug(self, message):
        self.__console('debug', message)

    def info(self, message):
        self.__console('info', message)

    def warning(self, message):
        self.__console('warning', message)

    def error(self, message):
        self.__console('error', message)
