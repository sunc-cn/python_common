#encoding=utf-8
'''
Created on 2015年1月19日

@author: sunchun
'''

import logging.handlers
#import time

WxLogFormat1 = '%(asctime)s - %(thread)d - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)d  - %(message)s'
WxLogFormat2 = '%(asctime)s - %(thread)d - %(levelname)s - %(message)s'

format_dict = {
   1 : logging.Formatter(WxLogFormat2),
   2 : logging.Formatter(WxLogFormat2),
   3 : logging.Formatter(WxLogFormat2),
   4 : logging.Formatter(WxLogFormat2),
   5 : logging.Formatter(WxLogFormat2)
}

class WxLogger():
    def __init__(self,  loglevel, log_name,log_path="./"):
        '''
           指定保存日志的文件路径，日志级别，以及调用文件
           将日志存入到指定的文件中
        '''
        # 创建一个logger
        self.logger = logging.getLogger(log_name)
        self.logger.setLevel(logging.DEBUG)

        # 创建一个handler，用于写入日志文件
        # 设置文件每天凌晨创建新的
        if len(log_path) == 0:
            log_path = "./"
        if log_path[-1:] != "/":
            log_path += "/"
            
        file_name = log_path + log_name +".log"
        fh = logging.handlers.TimedRotatingFileHandler(file_name,"midnight",1,15)
        fh.suffix = "%Y%m%d.log"
        fh.setLevel(logging.DEBUG)

        # 再创建一个handler，用于输出到控制台
        #ch = logging.StreamHandler()
        #ch.setLevel(logging.DEBUG)

        # 定义handler的输出格式
        #formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        formatter = format_dict[int(loglevel)]
        fh.setFormatter(formatter)
        #ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        #self.logger.addHandler(ch)
    
    def getlog(self):
        return self.logger
    
if __name__ == "__main__":
    log_path="e:"
    m_Log =WxLogger(log_name='Server', loglevel=1,log_path=log_path)
    print(log_path)
    logger = m_Log.getlog()
    logger.info("helloworld")

    logger2 = m_Log.getlog()
    logger2.info("helloworld2")
    logger2.error("this  is a error")
    logger2.warning("this is a waring")
    logger2.debug("msg_debug")

