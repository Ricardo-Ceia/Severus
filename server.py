#!/usr/bin/env python3
import socket
import threading 
import json 


def handle_client(conn,addr):
    print(f"New connection: {addr} connected!")
    connected = True
    while connected:
        data = json.loads(conn.recv(1024).decode('utf-8'))
        if data['packet_type'] == 'conn_close':
            connected = False
            print(f"Closing {addr} connection!")
    conn.close()


HOST = ''
PORT = 50008


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST,PORT))
    s.listen(1)

    while True:
        conn,addr = s.accept()
        thread = threading.Thread(target=handle_client,args=(conn,addr))
        thread.start()
        print(f"{threading.active_count() - 1} Active connection ")



