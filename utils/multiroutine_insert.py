import time

from utils.ax_db_aiopool import *
from utils.ax_sql import *
from utils.db_config import *

class TestMultiRoutineInsert():
    def __init__(self):
        self.task_obj = None
        pass
           
    async def thread_proc(self,loop,db,item):
        #print("TestMultiRoutineInser,thread_proc,",item)
        name = "xiaoming's name"
        gender = "male"
        price = 1000000000231.23123
        create_time = int(time.time())
        sql_str = "insert into t_test_insert(id,name,gender,price,create_time,extra_str1,extra_str2,extra_int1,extra_int2) values(%s,%s,%s,%s,%s,'','',0,0)"
        (is_exception,resList) = await db.exec_nonquery(loop,sql_str, (item,name,gender,price,create_time))
        if is_exception:
            print("insert error:",is_exception,resList)
 
    def dispatch_tasks(self):
        self.task_obj = AxAsyncDBTaskThread(self.thread_proc,DBLocalMysql)
        task_count = 100000
        for i in range(task_count):
            self.task_obj.post_task((i))

    def query_task_queue_size(self):
        return self.task_obj.query_task_queue_size()

if __name__ == "__main__":
    pass
