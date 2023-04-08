from .board_variable import SQUARE_SIZE, WHITE, BLACK, SIZE
import pygame


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
        pygame.draw.circle(win, WHITE if self.color else BLACK, (x, y), radius)

    def __repr__(self):
        return str(self.color)
