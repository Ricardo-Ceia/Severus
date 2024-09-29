import socket
import json
import sys
import pygame

#ADD A NEWLINE (ENTER) AT THE END OF "-send" TO SEND THE MESSAGE
def check_send_command(line):
    print("This is the line :"+line)
    if '-send' in line:
        return True
    return False


def send_msg_to_server(socket,msg,msg_type):
    text_packet = {
        'packet_type':msg_type,
        'size':len(msg),
        'message':msg
    }
    socket.sendall(bytes(json.dumps(text_packet),encoding = 'utf-8'))


HOST = ''
PORT = 50008

WIDTH = 600
HEIGHT = 600

NEXT_CHAR_POSITION_WIDTH_OFFSET = 10
NEXT_CHAR_POSITION_HEIGHT_OFFSET = 20
NEW_BOTTOM_BAR_RENDER_OFFSET = 15
COLOR_BOTTOM_BAR = (255,255, 220)
COLOR_LETTERS = (0,0,0)

pygame.init()

pygame.display.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT)) #DEAL PROPERLY WITH RESIZING ISSUE
pygame.draw.rect(screen, COLOR_BOTTOM_BAR, pygame.Rect(0,HEIGHT-15,WIDTH,HEIGHT))
pygame.display.flip()
font = pygame.font.Font('freesansbold.ttf', 15)

running = True
current_char_width_position = 0
current_char_height_position = HEIGHT-15
new_rect_height_offset = HEIGHT - NEW_BOTTOM_BAR_RENDER_OFFSET

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    line = ""
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                send_msg_to_server(s,"","conn_close")
                print("Severus has been closed!")
                sys.exit()
            if event.type == pygame.KEYDOWN:
                inputed_char = event.unicode
                char_to_be_rendered = font.render(inputed_char,True,COLOR_LETTERS)
                screen.blit(char_to_be_rendered, (current_char_width_position, current_char_height_position))
                pygame.display.update()
                current_char_width_position += NEXT_CHAR_POSITION_WIDTH_OFFSET
                if check_send_command(line):
                    send_msg_to_server(s,line,"text")
                    pygame.draw.rect(screen,COLOR_BOTTOM_BAR,pygame.Rect(0,HEIGHT-15,WIDTH,HEIGHT))
                    pygame.display.update()
                    current_char_width_position = 0
                    line = ""
                    current_char_height_position = HEIGHT-15
                if current_char_width_position >= WIDTH:
                    current_char_height_position += NEXT_CHAR_POSITION_HEIGHT_OFFSET
                    current_char_width_position = 0
                #TODO:ADD MULTI-LINE SUPPORT 
                if current_char_height_position >= HEIGHT:
                    pygame.quit()
                    print("Severus has been closed! You have reached the max amount of characters!")
                    sys.exit()

                line += inputed_char
