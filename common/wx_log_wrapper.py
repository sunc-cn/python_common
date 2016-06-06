#encoding=utf-8
'''
Created on 2015年1月23日

@author: sunchun
'''

from src.Server.common import  wx_log

class WxLogWrapper():
    def __init__(self,log_name,log_path):
        self.__business_log = wx_log.WxLogger(1,log_name,log_path)
        error_log_name = log_name + "_Error"
        self.__error_log = wx_log.WxLogger(1,error_log_name,log_path)
    
    def logError(self,msg):
        self.__business_log.getlog().error(msg)
        self.__error_log.getlog().error(msg)
    
    def logWarning(self,msg):
        self.__business_log.getlog().warning(msg)
    
    def logInfo(self,msg):
        self.__business_log.getlog().info(msg)
        
    def logDebug(self,msg):
        self.__business_log.getlog().debug(msg)
        

global g_LogObject
g_LogObject = None


def InitLog(log_name,log_path):
    global g_LogObject
    if g_LogObject == None:
        g_LogObject = WxLogWrapper(log_name,log_path)
    else:
        print("log object has initialized")

def logError(msg):
    global g_LogObject
    if g_LogObject == None:
        print("log object is not initalize")
    else:
        g_LogObject.logError(msg)

def logWarning(msg):
    global g_LogObject
    if g_LogObject == None:
        print("log object is not initalize")
    else:
        g_LogObject.logWarning(msg)

def logInfo(msg):
    global g_LogObject
    if g_LogObject == None:
        print("log object is not initalize")
    else:
        g_LogObject.logInfo(msg)
        
def logDebug(msg):
    global g_LogObject
    if g_LogObject == None:
        print("log object is not initalize")
    else:
        g_LogObject.logDebug(msg)
        

if __name__ == "__main__":
    InitLog("log_name", "./")
    
    logDebug("debug_msg")
    logError("error_msg")
    logInfo("this:%d,%s"%(3,"23"))

    


    
    