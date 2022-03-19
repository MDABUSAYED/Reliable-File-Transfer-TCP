#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  17 21:41:53 2022

@author: msayed
"""

from socket import *
import threading
import sys
import ast
import os


    

def main():
    """
    Open servver socket and bind it at IP and port number.
    Receiving client request and execute it and waiting for new request.
    
    Arguments:
    None.
    
    Returns:
    None.
    """
    buffer_size = 1000
    host = "10.0.0.3"
    
    # Input port
    port = int(input('Listen at port# '))
    
    try: 
        # The proxy server is listening at hoat and port 
        tcpSerSock = socket(AF_INET, SOCK_STREAM)
        tcpSerSock.bind((host, port))
        tcpSerSock.listen(100)
    except tcpSerSock.error as error:
        print('Caught exception tcpSerSock.error : %s', error)
        
    # Infinite loop for accepting client request.
    while True:
        
        
        print('Listening for connection at ...', port)
        
        try:
            # Waiting for client to connect
            tcpCliSock, addr = tcpSerSock.accept()
            
        except tcpSerSock.error as error:
            print('Caught exception tcpSerSock.error : %s', error)
        
        print('Connection accepted from: ', addr)
        
        
        # Client request specific file from server.
        requested_file = tcpCliSock.recv(buffer_size).decode()
        
        # Extract file name
        requested_file = requested_file.split(' ')[1]
        
        # Calculate file size in bytes
        file_size = os.path.getsize(requested_file)
        
        # Send file size to client 
        #print(str(file_size).encode())
        tcpCliSock.send(str(file_size).encode('utf-8')) 
        
        print('Asking for file ', requested_file)
        
        print('Sending the file ...')
        
        # Open requested file
        with open(requested_file, "rb") as f:
            while True:
                # Read the bytes from the file
                bytes_read = f.read(buffer_size)
                if not bytes_read:
                    # File transmission is done
                    break
                # Send sigle packet to client
                tcpCliSock.send(bytes_read)
        
        print('Transfer Complete!')
        
        # Waiting for client msg to proceed 
        msg = tcpCliSock.recv(buffer_size).decode('utf-8')
        
        if msg == 'CLOSE':
            print('Connection closed, See you later!')
    try:  
        # Close the client and server sockets  
        tcpCliSock.close()
        tcpSerSock.close()
        
    except tcpCliSock.error as error:
        print("Caught exception tcpCliSock.error : %s", error)

    
    
if __name__ == '__main__':
    main()
    
