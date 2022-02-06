#inspired by : https://www.youtube.com/watch?v=U4ogK0MIzqk&ab_channel=SebastianLague

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


def get_possible_moves(position,board,en_passant=None):
    """ Gets a list of all possible moves for the current selected piece """
    possible_moves = []
    if board[position] == 'P':
        if (position // 8 == 6) and board[position-8]== None and board[position-16]== None: #The white pawn is in the second rank and there are no pieces on the third or forth rank in front of the pawn
            possible_moves.extend([position-8 , position-16]) #pawn can jump either one or two squares
        elif board[position-8]== None:
            possible_moves.append(position-8)
        if position % 8 < 7 and ( board[position-7] in ['k','q','b','n','r','p'] or position-7 == en_passant): #if there is an opposite piece in the right side diagonal, then the pawn can capture them
            possible_moves.append(position-7)
        if position % 8 > 0  and ( board[position-9] in ['k','q','b','n','r','p'] or position-9 == en_passant): #if there is an opposite piece in the left side diagonal, then the pawn can capture them
            possible_moves.append(position-9)
    if board[position] == 'p':
        if (position // 8 == 1) and board[position+8]== None and board[position+16]== None: #The white pawn is in the second rank and there are no pieces on the third or forth rank in front of the pawn
            possible_moves.extend([position+8 , position+16]) #pawn can jump either one or two squares
        elif board[position+8]== None:
            possible_moves.append(position+8)
        if position % 8 < 7 and ( board[position+9] in ['k','q','b','n','r','p'] or position+9 == en_passant): #if there is an opposite piece in the right side diagonal, then the pawn can capture them
            possible_moves.append(position+9)
        if position % 8 > 0  and ( board[position+7] in ['k','q','b','n','r','p'] or position+7 == en_passant): #if there is an opposite piece in the left side diagonal, then the pawn can capture them
            possible_moves.append(position+7)   
    return(possible_moves)


class Piece(pygame.sprite.Sprite):
    """ This class represents the pieces.It derives from the "Sprite" class in Pygame."""
    def __init__(self,piecetype,position):
        """ Constructor. Pass in the color of the piece"""
        super().__init__()
        
        self.piecetype = piecetype
        self.position = position
        
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

def mouse_pos_to_square(mp):
    """
    Takes a mouse position and translates it into a square number in game from 0-63
    """
    x , y = mp
    if x >= 100 and x <= 100 + SQW*8 and y >= 100 and y <= 100 + SQW*8:
        return ((y-100) // SQW * 8 + (x-100) // SQW)
        

        
def main():
    WHITE = (255,255,255)
    DARK = (119,149,86)
    LIGHT = (235,236,208)
    mouse_pos = 0

    pygame.init()

    screen = pygame.display.set_mode((1200,800))
    screen.fill(WHITE)
    pygame.draw.rect(screen,DARK,(100,100,600,600))
    #Draw the chess board
    for i in range(0,8):
        for j in range(0,8):
            if (i+j) % 2 == 0:
                pygame.draw.rect(screen,LIGHT,(100+75*i,100+75*j,75,75))
   
    
    # This is a list of every sprite including the mouse spirite
    all_sprites_list = pygame.sprite.Group()
    
    pygame.font.init() # you have to call this at the start, if you want to use this module.
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    
    Rematch = True
    
    all_sprites_list = setup_board(starting_board)
    
    
    while Rematch:
        
        all_sprites_list.draw(screen)
        #Show text
        textsurface = myfont.render( 'Mouse Position: {}'.format(mouse_pos), False, (0, 0, 0))
        pygame.display.update(screen.blit(textsurface,(700,400)))
        pygame.display.flip()

        for event in pygame.event.get():
            if (event.type == pygame.QUIT) | (pygame.key.get_pressed()[K_ESCAPE]):
                Rematch = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: #event.type == 5: #mouse left button down (1: Left-click , 2= Middle-click , 3=Right-click)
                textsurface = myfont.render( 'Mouse Position: {}'.format(mouse_pos), False, WHITE)
                # pygame.display.update(textsurface.fill(WHITE))
                pygame.display.update(screen.blit(textsurface,(700,400)))
                # mouse_pos = pygame.mouse.get_pos()
                mouse_pos = mouse_pos_to_square(pygame.mouse.get_pos())
       
        
    #Exit pygame incase Escape is pressed or pragram stopped
    pygame.quit()

    
main()
