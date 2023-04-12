import pygame
from .main_variable import *
from .othello.board_variable import *
from .button import *


def drawBar(win, colorTurn, playerTime):
    pygame.draw.rect(win, BARCOLOR2, (0,0,800,200))

    font = pygame.font.Font(None, 50)
    text1 = font.render("'s Turn ", True, BLACK)
    colorTxt = font.render("White" if colorTurn else "Black", True, WHITEPAWN if colorTurn else BLACKPAWN)
    win.blit(text1, (390, 20))
    win.blit(colorTxt, (290, 20))

    font2 = pygame.font.Font(None, 20)

    text2 = font2.render("Black playing time   :  " + str(int(playerTime[0]) // 60) + " : " + "{:.1f}".format(playerTime[0] % 60), True, BLACK)
    text3 = font2.render("White playing time :  " + str(int(playerTime[1]) // 60) + " : " + "{:.1f}".format(playerTime[1] % 60), True, BLACK)
    win.blit(text2, (20, 70))
    win.blit(text3, (20, 90))

def updateNbExplo(win, nbExplo):
    pygame.draw.rect(win, BARCOLOR2, (0, 120, 800, 200))

    font2 = pygame.font.Font(None, 20)
    text4 = font2.render("Explorations number :  " + str(nbExplo), True, BLACK)
    win.blit(text4, (20, 130))