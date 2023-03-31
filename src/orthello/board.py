import pygame
from .variable import *
from .piece import Piece


class Board:
    def __init__(self):
        self.board = []
        self.create_board()
        self.currentPlayer = True  # True = White, False = Black
        self.playable_cell = []

    def draw_lines(self, win):
        win.fill(COLOR)
        for row in range(ROWS):
            pygame.draw.line(win, BLACK, (0, row * SQUARE_SIZE),
                             (WIDTH, row * SQUARE_SIZE), 2)
        for col in range(COLS):
            pygame.draw.line(win, BLACK, ((col + 1) * SQUARE_SIZE, 0),
                             ((col + 1) * SQUARE_SIZE, HEIGHT), 2)

    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if row >= (ROWS // 2) - 1 and row <= (ROWS // 2):
                    if col >= (COLS // 2) - 1 and col <= (COLS // 2):
                        if col % 2 == ((row) % 2):
                            self.board[row].append(Piece(row, col, False))
                        else:
                            self.board[row].append(Piece(row, col, True))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)

    def place_piece(self, pos):
        col = pos[0] // SQUARE_SIZE
        row = pos[1] // SQUARE_SIZE
        if self.board[row][col] == 0:  # Si la case est vide
            if self.isValid(row, col):
                self.board[row][col] = Piece(
                    row, col, self.currentPlayer)  # On joue sur cette case
                # Changement du joueur courant si le mouve a été joué
                if self.currentPlayer == True:
                    self.currentPlayer = False
                else:
                    self.currentPlayer = True

    def isValid(self, row, col):  # Verifie si la pièce jouée est bien valide
        res = False
        neighbours = self.get_neighbour(row, col)
        for neigh in neighbours:
            if self.board[neigh[0]][neigh[1]] != 0:
                if (self.board[neigh[0]][neigh[1]]).color != self.currentPlayer:
                    res = True
        return res

    def get_neighbour(self, row, col):  # Recupère le 4-voisinage d'une case
        neighbours = []
        if row > 0:
            neighbours.append((row - 1, col))  # Voisin du haut
        if row < ROWS - 1:
            neighbours.append((row + 1, col))  # Voisin du bas
        if col > 0:
            neighbours.append((row, col - 1))  # Voisin de gauche
        if col < COLS - 1:
            neighbours.append((row, col + 1))  # Voisin de droite
        return neighbours

    def draw_cross(self, win, row, col):  # Dessine une croix a une case données
        # Calculer la position x de la case
        x = col * 100
        # Calculer la position y de la case
        y = row * 100
        pygame.draw.line(win, GREY, (x, y), (x + 100, y + 100), 10)
        pygame.draw.line(win, GREY, (x + 100, y), (x, y + 100), 10)

    # Affiche les mouvement jouable au tour courant
    def show_playable_cell(self, win, row, col):
        neighbours = self.get_neighbour(row, col)
        for neigh in neighbours:
            if self.board[neigh[0]][neigh[1]] == 0:
                if (self.board[row][col]).color != self.currentPlayer:
                    self.draw_cross(win, neigh[0], neigh[1])

    def draw(self, win):  # Dessine le quadrillage, les pieces jouées et les croix ou on peut jouer
        self.draw_lines(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                neighbours = self.get_neighbour(row, col)
                if piece != 0:
                    piece.draw(win)
                    self.show_playable_cell(win, row, col)

    # TODO : faut refaire, ça c'est de la merde. Faut check si il n'y a plus de coup jouable.
    # TODO : Par contre ça peut être chaud niveau ressource si on fait pas un truc intelligent,
    # TODO : parce que c'est appelé bcp de fois dans minimax
    def isGameFinished(self):
        for row in self.board:
            for piece in row:
                if piece == 0:
                    return False
        return True
