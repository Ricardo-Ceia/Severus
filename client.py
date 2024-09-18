import socket
import json
import sys
import pygame

HOST = ''
PORT = 50008

WIDTH = 600
HEIGHT = 600

NEXT_CHAR_POSITION_WIDTH_OFFSET = 5
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
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            print("Severus has been closed!")
            sys.exit()
        if event.type == pygame.KEYDOWN:
            inputed_char = chr(event.key)
            char_to_be_rendered = font.render(inputed_char,True,COLOR_LETTERS)
            screen.blit(char_to_be_rendered, (current_char_width_position, current_char_height_position))
            pygame.display.update()
            current_char_width_position += NEXT_CHAR_POSITION_WIDTH_OFFSET
            if current_char_width_position >= WIDTH:
                current_char_height_position += NEXT_CHAR_POSITION_HEIGHT_OFFSET
                current_char_width_position = 0
            #TODO:REVIEW THIS PART OF THE CODE TO RENDER A RECTANGLE ON TOP OF THE OTHER WITHOUT DELETE PREVIOUS WRITTEN LINES 
            #if current_char_height_position >= HEIGHT:
                #new_rect_height_offset-=NEW_BOTTOM_BAR_RENDER_OFFSET
                #pygame.draw.rect(screen,COLOR_BOTTOM_BAR,pygame.Rect(0,new_rect_height_offset,WIDTH,HEIGHT))
                #pygame.display.update(pygame.Rect(pygame.Rect(0,new_rect_height_offset,WIDTH,HEIGHT)))
                #current_char_height_position = HEIGHT-15            

'''    
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))i
    text = input()
    text_packet={
        'packet_type':'text',
        'size':len(text),
        'data':text
    }
    s.sendall(bytes(json.dumps(text_packet),encoding='utf-8'))
    data_recevied = json.loads(s.recv(1024).decode('utf-8'))
print('Received ',data_recevied)
'''