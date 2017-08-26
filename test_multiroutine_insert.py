#!/usr/local/bin/python3.6
#encoding=utf-8

import sys
from os.path import abspath,join,dirname
sys.path.insert(0,join(abspath(dirname(__file__)),'src'))
import time

from utils.multiroutine_insert import *

if __name__ == "__main__":
    obj = TestMultiRoutineInsert()
    start = time.time()
    obj.dispatch_tasks()
    while(True):
        time.sleep(0.01)
        if 10000 == obj.query_task_queue_size():
            now = time.time()
            cost = now-start
            print("tasks done:",cost)
            break
    pass
