import pygame, sys, random, time, json
from pygame.locals import *

pieces_file = './Files/Pieces.png' #file with image of pieces
SQW = 75 #Square width

#FEN Notation: https://en.wikipedia.org/wiki/Forsyth%E2%80%93Edwards_Notation
starting_board = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'


def setup_board(fen_string):
    """
    This will create spirites and places them in their appropriate location based on the FEN string 
    """
    spirit_group = pygame.sprite.Group()
    i = 0
    for p in starting_board:
        if p == '/':
            continue
        elif p == ' ':
            break
        elif p.isdigit():
            i += int(p)
        else:
            Pieces = Piece(p,i)
            spirit_group.add(Pieces)
            i += 1

    return(spirit_group)


class Piece(pygame.sprite.Sprite):
    """ This class represents the pieces.It derives from the "Sprite" class in Pygame."""
    def __init__(self,piecetype,position):
        """ Constructor. Pass in the color of the piece"""
        super().__init__()

        # Load All chess pieces into PIECES
        # K Q B N R
        # k q b n r
        #rescales the pieces file into scale
        SPRITE = pygame.transform.smoothscale(pygame.image.load(pieces_file), (int(SQW*6), int(SQW*2)))
        
        PIECES = ['K','Q','B','N','R','P','k','q','b','n','r','p']
        for i in range(2):
            for j in range(6):
                if piecetype == PIECES[j + i*6]:
                    SURF = pygame.Surface.subsurface(SPRITE, (j*SQW, i*SQW, SQW, SQW))
                    self.image = SURF
        self.rect = self.image.get_rect()
        self.rect.x = 100 + (position % 8) * SQW
        self.rect.y = 100 + (position // 8) * SQW

def main():
    WHITE = (255,255,255)
    DARK = (119,149,86)
    LIGHT = (235,236,208)

    pygame.init()

    screen = pygame.display.set_mode((1200,800))
    screen.fill(WHITE)
    pygame.draw.rect(screen,DARK,(100,100,600,600))
    
    # This is a list of every sprite including the mouse spirite
    all_sprites_list = pygame.sprite.Group()
    
    
    #Draw the chess board
    for i in range(0,8):
        for j in range(0,8):
            if (i+j) % 2 == 0:
                pygame.draw.rect(screen,LIGHT,(100+75*i,100+75*j,75,75))
    

    Rematch = True
    
    all_sprites_list = setup_board(starting_board)
    
    
    while Rematch:
        
        all_sprites_list.draw(screen)
        pygame.display.flip()

        for event in pygame.event.get():
            if (event.type == pygame.QUIT) | (pygame.key.get_pressed()[K_ESCAPE]):
                Rematch = False
        
        
    #Exit pygame incase Escape is pressed or pragram stopped
    pygame.quit()

    
main()
