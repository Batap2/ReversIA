import pygame
from variable import WIDTH, HEIGHT
from othello.board import Board
from othello_minimax import *

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Orthello")


def main():
    global Nb_exploration
    run = True
    clock = pygame.time.Clock()
    board = Board()

    board.draw(WIN)
    pygame.display.update()

    while (run):
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                board.mouse_place_piece(mouse_pos)

                board.draw(WIN)
                pygame.display.update()

                if board.currentPlayer == False:
                #    board.applyMove(minimax(Node(board), 4, True, False)[1], False)
                    AImove = alpha_beta_minimax(Node(board), 4, float("-inf"), float("inf"), True, False)[1]
                    if AImove != None:
                        board.applyMove(AImove, False)
                    else:
                        board.switch_player()

                print(Nb_exploration)
                Nb_exploration[0] = 0

                board.draw(WIN)
                pygame.display.update()

                if board.isGameFinished():
                    print("Partie Terminée")
                pass

    pygame.quit()


main()
