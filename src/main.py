import pygame
from orthello.variable import WIDTH, HEIGHT, SQUARE_SIZE
from orthello.board import Board

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Orthello")


def main():
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
                board.place_piece(mouse_pos)

                board.draw(WIN)
                pygame.display.update()

                if board.isGameFinished():
                    print("Partie Terminée")
                pass

    pygame.quit()


main()
