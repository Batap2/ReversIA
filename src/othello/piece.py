from .board_variable import *
import pygame

import sys
sys.path.append('../main_variable.py')
from src.main_variable import BOARD_Y_OFFSET

class Piece:
    PADDING = 10
    BORDER = 2

    def __init__(self, color: bool, x: int, y: int = None):
        if y is None:
            self.pos = x
        else:
            self.pos = SIZE * y + x
        self.color = color

    def getPos_xy(self) -> (int, int):
        return self.pos % SIZE, self.pos // SIZE

    def draw(self, win):
        radius = SQUARE_SIZE // 2 - self.PADDING
        x = SQUARE_SIZE * (self.pos % SIZE) + SQUARE_SIZE // 2
        y = SQUARE_SIZE * (self.pos // SIZE) + SQUARE_SIZE // 2
        pygame.draw.circle(win, WHITEPAWN if self.color else BLACKPAWN, (x, y + BOARD_Y_OFFSET), radius)

    def __repr__(self):
        return str(self.color)
