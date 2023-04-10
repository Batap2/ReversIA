import time

import pygame.mixer
from othello.board import Board
from othello_minimax import *
from menu import *
from main_variable import *
import display

pygame.mixer.init()
pygame.mixer.music.load("../media/1.ogg")
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)

class AI:
    def __init__(self, color: bool, heuristic: int = 0, depth: int = 4):
        self.color = color
        self.heuristic = heuristic
        self.depth = depth


def drawEndBar(win, mousePos, winner):
    pygame.draw.rect(win, BARCOLOR2, (0, 0, 800, 200))

    font = pygame.font.Font(None, 50)

    if winner == 2:
        text = font.render("Égalité", True, BLACK)
        win.blit(text, (WIDTH / 2, 20))
    else:
        text = font.render("Victoire des ", True, BLACK)
        colorTxt = font.render("blancs" if bool(winner) else "noirs", True, WHITEPAWN if bool(winner) else BLACKPAWN)

        win.blit(text, (250, 20))
        win.blit(colorTxt, (460, 20))

    retry_Button = Button(300, 150, "Recommencer", None, 50, WHITE, BLACK)
    quit_Button = Button(550, 150, "Quitter", None, 50, WHITE, BLACK)

    retry_Button.draw(win, mousePos)
    quit_Button.draw(win, mousePos)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if quit_Button.is_hovered:
                pygame.quit()
            if retry_Button.is_hovered:
                main()


FPS = 60

# Noir, Blanc, False = joueur, sinon AI()
Players = [False, AI(True, 0)]
playerPlayTime = [0, 0]

EasyAI = AI(True, 1, 2)
MediumAI = AI(True, 1, 4)
HardAI = AI(True, 1, 6)

WIN = pygame.display.set_mode(WINDOWSIZE)

pygame.display.set_caption("ReversIA")


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
        WIN.fill(WHITEPAWN)
        write_text(WIN, WIDTH / 2, HEIGHT / 8, "ReversIA", main_font, 80, BLACKPAWN)

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

    pygame.mixer.init()
    pygame.mixer.music.load("../media/2.ogg")
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1)

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

                    while True:
                        mouse = pygame.mouse.get_pos()
                        drawEndBar(WIN, mouse, winner)
                        pygame.display.update()

            else:
                display.drawBar(WIN, board.currentPlayer, playerPlayTime)
                display.updateNbExplo(WIN, Nb_exploration[0])

                playTime = time.time()

            board.draw(WIN)
            pygame.display.update()

            check_canPlay = True

        if Players[int(board.currentPlayer)] != False:
            check_canPlay = False
            Nb_exploration[0] = 0

            result = alpha_beta_minimax(Node(board), Players[int(board.currentPlayer)].depth, float("-inf"),
                                        float("inf"), True, board.currentPlayer,
                                        Players[int(board.currentPlayer)].heuristic)
            if result[1] is not None:
                board.applyMove(result[1], board.currentPlayer)
                print(
                    "Nb explorations: " + str(Nb_exploration[0]) + " Score: " + str(result[0]) + " Coup: " + str(
                        result[1]))

                playerPlayTime[int(not board.currentPlayer)] = playerPlayTime[
                                                                   int(not board.currentPlayer)] + time.time() - playTime
        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                if event.type == pygame.MOUSEBUTTONDOWN:

                    if Players[int(board.currentPlayer)] == False:
                        mouse_pos = pygame.mouse.get_pos()
                        if board.mouse_place_piece(mouse_pos):
                            check_canPlay = False
                            playerPlayTime[int(not board.currentPlayer)] = playerPlayTime[
                                                                               int(not board.currentPlayer)] + time.time() - playTime

            board.draw(WIN)
            pygame.display.update()


main()
