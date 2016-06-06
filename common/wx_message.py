#encoding=utf-8
'''
Created on 2015年1月20日

@author: sunchun
'''

import http.client
import urllib

class WxMessage():
    def __init__(self,svr_url,svr_ip,svr_port):
        self.svr_url_ = svr_url
        self.svr_ip_ = svr_ip
        self.svr_port_ = svr_port

    def send_message(self,phone,message):      
        '''''连接server'''  
        res = ''  
        is_send_succ = False
        try:              
            url_phone   = urllib.parse.quote(phone)
            url_message = urllib.parse.quote(message)
            httpRequest = "%s?iphones=%s&imessage=%s" % (self.svr_url_,url_phone,url_message)      
            conn = http.client.HTTPConnection(host=self.svr_ip_,port=self.svr_port_)   
            conn.request("GET", httpRequest)   
            service_res = conn.getresponse() 
            if 200 == service_res.status:  
                res = service_res.read(1024)  
                res = repr(res)  
                is_send_succ = True
            else :  
                res = "connect server fail."  
            #主动关闭连接
            conn.close()  
        except Exception as e:  
            res = 'connect server except:%s.' % (e)  
            
        return (is_send_succ,res)  
    
    def check_config(self):
        (is_send_succ,res)  = self.send_message("", "测试短信接口")
        res
        return is_send_succ
    
if __name__ == "__main__"   :
    pass
