#!/usr/bin/env python3
import socket
import threading 
import json 


client_messages = {}
num_lock = threading.Lock()
client_id = 1


def handle_client(conn,addr):
    global client_id
    
    print(f"New connection: {addr} connected!")
    with num_lock:
        conn.send(str(client_id).encode('utf-8'))
        client_id += 1
    connected = True
    while connected:      
        data = json.loads(conn.recv(1024).decode('utf-8'))
        client_messages[data['reciver']] = []
        client_messages['reciver'].add(data['message'])
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



