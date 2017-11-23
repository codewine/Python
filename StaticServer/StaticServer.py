#coding:utf-8
import socket
import multiprocessing
import re


HTML_ROOT_DIR = "./html"

class HTTPServer(object):

    #初始化
    def __init__(self):
        self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


    #开启服务器启动进程
    def start(self):
        self.serversocket.listen(128)
        while True:
            clintsocket, addree = self.serversocket.accept()
            hanlderprogess = multiprocessing.Process(target=self.jiexi, args=(clintsocket,))
            hanlderprogess.start()
            clintsocket.close()

    #绑定端口
    def bind(self,port):
        self.serversocket.bind(("127.0.0.1", 5000))


    #获取请求头，进行解析，同时发送相应头
    def jiexi(clserver):
        date = clserver.recv(1024)
        print (date)
        list = str(date).split("\r\n")
        # 解析
        requesthead = list[0]
        print (requesthead)
        #使用正则表达式解析出请求头的文件名称
        file = re.match(r"\w+ +(/[^ ]*) ",requesthead).group(1)

        #对获取的问题名判断，如果是／的就进行显示index.html
        if "/"==file:
            file = "/index.html"
        try:
            f = open(HTML_ROOT_DIR+file,"rb")
        except:
            response_start_line = "HTTP/1.1 200 OK \r\n"
            response_headers = "Server:My server\r\n"
            response_body = "the file not file"
        else:
            file_date = f.readline()
            f.close()
            response_start_line = "HTTP/1.1 200 OK \r\n"
            response_headers = "Server:My server\r\n"
            response_body = file_date.decode("utf-8")

        response = response_start_line+response_headers+"\r\n"+response_body
        print (response)
        clserver.send(bytes(response))
        clserver.close()

def main():
    server  = HTTPServer()
    server.bind(1001)
    server.start()

if __name__=="__main__":
    main()