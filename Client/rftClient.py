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
import signal
import math

# Global variable, 
dictionary = {}
    

def main():
    """
    Open client socket and connect it with IP and port number of server.
    
    Arguments:
    None.
    
    Returns:
    None.
    """
    buffer_size = 1000
    
    # Input server ip
    server_ip = input("Provide Server IP: ")
    
    # Input server port
    port = int(input("Provide Port#: "))
    
    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    
    # Connect with server ip and port
    tcpCliSock.connect((server_ip, port))
    
    print("You are now connected! Enter your commands now.")
    
    # Requested file from client 
    requested_file = input()
    #Send requested file name to server
    tcpCliSock.send(requested_file.encode('utf-8'))
    
    # Extract file name
    requested_file = requested_file.split(' ')[1]
    
    # File size form server
    file_size = int(tcpCliSock.recv(buffer_size).decode('utf-8'))
    
    # Number of packets going to receive form server
    number_of_packets = math.ceil(file_size / buffer_size)
    
    # Loop counter
    i = 0
    
    with open(requested_file, "wb") as f:
        while True:
            if i == number_of_packets:    
                # Nothing is received file transmitting is done
                break
            # Receive sigle packet from server
            bytes_read = tcpCliSock.recv(buffer_size)
            
            #if bytes_read == b'':
            	#print('cb')
            	#break
            
            # Write the received packet on file
            f.write(bytes_read)
            
            # Increment counter
            i = i + 1
    
    
    
    
    print('Received ', requested_file)
    
    # Send msg to  server to lcose socket
    tcpCliSock.send(input().encode('utf-8'))
    
    try:  
        # Close the client sockets  
        tcpCliSock.close()
        
    except tcpCliSock.error as error:
        print("Caught exception tcpCliSock.error : %s", error)
    
    
        
    
if __name__ == '__main__':
    main()
    
