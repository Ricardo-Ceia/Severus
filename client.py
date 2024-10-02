import socket
import json
import sys

def validate_command():
    while True:
        command = input("Enter the command to send message to user_X: user_id;message:")
        if not command == '':
            list_command = command.split(';')
            if not list_command[0]==command and command[0].isdigit():
                break
            else:
                print("INCORRECT INPUT:To send message to user_X use command:user_id;message")
    return int(list_command[0]),list_command[1]

#ADD A NEWLINE (ENTER) AT THE END OF "-send" TO SEND THE MESSAGE
def check_send_command(line):
    print("This is the line :"+line)
    if '-send' in line:
        return True
    return False


def send_msg_to_server(socket,msg,msg_type,reciver_id):
    text_packet = {
        'packet_type':msg_type,
        'size':len(msg),
        'message':msg,
        'reciver':'client'+str(reciver_id)
    }
    socket.sendall(bytes(json.dumps(text_packet),encoding = 'utf-8'))


HOST = ''
PORT = 50008


running = True

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    #This line is blocking so i cant close the window
    client_id = s.recv(1024)
    #######################
    while running:
        reciver_id,message = validate_command()
        send_message_to_server(s,message,"text",reciver_id)
                 