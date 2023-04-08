import pygame
from othello.board_variable import WIDTH, HEIGHT
from othello.board import Board
from othello_minimax import *


class AI:
    def __init__(self, color: bool, heuristic: int = 0, depth: int = 4):
        self.color = color
        self.heuristic = heuristic
        self.depth = depth


FPS = 60

# Noir, Blanc, False = joueur, sinon AI()
Players = [AI(False, 1, 3), AI(True, 2, 3)]
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Le Othello aka L'Reversi")


def main():
    global Nb_exploration
    run = True
    clock = pygame.time.Clock()
    board = Board()

    check_canPlay = False

    board.draw(WIN)
    pygame.display.update()

    while (run):
        clock.tick(FPS)

        if not check_canPlay:
            # check pour voir si le joueur actuel peux jouer, change board.currentPlayer sinon
            if (not board.canPlay(board.currentPlayer)):
                print("Le joueur " + ("blancs" if board.currentPlayer else "noirs") + " ne peux pas jouer. Tour sauté")
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

                    while True:
                        True
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
