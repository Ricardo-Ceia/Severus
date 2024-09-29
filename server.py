#!/usr/bin/env python3
import socket
import threading 
import json 

HOST = ''
PORT = 50008


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST,PORT))
    s.listen(1)
    conn,addr = s.accept()
    with conn:
        print("Connected by ",addr)
        Connected = True
        while Connected:
            data = json.loads(conn.recv(1024).decode('utf-8'))
            print(f"Client Data:{data}")
            print(type(data))
            if data['packet_type'] == 'conn_close':
                Connected = False
        conn.close()
            #conn.sendall(data)
    #conn.exit()



