from pygame import time
from pygame import mixer
import numpy as np
import pygame
import sys

pygame.init()


class button :
    def __init__(self,text,width,height,pos) :
        self.top_rect = pygame.Rect(pos,(width,height))
        self.top_color = '#475F77'
        self.click = False
        self.text_surf = font.render(text,True,'#FFFFFF')
        self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)    

    def draw(self) :
        pygame.draw.rect(screen,self.top_color,self.top_rect,border_radius=10)
        screen.blit(self.text_surf,self.text_rect)
        return self.check_click()
    
    def check_click(self) :
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            self.top_color= '#D74B4B'
            if pygame.mouse.get_pressed()[0]:
                self.click = True
                self.top_color = '#a72525'
            else:
                if self.click == True :
                    self.click = False
                    return True
        else :
            self.top_color = '#475F77'
            return False

font = pygame.font.SysFont("Arial",30)
height = 500
width = 800
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Music")
Pause = button('Pause',125,50,(270,440))
Next = button('Next',125,50,(405,440))
Play = button('Play',125,50,(270,440))
run = True
state = 'Play'



mixer.init()
mixer.music.set_volume(1)
number = np.random.permutation(20)
# number.extend(np.random.permutation(20))
#print(number)
number = number + np.ones(20 ,dtype = int).reshape(20)
#print(number)
while run:
    
    count = 0
    song = number[0]
    s = str(song)
    mixer.music.load(s + '.mp3')
    mixer.music.play()
    print(s +'.mp3')
    Text = button('Currently Playing: '+ s + '.mp3',395,60,(220,220))
    
    screen.fill((39,48,71))
    Text.draw()
    while True :
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
         
        
        if Next.draw() or (pygame.mixer.music.get_busy() and not state == "Play"):
            count += 1
            if count == 20:
                number = np.random.permutation(20)
                number = number + np.ones(20 ,dtype = int).reshape(20)
            song = number[count%20]
            s= str(song)
            path = str(song) + '.mp3'             
            print(path)
            mixer.music.load(path)
            mixer.music.play()
            screen.fill((39,48,71))
            Text = button('Currently Playing: '+ s + '.mp3',395,60,(220,220))
            Text.draw()
            Next.draw()
            
        if state == "Play" :
            if Pause.draw():
                state = 'Pause'
                mixer.music.pause()
        else :
            if Play.draw() :
                state = 'Play'
                mixer.music.unpause()
            
        
        
               
        pygame.display.update()
        


pygame.quit()


