#encoding=utf-8
from queue import Queue,Empty
from threading import Thread
from threading import Event
import time
from utils.ax_sql import *
  

class AxDBThread(Thread):
    def __init__(self,thread_proc,task_queue,db_config):
        Thread.__init__(self,target=self.__run)
        self.__thread_proc_ = thread_proc
        self.__task_queue_ = task_queue
        self.__quit_event_ = Event()
        self.setDaemon(True)
        self.__thread_busy = False
        
        self.__db = AxMySQL(db_config)
        if not self.__db.check_config():
            self.__db.show()
            raise NameError("check_config failed")

    def is_busy(self):
        return self.__thread_busy
        
    def start(self):
        self.__quit_event_.clear()
        Thread.start(self)
        
    def stop(self):
        self.__db.Close()
        self.__quit_event_.set()
        #Thread.join()
    
    def __run(self):
        while True:
            if self.__quit_event_.is_set():
                break
            try:
                task_argv = self.__task_queue_.get_nowait()
                self.__thread_busy = True
                self.__thread_proc_(self.__db,task_argv)
            except Empty:
                self.__thread_busy = False
                time.sleep(1)
                continue;
            except Exception as e :  
                raise NameError(str(e))

class AxDBTaskThread():
    def __init__(self,thread_proc,db_config,thread_num = 4):
        self.db_config = db_config
        self.thread_num_ = thread_num
        self.thread_proc_ = thread_proc
        self.task_queue_ = Queue()
        self.thread_list = []
        self.__init_threads()
      
    def __init_threads(self):
        for i in range(self.thread_num_):
            i
            m_thread = AxDBThread(
                    self.thread_proc_,
                    self.task_queue_,
                    self.db_config)
            #m_thread.__thread_proc_ = None
            m_thread.start()
            self.thread_list.append(m_thread)
        
    def query_task_queue_size(self):
        return self.task_queue_.qsize()
     
    def __check_threads_busy(self):
        for t in self.thread_list:
            if t.is_busy():
                return True
        return False

    def query_task_is_done(self):
        if self.query_task_queue_size() > 0:
            return False
        if self.__check_threads_busy():
            return False
        return True
    
    def task_start(self):
        pass
    
    def task_stop(self):
        for thread in self.thread_list:
            thread.stop()
    
    def post_task(self,argv):
        print("argv,",argv)
        self.task_queue_.put((argv))
 
class ThreadTest():
    def __init__(self):
        pass
           
    def thread_proc(self,n_id=0):
        print("contents "  + str(n_id))
 
    def test_case1(self):
        db_config = AxDBConfig()
        m_task = AxDBTaskThread(self.thread_proc,db_config)
        for i in range(10000):
            m_task.post_task((i))
        #m_task.task_stop()
        
    def run_test(self):
        self.test_case1()
            
