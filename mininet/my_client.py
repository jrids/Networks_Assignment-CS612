# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 17:37:14 2021

@author: Johri
"""

import socket
import os
import time
import random

class Client:
    def __init__(self):
        self.ClientSocket = socket.socket()
        self.host = '10.0.0.1'
        #socket.gethostname()
        self.port = 12345
        self.main()
        
    def main(self):
        print('Waiting for connection')
        try:
            self.ClientSocket.connect((self.host, self.port))
        except socket.error as e:
            print(str(e))

        #fname = input(self.ClientSocket.recv(1024).decode())
        fname = '2600-0.txt' #input('File name?')
        self.ClientSocket.send(fname.encode())
        #i = self.ClientSocket.recv(1024).decode()
        i = str(random.randint(1,50))

        confirmation = self.ClientSocket.recv(32)
        if confirmation.decode() == "file does not exist":
            print("File doesn't exist on server.")


        else:
            
            write_name = 'Server_file '+ i + fname
            if os.path.exists(write_name): os.remove(write_name)

            with open(write_name,'wb') as file:
                start_time = time.time()
                while True:
                    data = self.ClientSocket.recv(1024)

                    if not data:
                        break

                    file.write(data)
                end_time = time.time()

            print(fname,'successfully downloaded.')
            file_size = os.path.getsize(write_name)
            #print("File size: ", file_size)
            print("\nFile transfer Complete.Total time: ", end_time - start_time, "s")
            print("Throughput:", (file_size)/((end_time-start_time)*(10**6)), "MBps")
        self.ClientSocket.shutdown(socket.SHUT_RDWR)
        self.ClientSocket.close()
        #cont = input('Download more file? Yes or No')
        #if cont == "Yes":
         #   Client()
        #else:
           # print('Thankyou')
        
Client()


