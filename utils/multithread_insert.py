import time

from utils.ax_db_threadpool import *
from utils.ax_sql import *
from utils.db_config import *

class TestMultiThreadInsert():
    def __init__(self):
        self.task_obj = None
        pass
           
    def thread_proc(self,db,item):
        if item == 0:
            print("thread_proc,",item)
        name = "xiaoming's name"
        gender = "male"
        price = 1000000000231.23123
        create_time = int(time.time())
        sql_str = "insert into t_test_insert(id,name,gender,price,create_time,extra_str1,extra_str2,extra_int1,extra_int2) values(%s,%s,%s,%s,%s,'','',0,0)"
        (is_exception,resList) = db.exec_nonquery(sql_str, (item,name,gender,price,create_time))
        if is_exception:
            print("insert error:",is_exception,resList)
 
    def dispatch_tasks(self):
        self.task_obj = AxDBTaskThread(self.thread_proc,DBLocalMysql,100)
        task_count = 100000
        for i in range(task_count):
            if i == 0:
                print(i)
            self.task_obj.post_task((i))

    def query_task_is_done(self):
        return self.task_obj.query_task_is_done()
if __name__ == "__main__":
    pass
