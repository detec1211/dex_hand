import struct
from proto_util import ctrl_command_pb2 as command
import queue


class command_write_worker:
    def __init__(self, sock):
        self.sock = sock
        self.command_queue = queue.Queue()
        # self.client_mes = client_message()  # TODO

    def add_new_impedance_control(self, id, new_impedance_control):
        new_command = command.CommandControl()
        new_command.id = id
        new_command.impedance_command.append(new_impedance_control)
        self.command_queue.put(new_command)



    def worker(self):
        while True:
            try:
                print("socket queue长度")
                new_command = self.command_queue.get()
                size_bytes = struct.pack("i", new_command.ByteSize())
                self.sock.sendall(size_bytes + new_command.SerializeToString())

            except Exception as e:
                print(e)
