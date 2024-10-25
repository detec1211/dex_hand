from proto_util import message_frame_pb2 as frame
import queue
import numpy as np
import struct

class frame_read_worker:
    def __init__(self, sock,sock_pub_sonn):
        self.sock = sock
        
        self.sock_pub_conn = sock_pub_sonn
        self.frame_queue = queue.Queue()
        # self.client_mes = client_message()  # TODO

    def read_payload_to_frame(self):
        bytes_to_read = self.sock.recv(4)
        bytes_length = int.from_bytes(bytes_to_read, "little")
        message = self.sock.recv(bytes_length)
        new_frame = frame.Frame()
        new_frame.ParseFromString(message)
        return new_frame

    def worker(self):
        while True:
            try:
                new_frame = self.read_payload_to_frame()
                self.frame_queue.put(new_frame)  # put it into a queue for use
                for frame_message in new_frame.frameMessages:
                    byte_string = str(frame_message.id)+','+str(frame_message.handMessage.thumb_split)+','+str(frame_message.handMessage.thumb_bend)+','+str(frame_message.handMessage.index_bend)+','+str(frame_message.handMessage.middle_bend)+','+str(frame_message.handMessage.ring_bend)+','+str(frame_message.handMessage.pinky_bend)
                    byte_string = byte_string.encode('utf-8')
                    length = len(byte_string)
                    self.sock_pub_conn.sendall(struct.pack('>I', length))
                    self.sock_pub_conn.sendall(byte_string)


                
              
                #print(new_frame)
            except Exception as e:

                print("Exception", e)
                self.sock_pub_conn.close()
                self.sock.close()