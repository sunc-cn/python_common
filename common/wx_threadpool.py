#encoding=utf-8
'''
Created on 2015年1月21日

@author: sunchun
'''
from queue import Queue , Empty
from threading import Thread
from threading import  Event
import time
  

class WxThread(Thread):
    def __init__(self,thread_proc,task_queue):
        Thread.__init__(self,target=self.__run)
        self.__thread_proc_ = thread_proc
        self.__task_queue_ = task_queue
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
                task_argv = self.__task_queue_.get_nowait()
                if task_argv:
                    self.__thread_proc_(task_argv)
                else:
                    self.__thread_proc_()
            except Empty:
                time.sleep(1)
                continue;
            except Exception as e :  
                raise NameError(str(e))

class WxTaskThread():
    def __init__(self,thread_proc,thread_num = 4):
        self.thread_num_ = thread_num
        self.thread_proc_ = thread_proc
        self.task_queue_ = Queue()
        self.thread_list = []
        self.__init_threads()
      
    def __init_threads(self):
        for i in range(self.thread_num_):
            i
            m_thread = WxThread(self.thread_proc_,self.task_queue_)
            #m_thread.__thread_proc_ = None
            m_thread.start()
            self.thread_list.append(m_thread)
        
    def task_start(self):
        pass
    
    def task_stop(self):
        for thread in self.thread_list:
            thread.stop()
    
    def post_task(self,argv):
        self.task_queue_.put((argv))
 
class ThreadTest():
    def __init__(self):
        pass
           
    def thread_proc(self,n_id=0):
        print("contents "  + str(n_id))
 
    def test_case1(self):
        m_task = WxTaskThread(self.thread_proc)
        for i in range(10000):
            m_task.post_task((i))
        #m_task.task_stop()
        
    def run_test(self):
        self.test_case1()
       
if __name__ =="__main__" :
    test = ThreadTest()
    test.run_test()
    while(1):
        time.sleep(10)

            