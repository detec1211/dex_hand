import sys
from socket import *
import threading
import src 



# connect to server

host_ip = "127.0.0.1"#接收灵巧手信息的本地IP
host_port = 55555
sock = socket(AF_INET, SOCK_STREAM)
sock.connect((host_ip, host_port))
sock_pub = socket(AF_INET,SOCK_STREAM)
sock_pub.bind(('127.0.0.1',1234))#更换为控制端Ip
sock_pub.listen(5)
sock_pub_conn,add = sock_pub.accept()
frame_read_worker_i = src.frame_read_worker(sock,sock_pub_conn)
frame_read_worker_t = threading.Thread(target=frame_read_worker_i.worker)
frame_read_worker_t.start()

