# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 17:35:49 2021

@author: Johri
"""
#Server Thread Model
import socket
import os
from _thread import *

ServerSocket = socket.socket()
host = socket.gethostname()
port = 12345
ThreadCount = 0
try:
    ServerSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print('Waitiing for a Connection.')
ServerSocket.listen(10)


def thread_client(conn,i):
    #conn.send(str.encode('Welcome to the Server. File name?'))
    fname = conn.recv(1024).decode()
    #conn.send(str.encode(str(i)))
    
    if not os.path.exists(fname):
        conn.send("file does not exist".encode())
        print("file does not exist")

    else:
        conn.send("file exists".encode())
        print('Sending',fname)
        if fname != '':
            file = open(fname,'rb')
            data = file.read(1024)
            while data:
                conn.send(data)
                data = file.read(1024)

            conn.shutdown(socket.SHUT_RDWR)
            conn.close()
    

while True:
    Client, address = ServerSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    ThreadCount += 1
    start_new_thread(thread_client, (Client, ThreadCount,))
    print('Thread Number: ' + str(ThreadCount))
ServerSocket.close()