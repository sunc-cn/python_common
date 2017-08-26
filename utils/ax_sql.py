#encoding=utf-8
import pymysql.cursors

class AxDBConfig():
    def __init__(self):
        self.Host = ""
        self.Port = 0
        self.User = ""
        self.Pwd = ""
        self.DBName = ""

class AxMySQL:
    def __init__(self,cfg=AxDBConfig()):
        self.host = cfg.Host 
        self.port = cfg.Port 
        self.user = cfg.User 
        self.pwd = cfg.Pwd 
        self.db = cfg.DBName
        self.__conn = None

        self.__connect()

    def show(self):
        for n,v in vars(self).items():
            print("%s.%s:%s"%(self.__class__.__name__,n,v))

    def __connect(self):
        if self.db == "":
            raise(NameError,"没有设置数据库信息")
        self.__conn = pymysql.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.pwd,
                database=self.db,
                charset="utf8",
                cursorclass=pymysql.cursors.DictCursor)
        cur = self.__conn.cursor()
        if not cur:
            raise(NameError,"连接数据库失败")


    def close(self):
        if self.__conn != None:
            self.__conn.close()
        self.__conn = None

    def exec_query(self,sql,paras=None):
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
            if self.__conn == None:
                self.__connect()
            cur = self.__conn.cursor()
            if paras == None:
                cur.execute(sql)
            else:
                cur.execute(sql,paras)
            op_result = cur.fetchall()
        except Exception as e:
            op_result = str(e)
            is_exception = True
        return(is_exception,op_result)

    def exec_nonquery(self,sql,paras):
        """
          执行非查询语句
          调用示例:
                 ms = AxMySQL(host="localhost",user="sa",pwd="123456",db="PythonWeiboStatistics")
	            ms.ExecNonQuery("update member set sName='test' where snbid = 'sc_test2' and scardid = '111111'")
        """
        is_exception = False
        op_result = None
        try:        
            if self.__conn == None:
                self.__connect()
            cur = self.__conn.cursor()
            cur.execute(sql,paras)
            self.__conn.commit()
            op_result = cur.rowcount
        except Exception as e:
            op_result = str(e)
            is_exception = True
        return (is_exception,op_result)
    
    def check_config(self):
        (is_exception,op_result) = self.exec_query("select 1")
        (op_result)
        return not is_exception

if __name__ == "__main__":
    pass
