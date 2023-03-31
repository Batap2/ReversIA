from .variable import SQUARE_SIZE, WHITE, BLACK
import pygame


class Piece:
    PADDING = 10
    BORDER = 2

    def __init__(self, row: int, col: int, color: bool):
        self.row = row
        self.col = col
        self.color = color
        self.x = 0
        self.y = 0
        self.compute_pos()

    def compute_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def draw(self, win):
        radius = SQUARE_SIZE // 2 - self.PADDING
        pygame.draw.circle(win, WHITE if self.color else BLACK, (self.x, self.y), radius)

    def __repr__(self):
        return str(self.color)
