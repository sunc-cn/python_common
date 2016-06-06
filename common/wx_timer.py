#encoding=utf-8
'''
Created on 2015年1月19日

主要实现对定时器的封装

@author: sunchun
'''

from threading import Thread
from threading import  Event
import time
 
class WxTimer(Thread):
    #参数1：回调函数
    #参数2：定时时间单位秒
    #参数3:是否立即执行    
    def __init__(self,function,interval=0,is_immediate=False):
        Thread.__init__(self,target=self.__run)
        self.__function = function
        self.__interval = interval
        self.__is_immediate = is_immediate
        self.__quit_event_ = Event()
        self.setDaemon(True)
        
    def start(self):
        self.__quit_event_.clear()
        Thread.start(self)
        
    def stop(self):
        self.__quit_event_.set()
        #Thread.join()
    
    def __run(self):
        while True:
            if self.__quit_event_.is_set():
                break
            try:
                if not self.__is_immediate:
                    time.sleep(self.__interval)
                    self.__function()
                else:
                    self.__function()
                    time.sleep(self.__interval)
            except Exception as e :
                raise NameError(str(e))
        print('timer quit,timer thread id is' + str(Thread.ident(self)))
    
class Timer_Test():
    def  __init__(self):
        pass
    
    def __del__(self):
        pass
    
    def on_timer(self):
        curr_time = time.strftime("%Y-%m-%d %H:%M:%S")
        print(curr_time)
        
    def test_case1(self):
        m_timer =   WxTimer(self.on_timer,5,True)
        m_timer.start()
        
    def run_test(self):
        self.test_case1()

def on_timer():
    curr_time = time.strftime("%Y-%m-%d %H:%M:%S")
    print(curr_time)
    
if __name__ == "__main__":
    m_test_timer = Timer_Test()
    m_test_timer.run_test()
    while(1):
        time.sleep(1)




