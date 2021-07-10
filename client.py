import socket
import threading
import math
import random
from encrypt import xor,text_to_bits,text_from_bits,DNA_coding_encrypt,start_encrypt
from decrypt import xor,text_to_bits,text_from_bits,DNA_coding_decrypt,start_decrypt
# from decrypt import *

class Client:
    def __init__(self):
        self.create_connection()

    def create_connection(self):
        self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        
        while 1:
            try:
                host = input('Enter host name --> ')
                port = int(input('Enter port --> '))
                self.s.connect((host,port))
                
                break
            except:
                print("Couldn't connect to server")

        self.username = input('Enter username --> ')
        self.s.send(self.username.encode())
        
        message_handler = threading.Thread(target=self.handle_messages,args=())
        message_handler.start()

        input_handler = threading.Thread(target=self.input_handler,args=())
        input_handler.start()

    def handle_messages(self):
        while 1:
            mes=str(self.s.recv(1204).decode())
            if(mes[0]!='*'):
                mes=mes.split('-')
                print(start_decrypt(mes[1]))

    def input_handler(self):
        while 1:
            
            # in_str=start_encrypt(in_str)
            self.s.send((self.username+'-'+start_encrypt(input())).encode())
            in_str=input("1.End_to_end\t2.Broadcast\t")
            self.s.send(in_str.encode())

            if in_str=='1':
                self.s.send(input().encode())
            



client = Client()
