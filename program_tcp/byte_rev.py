import socket
import numpy as np
import struct

def receive_array_as_bytes(host='127.0.0.1', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))  # 连接到服务器
        while True:
            # 首先接收字节长度（4字节）
            length_bytes = client_socket.recv(4)
            if not length_bytes:
                break  # 如果没有接收到数据，则退出循环
            
            length = struct.unpack('>I', length_bytes)[0]  # 解包长度
            print(f"Expected byte string length: {length}")

            # 接收实际的字节串
            byte_string = client_socket.recv(length)
            if not byte_string:
                break  # 如果没有接收到数据，则退出循环

            print(f"Received byte string: {byte_string}")

            # 将字节串转换为 NumPy 数组
            array = np.frombuffer(byte_string, dtype=np.int32)
            print(f"Received array: {array}")

if __name__ == "__main__":
    receive_array_as_bytes()