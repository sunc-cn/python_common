#encoding=utf-8
'''
Created on 2015年1月22日

@author: sunchun
'''

import pymssql

class WxMSSQL:
    def __init__(self,host,user,pwd,db):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db

    def __GetConnect(self):
        """
        得到连接信息
        返回: conn.cursor()
        """
        if not self.db:
            raise(NameError,"没有设置数据库信息")
        self.conn = pymssql.connect(host=self.host,user=self.user,password=self.pwd,database=self.db,charset="utf8")
        cur = self.conn.cursor()
        if not cur:
            raise(NameError,"连接数据库失败")
        else:
            return cur

    def ExecQuery(self,sql):
        """
        执行查询语句
        返回结果为（是否发生异常，发生异常则为异常描述，无异常则是结果集返回）
        调用示例：
                ms = WxMSSQL(host="localhost",user="sa",pwd="123456",db="PythonWeiboStatistics")
                (is_exception,resList) = ms.ExecQuery("SELECT id,NickName FROM WeiBoUser")
                if  not is_exception:
                    for (id,NickName) in resList:
                        print str(id),NickName
        """
        is_exception = False
        op_result = None
        try:
            cur = self.__GetConnect()
            cur.execute(sql)
            op_result = cur.fetchall()
            #查询完毕后必须关闭连接
            self.conn.close()
        except Exception as e:
            op_result = str(e)
            is_exception = True
        return(is_exception,op_result)

    def ExecNonQuery(self,sql):
        """
          执行非查询语句
          调用示例:
                 ms = WxMSSQL(host="localhost",user="sa",pwd="123456",db="PythonWeiboStatistics")
	            ms.ExecNonQuery("update member set sName='test' where snbid = 'sc_test2' and scardid = '111111'")
        """
        is_exception = False
        op_result = None
        try:        
            cur = self.__GetConnect()
            cur.execute(sql)
            self.conn.commit()
            op_result = cur.rowcount
            self.conn.close()
        except Exception as e:
            op_result = str(e)
            is_exception = True
        return (is_exception,op_result)
    
    def Check_Config(self):
        (is_exception,op_result) = self.ExecQuery("select 1")
        op_result
        return not is_exception

if __name__ == "__main__":
    pass
