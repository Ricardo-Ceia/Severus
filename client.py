import socket
import json
import sys
import pygame

HOST = ''
PORT = 50008
WIDTH = 600
HEIGHT = 600
COLOR_BOTTOM_BAR = (255,255, 220)
pygame.display.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT)) #DEAL PROPERLY WITH RESIZING ISSUE
pygame.draw.rect(screen, COLOR_BOTTOM_BAR, pygame.Rect(0,HEIGHT-30,WIDTH,HEIGHT))
pygame.display.flip()
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    text = input()
    text_packet={
        'packet_type':'text',
        'size':len(text),
        'data':text
    }
    s.sendall(bytes(json.dumps(text_packet),encoding='utf-8'))
    data_recevied = json.loads(s.recv(1024).decode('utf-8'))
print('Received ',data_recevied)
