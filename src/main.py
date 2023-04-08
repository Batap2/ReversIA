import pygame
from othello.board_variable import WIDTH, HEIGHT
from othello.board import Board
from othello_minimax import *
from othello.menu import *


class AI:
    def __init__(self, color: bool, heuristic: int = 0, depth: int = 4):
        self.color = color
        self.heuristic = heuristic
        self.depth = depth


FPS = 60

# Noir, Blanc, False = joueur, sinon AI()

Players = [False, AI(True, 0)]

EasyAI = AI(True, 0, 1)
MediumAI = AI(True, 0, 4)
HardAI = AI(True, 0, 6)

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Le Othello aka L'Reversi")


def main():
    global Nb_exploration
    run = True
    clock = pygame.time.Clock()
    board = Board()

    check_canPlay = False

    # Menu loop
    menu_id = 1
    pygame.font.init()  # init les fonts
    while (menu_id):
        clock.tick(FPS)
        mouse = pygame.mouse.get_pos()
        # Draw menu
        WIN.fill(GREY)
        write_text(WIN, WIDTH/2, HEIGHT/8, "OTHELLO", main_font, 80, BLACK)

        menu_id = render_menu(menu_id, WIN, mouse)  # Compute le menu courant

        # Si on quit (croix ou button QUIT)
        if (menu_id == 0):
            run = False

        # ---------- Player vs Player
        if (menu_id == 3):
            menu_id = 0
            Players = [False, False]

        # ---------- Player vs AI
        # ---Player starts
        if (menu_id == 8):  # AI easy
            Players = [False, EasyAI]
            menu_id = 0
        if (menu_id == 9):  # AI medium
            Players = [False, MediumAI]
            menu_id = 0
        if (menu_id == 10):  # AI hard
            Players = [False, HardAI]
            menu_id = 0
        # ---AI starts
        if (menu_id == 11):  # AI easy
            Players = [EasyAI, False]
            menu_id = 0
        if (menu_id == 12):  # AI medium
            Players = [MediumAI, False]
            menu_id = 0
        if (menu_id == 13):  # AI hard
            Players = [HardAI, False]
            menu_id = 0

        # AI vs AI
        # -------First AI
        if (menu_id == 14):
            FirstAI = EasyAI
        if (menu_id == 15):
            FirstAI = MediumAI
        if (menu_id == 16):
            FirstAI = HardAI
        # --------Second AI
        if (menu_id == 17):
            SecondAI = EasyAI
            Players = [FirstAI, SecondAI]
            menu_id = 0
        if (menu_id == 18):
            SecondAI = MediumAI
            Players = [FirstAI, SecondAI]
            menu_id = 0
        if (menu_id == 19):
            SecondAI = HardAI
            Players = [FirstAI, SecondAI]
            menu_id = 0
        pygame.display.update()

    # Game loop
    gameIsrunning = True
    while (run):
        clock.tick(FPS)
        if not check_canPlay and gameIsrunning:
            # check pour voir si le joueur actuel peux jouer, change board.currentPlayer sinon
            if (not board.canPlay(board.currentPlayer)):
                print("Le joueur " + ("blancs" if board.currentPlayer else "noirs") +
                      " ne peux pas jouer. Tour sauté")
                board.currentPlayer = not board.currentPlayer

                if (not board.canPlay(board.currentPlayer)):
                    print("Le joueur " + (
                        "blancs" if board.currentPlayer else "noirs") + " ne peux pas jouer. Tour sauté")
                    board.currentPlayer = not board.currentPlayer

                    winner = board.winner()
                    if winner == 0:
                        winner = "noirs"
                    elif winner == 1:
                        winner = "blancs"

                    if winner != 2:
                        print("Partie Terminée, les " + winner + " gagnent")
                    else:
                        print("Partie Terminée, égalité")
                    gameIsrunning = False
            else:
                # print("coups possibles pour les " + ("blancs" if board.currentPlayer else "noirs") + " : " + str(board.getPossiblePlay(board.currentPlayer)))
                print("----------------------------------- Tour des " + (
                    "blancs" if board.currentPlayer else "noirs") + " -------------------------------------------")
                None

            board.draw(WIN)
            pygame.display.update()

            check_canPlay = True

        if Players[int(board.currentPlayer)] != False:
            check_canPlay = False

            actualPlayer = Players[int(board.currentPlayer)]

            result = alpha_beta_minimax(Node(board), Players[int(board.currentPlayer)].depth, float("-inf"),
                                        float("inf"), True, board.currentPlayer,
                                        Players[int(board.currentPlayer)].heuristic)
            if result[1] is not None:
                board.applyMove(result[1], board.currentPlayer)
                print(
                    "Nb explorations: " + str(Nb_exploration[0]) + " Score: " + str(result[0]) + " Coup: " + str(result[1]))
                Nb_exploration[0] = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:

                check_canPlay = False

                if Players[int(board.currentPlayer)] == False:
                    mouse_pos = pygame.mouse.get_pos()
                    board.mouse_place_piece(mouse_pos)

            board.draw(WIN)
            pygame.display.update()

    # pygame.quit()


main()
