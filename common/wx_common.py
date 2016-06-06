#encoding=utf-8
'''
Created on 2015年4月23日

@author: sunchun
'''

import os.path
import shutil
import zipfile 
import time
import sys

#递归遍历出rootDir下所有文件
def list_all_file(rootDir,all_file): 
    if not os.path.exists(rootDir) or not os.path.isdir(rootDir):
        return False
    try:
        for lists in os.listdir(rootDir): 
            path = os.path.join(rootDir, lists) 
            all_file.append(path)
            if os.path.isdir(path): 
                list_all_file(path,all_file) 
    except Exception as e:
        print(e)
        return False
    return True
            
#解压zip文件 
def unzip(source_zip,target_dir = os.getcwd()):  
    if len(target_dir) <= 0:
        return False
    if target_dir[len(target_dir) - 1] != "\\" or target_dir[len(target_dir) - 1] != "/" :
        target_dir += "\\"
    try:
        myzip=zipfile.ZipFile(source_zip) 
        myfilelist=myzip.namelist() 
        for name in myfilelist: 
            f_handle=open(target_dir+name,"wb") 
            f_handle.write(myzip.read(name))       
            f_handle.close() 
        myzip.close() 
    except Exception as e:
        print(e)
        return False
    return True

#删除文件
def del_file(file_path):
    if not os.path.isfile(file_path):
        return False
    try:
        os.remove(file_path)
    except Exception as e:
        print(e)
        return False
    return True

#拷贝文件
def copy_file(src_path,dest_dir):
    if not os.path.exists(dest_dir) or not os.path.isdir(dest_dir):
        return False
    if not os.path.exists(src_path) or not os.path.isfile(src_path):
        return False
    try:
        shutil.copy(src_path, dest_dir)
    except Exception as e:
        print(e)
        return False
    return True

#文件重命名
def rename_file(src_path,new_name):
    if not os.path.exists(src_path) or not os.path.isfile(src_path):
        return False
    try:
        os.rename(src_path, new_name)
    except Exception as e:
        print(e)
        return False
    return True

def create_dir(dest_dir):
    try:
        os.makedirs(dest_dir)
    except Exception as e:
        print(e)
        return False
    return True

#删除文件夹
def del_dir(src_dir):
    '''delete files and folders'''
    if os.path.isfile(src_dir):
        try:
            os.remove(src_dir)
        except:
            pass
    elif os.path.isdir(src_dir):
        for item in os.listdir(src_dir):
            itemsrc=os.path.join(src_dir,item)
            del_dir(itemsrc) 
        try:
            os.rmdir(src_dir)
        except:
            pass

#获取年月日时间字符串
def get_ymd_timestr(time_format = "%Y-%m-%d"):
    local_time = time.localtime(time.time())
    return time.strftime(time_format,local_time)

#获取是时分秒时间字符串
def get_hms_timestr(time_format = "%H-%M-%S"):
    local_time = time.localtime(time.time())
    return time.strftime(time_format,local_time)

#获取文件名
def get_file_name(file_path):
    file_name = ""
    try:
        file_name = os.path.basename(file_path)
    except Exception as e:
        print(e)
    return file_name

#获取文件上层路径
def get_file_dir_path(file_path):
    file_dir = ""
    try:
        file_dir = os.path.dirname(file_path)
    except Exception as e:
        print(e)
    return file_dir

def hexstrtoint(hex_str):
    return int(hex_str,16)

def str_replace_all(src_str,old_str,new_str):
    count = src_str.count(old_str)
    dest_str = src_str.replace(old_str, new_str, count) 
    return dest_str

def get_file_modified_time(file_path):
    try:
        return os.path.getmtime(file_path)
    except Exception as e:
        print("get_file_modified_time,exception:%s"%(e))
        return 0
def get_last_modified_file_in_dir(dir_path):
    if not os.path.isdir(dir_path):
        return ""
    all_file_and_dir = []
    list_all_file(dir_path,all_file_and_dir)
    all_file = []
    for file in all_file_and_dir:
        if os.path.isfile(file):
            m_time = get_file_modified_time(file) 
            all_file.append((file,m_time))
    ret_slice = sorted(all_file,key=lambda item:item[1],reverse=1)
    if len(ret_slice) == 0:
        return ""
    return ret_slice[0][0]

    
if __name__ == "__main__":
   print(get_last_modified_file_in_dir("/tmp/test")) 
