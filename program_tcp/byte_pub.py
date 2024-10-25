import socket
import numpy as np
import struct

def start_server(host='127.0.0.1', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"Server listening on {host}:{port}")
        
        conn, addr = server_socket.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                # 创建 NumPy 数组
                integer_array = np.array([1364560, 2, 3, 4, 5], dtype=np.int32)
                # 将数组转换为字节串
                byte_string = integer_array.tobytes()
                
                # 发送字节长度（4字节的整数）
                length = len(byte_string)
                conn.sendall(struct.pack('>I', length))  # 大端字节序发送长度
                
                # 发送字节串
                conn.sendall(byte_string)
                print(f"Sent byte string of length {length}: {byte_string}")

if __name__ == "__main__":
    start_server()