#encoding=utf-8
'''
Created on 2015年8月24日

@author: sunchun
'''
import os  
import sys  
import time  
  
class WxTail(object):  
    ''''' Represents a tail command. '''  
    def __init__(self):  
        self.__tailed_file = "" 
        self.__callback = sys.stdout.write  
        self.__is_stop = False
  
    def start(self,tailed_file,wait_time=1):  
        ''''' Do a tail follow. If a callback function is registered it is called with every new line. 
        Else printed to standard out. 
 
        Arguments: 
            s - Number of seconds to wait between each iteration; Defaults to 1. '''  
        self.__is_stop = False
        self.check_file_validity(tailed_file)
        self.__tailed_file = tailed_file
        with open(self.__tailed_file) as file_:  
            # Go to the end of file  
            file_.seek(0,2)  
            while not self.__is_stop:  
                curr_position = file_.tell()  
                line = file_.readline()  
                if not line:  
                    file_.seek(curr_position)  
                else:  
                    self.__callback(line)  
                time.sleep(wait_time)  
    
    def stop(self):
        self.__is_stop = True

    def register_callback(self, func):  
        ''''' Overrides default callback function to provided function. '''  
        self.__callback = func  
  
    def check_file_validity(self, file_):  
        ''''' Check whether the a given file exists, readable and is a file '''  
        if not os.access(file_, os.F_OK):  
            raise WxTailError("File '%s' does not exist" % (file_))  
        if not os.access(file_, os.R_OK):  
            raise WxTailError("File '%s' not readable" % (file_))  
        if os.path.isdir(file_):  
            raise WxTailError("File '%s' is a directory" % (file_))  
  
class WxTailError(Exception):  
    def __init__(self, msg):  
        Exception.__init__()
        self.message = msg  
    def __str__(self):  
        return self.message  


if __name__ == "__main__":
    pass
