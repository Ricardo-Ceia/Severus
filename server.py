#!/usr/bin/env python3
import socket

HOST = ''
PORT = 50008

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST,PORT))
    s.listen(1)
    conn,addr = s.accept()
    with conn:
        print("Connected by ",addr)
        while True:
            data = conn.recv(1024)
            print(f"Client Data:{data}")
            conn.sendall(data)
    conn.exit()



