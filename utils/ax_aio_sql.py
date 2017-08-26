#encoding=utf-8
import asyncio
import aiomysql 
from utils.ax_sql import *


class AxAsyncMySQL:
    def __init__(self,cfg=AxDBConfig()):
        self.host = cfg.Host 
        self.port = cfg.Port 
        self.user = cfg.User 
        self.pwd = cfg.Pwd 
        self.db = cfg.DBName

    def show(self):
        for n,v in vars(self).items():
            print("%s.%s:%s"%(self.__class__.__name__,n,v))

    async def __connect(self,loop):
        if self.db == "":
            raise(NameError,"没有设置数据库信息")
        conn = await aiomysql.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.pwd,
                db=self.db,
                charset="utf8",
                autocommit=False,
                loop=loop)
        #print("__connect,over")
        return conn

    def close(self):
        pass

    async def exec_query(self,loop,sql,paras=None):
        """
        执行查询语句
        返回结果为（是否发生异常，发生异常则为异常描述，无异常则是结果集返回）
        调用示例：
                ms = AxMySQL(host="localhost",user="sa",pwd="123456",db="PythonWeiboStatistics")
                (is_exception,resList) = ms.ExecQuery("SELECT id,NickName FROM WeiBoUser")
                if  not is_exception:
                    for (id,NickName) in resList:
                        print str(id),NickName
        """
        is_exception = False
        op_result = None
        try:
            conn = await self.__connect(loop)
            cur = await conn.cursor()
            if paras == None:
                await cur.execute(sql)
            else:
                await cur.execute(sql,paras)
            op_result = await cur.fetchall()
        except Exception as e:
            op_result = str(e)
            is_exception = True
        if conn != None:
            conn.close()
        return(is_exception,op_result)

    async def exec_nonquery(self,loop,sql,paras):
        """
          执行非查询语句
          调用示例:
                 ms = AxMySQL(host="localhost",user="sa",pwd="123456",db="PythonWeiboStatistics")
	            ms.ExecNonQuery("update member set sName='test' where snbid = 'sc_test2' and scardid = '111111'")
        """
        is_exception = False
        op_result = None
        try:        
            #print("exec_nonquery,sql:",sql)
            conn = await self.__connect(loop)
            cur = await conn.cursor()
            await cur.execute(sql,paras)
            await conn.commit()
            op_result = cur.rowcount
            await cur.close()
        except Exception as e:
            op_result = str(e)
            is_exception = True
        if conn != None:
            conn.close()
        return (is_exception,op_result)

if __name__ == "__main__":
    pass
