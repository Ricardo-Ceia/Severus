import socket
import json



HOST = ''    # The remote host
PORT = 50007              # The same port as used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    text = input()
    text_packet={
        'size':len(text),
        'data':text 
    }
    s.sendall(bytes(json.dumps(text_packet),encoding='utf-8'))
    data_recevied = json.loads(s.recv(1024).decode('utf-8'))
print('Received ',data_recevied['data'])
