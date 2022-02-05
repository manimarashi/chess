import pygame, sys, random, time, json
from pygame.locals import *

pieces_file = './Files/Pieces.png' #file with image of pieces
SQW = 75 #Square width

# ---------------------------------------- Pieces class ----------------------------
class Piece(pygame.sprite.Sprite):
    """ This class represents the pieces.It derives from the "Sprite" class in Pygame."""
    def __init__(self,piecetype,pos):
        """ Constructor. Pass in the color of the piece"""
        super().__init__()
        if piecetype== 'K':
            # self.image = pygame.image.load(WhitePiecePicFile).convert_alpha()
            self.image = pygame.Surface.subsurface(SPRITE, (j*SQW, i*SQW, SQW, SQW))
        elif color == 'b':
            # self.image = pygame.image.load(BlackPiecePicFile).convert_alpha()
            
        # Load All chess pieces into PIECES
        # K Q B N R
        # k q b n r
        SPRITE = pygame.transform.smoothscale(pygame.image.load(pieces_file), (int(SQW*6), int(SQW*2)))
        PIECES = [None] * 12
        for i in range(2):
            for j in range(6):
                PIECES[j + i*6] = pygame.Surface.subsurface(SPRITE, (j*SQW, i*SQW, SQW, SQW))    
            
        self.rect = self.image.get_rect()

def main():
    WHITE = (255,255,255)
    DARK = (119,149,86)
    LIGHT = (235,236,208)

    pygame.init()

    screen = pygame.display.set_mode((1200,800))
    screen.fill(WHITE)
    pygame.draw.rect(screen,DARK,(100,100,600,600))
    for i in range(0,8):
        for j in range(0,8):
            if (i+j) % 2 == 0:
                pygame.draw.rect(screen,LIGHT,(100+75*i,100+75*j,75,75))
    
    
    # https://stackoverflow.com/questions/38535330/load-only-part-of-an-image-in-pygame
    SPRITE = pygame.transform.smoothscale(pygame.image.load(pieces_file), (int(SQW*6), int(SQW*2)))
    PIECES = [None] * 12
    for i in range(2):
        for j in range(6):
            PIECES[j + i*6] = pygame.Surface.subsurface(SPRITE, (j*SQW, i*SQW, SQW, SQW))
            screen.blit(PIECES[j + i*6], (100+j*75,100+i*75),(0,0,80,80))
    
    
    #pygame.display.flip()
    
    
    
    
    Rematch = True

    while Rematch:

        for event in pygame.event.get():
            if (event.type == pygame.QUIT) | (pygame.key.get_pressed()[K_ESCAPE]):
                Rematch = False
        pygame.display.update()
    pygame.quit()

    
main()
