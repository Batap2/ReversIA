from .board_variable import *
from .piece import Piece


class Board:
    def __init__(self):
        self.board = []
        self.create_board()
        # TODO : inverser sens car c'est le noir qui commence. Faut pas juste passer currentPlayer a False, faut faire ce qui va avec, si tu sais pas ce qui va avec fait pas
        self.currentPlayer = False  # True = White, False = Black
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
    def applyMove(self, pos, player: bool) -> bool:
        x = pos % SIZE
        y = pos // SIZE

        if self.getPiece(pos) == 0:  # Si la case est vide
            if self.isValid(x, y, self.currentPlayer):
                self.setPiece(self.currentPlayer, x, y)  # On joue sur cette case
                self.compute_outflanking(x, y, self.currentPlayer)
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

        self.applyMove(SIZE * y + x, self.currentPlayer)

    # Change la couleur des pions pris en sandwich par le pion placé
    def compute_outflanking(self, x, y, player: bool):
        neighbours = self.get8NeighbourPos(x, y)
        for n in neighbours:
            if self.getPiece(n[0], n[1]) != 0:
                if self.getPiece(n[0], n[1]).color != player:
                    direction = (n[0] - x, n[1] - y)  # direction dans laquelle doit se faire le sandwich
                    if 0 <= n[0] + direction[0] <= SIZE - 1 and 0 <= n[1] + direction[1] <= SIZE - 1:
                        if self.getPiece(n[0] + direction[0], n[1] + direction[1]) != 0:
                            if self.getPiece(n[0] + direction[0], n[1] + direction[1]).color == player:
                                self.getPiece(n[0], n[1]).color = player

    def isValid(self, x, y, player: bool):  # Verifie si la pièce jouée est bien valide
        neighbours = self.get8NeighbourPos(x, y)

        # condition 1 : La case doit être vide
        if self.getPiece(x, y) != 0:
            return False

        # condition 2 : La case doit être adjacente à un pion du joueur adverse
        check = False
        for n in neighbours:
            if self.getPiece(n[0], n[1]) != 0:
                if self.getPiece(n[0], n[1]).color != player:
                    check = True
                    break
        if not check:
            return False

        # condition 3 : Le pion placé doit permettre le retournement d'au moins un pion adverse
        # i.e. le placement permet de prendre en sandwich un pion adverse.
        adjacent = []  # listes des pions adverses adjacents
        for n in neighbours:
            if self.getPiece(n[0], n[1]) != 0:
                if self.getPiece(n[0], n[1]).color != player:
                    adjacent.append((n[0], n[1]))
        check = False
        for p in adjacent:
            direction = (p[0] - x, p[1] - y)  # direction dans laquelle doit se faire le sandwich
            if 0 <= p[0] + direction[0] <= SIZE - 1 and 0 <= p[1] + direction[1] <= SIZE - 1:
                if self.getPiece(p[0] + direction[0], p[1] + direction[1]) != 0:
                    if self.getPiece(p[0] + direction[0], p[1] + direction[1]).color == player:
                        check = True
                        break
        if not check:
            return False

        return True

    def get8NeighbourPos(self, x, y):  # Recupère le 8-voisinage d'une case
        neighbours = []
        for i in x - 1, x, x + 1:
            for j in y - 1, y, y + 1:
                if i == x and j == y:
                    continue
                if not ((0 <= i <= SIZE - 1) and (0 <= j <= SIZE - 1)):
                    continue
                neighbours.append((i, j))
        return neighbours

    def getValidNeighbourPos(self, pos, player: bool) -> [int]:
        neighbours = []
        x = pos % SIZE
        y = pos // SIZE
        for i in x - 1, x, x + 1:
            for j in y - 1, y, y + 1:
                if i == x and j == y:
                    continue
                if not ((0 <= i <= SIZE - 1) and (0 <= j <= SIZE - 1)):
                    continue
                if self.isValid(i, j, player):
                    neighbours.append(i + SIZE * j)
        return neighbours

    # Retourne les coup jouable pour player
    # TODO : A remplacer si ya des problèmes de perf, au début c'est bien mais vers le milieu du jeu c'est plus opti
    # TODO : Ouais faut faire une condition si il y a X pion présent parce que c'est infernal
    def getPossiblePlay(self, player: bool) -> [int]:
        plays = set([])
        for piece in self.board:
            if piece != 0:
                plays.update(self.getValidNeighbourPos(piece.pos, player))

        return plays

    def canPlay(self, color: bool) -> bool:
        if self.getPossiblePlay(color):
            return True
        else:
            return False

    # Si il n'y a plus de coup jouable pour les deux joueurs alors la partie est finie
    def isGameFinished(self):
        if not (self.getPossiblePlay(True) or self.getPossiblePlay(False)):
            return True

        return False

    # noirs, blancs
    def countPawn(self) -> (int, int):
        n = 0
        b = 0
        for squares in self.board:
            if squares != 0:
                if squares.color:
                    b = b + 1
                else:
                    n = n + 1
        return n, b

    # 0 = noir, 1 = blanc, 2 = égalité
    def winner(self) -> int:
        res = self.countPawn()

        if res[0] > res[1]:
            return 0
        elif res[1] > res[0]:
            return 1
        else:
            return 2

    def draw_cross(self, win, x, y):  # Dessine une croix a une case données
        # Calculer la position x de la case
        x = x * 100
        # Calculer la position y de la case
        y = y * 100
        pygame.draw.line(win, GREY, (x + 30, y + 30), (x + 70, y + 70), 5)
        pygame.draw.line(win, GREY, (x + 70, y + 30), (x + 30, y + 70), 5)

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
