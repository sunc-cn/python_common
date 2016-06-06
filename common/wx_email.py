#encoding=utf-8
'''
Created on 2015年1月19日

@author: sunchun
'''

import smtplib  
from email.mime.text import MIMEText

class WxMail():
    def __init__(self,mail_host,mail_user,mail_pwd,mail_postfix="xx.com"):
        self.mail_host_ = mail_host
        self.mail_user_ = mail_user
        self.mail_pwd_ = mail_pwd
        self.mail_postfix_ = mail_postfix
        pass
    
    def __del__(self):
        pass
    
    def send_mail(self,to_list,sub,contents):
            me="<"+self.mail_user_+"@"+self.mail_postfix_+">"  
            msg = MIMEText(contents,_subtype='plain',_charset='gb18030')  
            msg['Subject'] = sub  
            msg['From'] = me  
            msg['To'] = ";".join(to_list)
            try:  
                server = smtplib.SMTP()  
                server.connect(self.mail_host_)  
                server.login(self.mail_user_,self.mail_pwd_)  
                server.sendmail(me, to_list, msg.as_string())  
                server.close()  
                return (True,"")
            except Exception as e:  
                error_discription = ( str(e)) 
                return (False,error_discription)
      
    def check_config(self):
        self_addr = self.mail_user_+"@"+self.mail_postfix_
        to_list = []
        to_list.append(self_addr)
        (send_result,error_discription) = self.send_mail(to_list, "启动时测试", "向自己发送一封邮件用于测试自身参数配置是否正确")
        error_discription
        return send_result
            
if __name__ == "__main__":
    pass
