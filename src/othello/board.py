from src.variable import *
from .piece import Piece


class Board:
    def __init__(self):
        self.board = []
        self.create_board()
        # TODO : inverser sens car c'est le noir qui commence. Faut pas juste passer currentPlayer a False, faut faire ce qui va avec, si tu sais pas ce qui va avec fait pas
        self.currentPlayer = True  # True = White, False = Black
        self.playable_cell = []

    def draw_lines(self, win):
        win.fill(COLOR)
        for horizontal in range(SIZE):
            pygame.draw.line(win, BLACK, (0, horizontal * SQUARE_SIZE),
                             (WIDTH, horizontal * SQUARE_SIZE), 2)
        for vertical in range(SIZE):
            pygame.draw.line(win, BLACK, ((vertical + 1) * SQUARE_SIZE, 0),
                             ((vertical + 1) * SQUARE_SIZE, HEIGHT), 2)

    # python oblige, si y n'est pas donné, int x = pos
    def setPiece(self, color: bool, x, y=None):
        if y is None:
            self.board[x] = Piece(color, x)
        else:
            self.board[SIZE * y + x] = Piece(color, x, y)

    # python oblige, si y n'est pas donné, int x = pos
    def getPiece(self, x, y=None) -> Piece:
        if y is None:
            return self.board[x]
        else:
            return self.board[SIZE * y + x]

    def create_board(self):
        for square in range(SIZE * SIZE):
            self.board.append(0)
        center = SIZE // 2
        self.setPiece(True, center, center)
        self.setPiece(False, center - 1, center)
        self.setPiece(False, center, center - 1)
        self.setPiece(True, center - 1, center - 1)

    # Fonction qui pose un pion et applique les conséquences. Retourn True si le move a pu être appliqué, puis change le joueur
    def applyMove(self, pos, player:bool) -> bool:
        x = pos % SIZE
        y = pos // SIZE

        if self.getPiece(pos) == 0:  # Si la case est vide
            if self.isValid(x, y, self.currentPlayer):
                self.setPiece(self.currentPlayer, x, y)  # On joue sur cette case
                # Changement du joueur courant si le move a été joué
                if self.currentPlayer == True:
                    self.currentPlayer = False
                else:
                    self.currentPlayer = True
                return True
        return False

    def mouse_place_piece(self, pos):
        x = pos[0] // SQUARE_SIZE
        y = pos[1] // SQUARE_SIZE

        self.applyMove(SIZE*y + x, self.currentPlayer)

    def isValid(self, x, y, player: bool):  # Verifie si la pièce jouée est bien valide
        # TODO : remplacer par get8NeighbourPos. Parce que c'est comme ça que ça marche et pas juste les 4
        neighbours = self.get4NeighbourPos(x, y)

        # condition 1 : La case doit être vide
        if self.getPiece(x, y) != 0:
            return False

        # condition 2 : La case doit être adjacente à un pion du joueur
        check = False
        for n in neighbours:
            if self.getPiece(n[0], n[1]) != 0:
                if self.getPiece(n[0], n[1]).color != player:
                    check = True
                    break
        if not check:
            return False

        # condition 3 : Le pion placé doit permettre le retournement d'au moins un pion adverse
        # TODO : checker les 8 directions, faut pas qu'il y ai de trous

        return True

    def get4NeighbourPos(self, x, y):  # Recupère le 4-voisinage d'une case
        neighbours = []
        if x > 0:
            neighbours.append((x - 1, y))  # Voisin du haut
        if x < SIZE - 1:
            neighbours.append((x + 1, y))  # Voisin du bas
        if y > 0:
            neighbours.append((x, y - 1))  # Voisin de gauche
        if y < SIZE - 1:
            neighbours.append((x, y + 1))  # Voisin de droite
        return neighbours

    #TODO : faire ça
    def get8NeighbourPos(self, x, y):  # Recupère le 4-voisinage d'une case
        neighbours = []
        if x > 0:
            neighbours.append((x - 1, y))  # Voisin du haut
        if x < SIZE - 1:
            neighbours.append((x + 1, y))  # Voisin du bas
        if y > 0:
            neighbours.append((x, y - 1))  # Voisin de gauche
        if y < SIZE - 1:
            neighbours.append((x, y + 1))  # Voisin de droite
        return neighbours

    def getValidNeighbourPos(self, pos, player: bool) -> [int]:
        neighbours = []
        x = pos % SIZE
        y = pos // SIZE

        if x > 0 and self.isValid(x - 1, y, player):
            neighbours.append(pos - 1)  # Voisin du haut

        if x < SIZE - 1 and self.isValid(x + 1, y, player):
            neighbours.append(pos + 1)  # Voisin du bas

        if y > 0 and self.isValid(x, y - 1, player):
            neighbours.append(pos - SIZE)  # Voisin de gauche

        if y < SIZE - 1 and self.isValid(x, y + 1, player):
            neighbours.append(pos + SIZE)  # Voisin de droite

        return neighbours

    # Retourne les coup jouable pour player
    # TODO : A remplacer si ya des problèmes de perf, au début c'est bien mais vers le milieu du jeu c'est plus opti
    # TODO : Ouais faut faire une condition si il y a X pion présent parce que c'est infernal
    def getPossiblePlay(self, player: bool) -> [int]:
        plays = []
        for piece in self.board:
            if piece != 0:
                plays = plays + self.getValidNeighbourPos(piece.pos, player)

        return plays

    # Si il n'y a plus de coup jouable pour les deux joueurs alors la partie est finie
    def isGameFinished(self):
        if not(self.getPossiblePlay(True) or self.getPossiblePlay(False)):
            return True

        return False


    def draw_cross(self, win, x, y):  # Dessine une croix a une case données
        # Calculer la position x de la case
        x = x * 100
        # Calculer la position y de la case
        y = y * 100
        pygame.draw.line(win, GREY, (x, y), (x + 100, y + 100), 10)
        pygame.draw.line(win, GREY, (x + 100, y), (x, y + 100), 10)

    def draw(self, win):  # Dessine le quadrillage, les pieces jouées et les croix ou on peut jouer
        self.draw_lines(win)

        for square in range(SIZE * SIZE):
            x = square % SIZE
            y = square // SIZE

            piece = self.getPiece(x, y)

            if piece != 0:
                piece.draw(win)

            if self.isValid(x, y, self.currentPlayer):
                self.draw_cross(win, x, y)

