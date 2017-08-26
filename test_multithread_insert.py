#!/usr/local/bin/python3.6
#encoding=utf-8

import sys
from os.path import abspath,join,dirname
sys.path.insert(0,join(abspath(dirname(__file__)),'src'))
import time

from utils.multithread_insert import *

if __name__ == "__main__":
    obj = TestMultiThreadInsert()
    start = time.time()
    obj.dispatch_tasks()
    while(True):
        time.sleep(0.01)
        if obj.query_task_is_done():
            now = time.time()
            cost = now-start
            print("tasks done:",cost)
            break
    pass
