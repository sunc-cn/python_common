#encoding=utf-8
'''
Created on 2015年8月24日

@author: sunchun
'''
import http.client
import urllib


class WxHttp():
    def __init__(self,svr_url,svr_ip,svr_port):
        self.svr_url_ = svr_url
        self.svr_ip_ = svr_ip
        self.svr_port_ = svr_port

    def send_get_request(self,**args):      
        '''''连接server'''  
        res = ''  
        is_send_succ = False
        str_args = ""
        conn = None
        try:              
            for item in args:
                temp = "%s=%s"%(item,args[item])
                temp = urllib.parse.quote(temp)
                str_args += temp + "&"
            if len(str_args) > 1:
                str_args = str_args[:len(str_args)-1]
            httpRequest = "%s?%s" % (self.svr_url_,str_args)      
            conn = http.client.HTTPConnection(host=self.svr_ip_,port=self.svr_port_)   
            conn.request("GET", httpRequest)   
            service_res = conn.getresponse() 
            if 200 == service_res.status:  
                res = service_res.read(1024)  
                res = repr(res)  
                is_send_succ = True
            else :  
                res = "connect server fail."  
        except Exception as e:  
            res = 'connect server except:%s.' % (e)  
        finally:
            if conn != None:
                conn.close()
            
        return (is_send_succ,res)  
    
    def send_post_request(self,**args):
        res = ''  
        is_send_succ = False
        conn = None
        try:              
            params = urllib.parse.urlencode(args)
            #headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
            conn = http.client.HTTPConnection(host=self.svr_ip_,port=self.svr_port_,timeout=30)   
            conn.request("POST", self.svr_url_, params)
            service_res = conn.getresponse() 
            if 200 == service_res.status:  
                res = service_res.read(1024)  
                res = repr(res)  
                is_send_succ = True
            else :  
                res = "connect server fail."  
        except Exception as e:  
            res = 'connect server except:%s.' % (e)  
        finally:
            if conn != None:
                conn.close()
            
        return (is_send_succ,res)  
    
if __name__ == "__main__"   :
    pass

