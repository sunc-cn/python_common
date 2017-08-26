#encoding=utf-8
from queue import Queue,Empty
from threading import Thread
from threading import Event
import time
import asyncio
from utils.ax_sql import *
from utils.ax_aio_sql import *

  

class AxAsyncDBThread(Thread):
    def __init__(self,thread_proc,db_config,loop):
        Thread.__init__(self,target=self.__run)
        self.__loop = loop
        self.__thread_proc_ = thread_proc
        self.__quit_event_ = Event()
        self.setDaemon(True)
        self.__db = AxAsyncMySQL(db_config)

    def get_db_conn(self):
        return self.__db

    def start(self):
        self.__quit_event_.clear()
        Thread.start(self)
        
    def stop(self):
        self.__db.Close()
        self.__quit_event_.set()
    
    def __run(self):
        while True:
            if self.__quit_event_.is_set():
                break
            try:
                asyncio.set_event_loop(self.__loop)
                #conn_task = asyncio.ensure_future(self.__db.connect(self.__loop))
                #self.__loop.run_until_complete(conn_task)
                #print("connect complete")
                #self.__is_connect = True
                self.__loop.run_forever()
            except Exception as e :  
                raise NameError(str(e))

class AxAsyncDBTaskThread():
    def __init__(self,thread_proc,db_config,thread_num = 4):
        self.db_config = db_config
        self.thread_num_ = thread_num
        self.thread_proc_ = thread_proc
        self.task_queue_ = Queue()
        self.thread_list = []
        self.loop_list = []
        self.__init_threads()
        self.__loop_index = 0

    async def __thread_proc(self,loop,db,argv):
        await self.thread_proc_(loop,db,argv)
        self.task_queue_.put(1)
      
    def __get_loop_index(self):
        if self.__loop_index >= len(self.loop_list)-1:
            self.__loop_index = 0
        else:
            self.__loop_index += 1
        return self.__loop_index

    def __init_threads(self):
        for i in range(self.thread_num_):
            i
            m_loop = asyncio.new_event_loop()
            m_thread = AxAsyncDBThread(
                    self.thread_proc_,
                    self.db_config,
                    m_loop)
            #m_thread.__thread_proc_ = None
            m_thread.start()
            self.thread_list.append(m_thread)
            self.loop_list.append(m_loop)
        
    def query_task_queue_size(self):
        return self.task_queue_.qsize()
     
    def task_start(self):
        pass
    
    def task_stop(self):
        for loop in self.loop_list:
            loop.stop()
        for thread in self.thread_list:
            thread.stop()
    
    def post_task(self,argv):
        loop_index = self.__get_loop_index()
        loop = self.loop_list[loop_index]
        db = self.thread_list[loop_index].get_db_conn()
        asyncio.run_coroutine_threadsafe(self.__thread_proc(loop,db,argv), loop) 

