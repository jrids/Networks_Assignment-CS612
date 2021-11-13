# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 17:35:49 2021

@author: Johri
"""
#Server Fork Model
import socket
import os

ServerSocket = socket.socket()
host = socket.gethostname()
port = 12345
i = 0
try:
    ServerSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print('Waitiing for a Connection..')
ServerSocket.listen(10)


def fork_client(conn,i):
    #conn.send(str.encode('Welcome to the Server. File name?'))
    fname = conn.recv(32).decode()
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
    child_pid=os.fork()
    if child_pid==0:
        print('Connected to: ' + address[0] + ":" + str(address[1]))
        i=i+1
        fork_client(Client, i, )
        break

ServerSocket.close()