import pygame
from .button import *
from .board_variable import BLACK, WHITE, WIDTH, HEIGHT

main_font = ""  # Font utilisé sur tout le texte
button_size = HEIGHT//15  # Size de la police d'écriture

# Ecrire du texte centré en x y - Utilisé pour Othello et pour les indications


def write_text(surface, x, y, text, font, size, color=(0, 0, 0)):
    font = pygame.font.SysFont(font, size)  # charge la font
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    surface.blit(text_surface, text_rect)


# Les différents menu a render
def render_menu(menu_id, WIN, mouse):
    if (menu_id == 1):
        id = render_main_menu(WIN, mouse)

    if (menu_id == 2):
        id = render_versus_menu(WIN, mouse)

    if (menu_id == 4):
        id = render_PvAI_menu(WIN, mouse)

    if (menu_id == 5):
        id = render_FirstAIdifficulty_menu(WIN, mouse)

    if (menu_id == 6):
        id = render_AIdifficulty1_menu(WIN, mouse)

    if (menu_id == 7):
        id = render_AIdifficulty2_menu(WIN, mouse)

    if (menu_id == 14 or menu_id == 15 or menu_id == 16):
        id = render_SecondAIdifficulty_menu(menu_id, WIN, mouse)
    return id


# La gestion de tout les menus
def render_main_menu(WIN, mouse):
    id = 1
    # Création des instances de Button pour les boutons PLAY et QUIT
    play_button = Button(WIDTH/2, HEIGHT/3, "PLAY",
                         main_font, button_size, WHITE, BLACK)

    quit_button = Button(WIDTH/2, HEIGHT/3 + 4 * HEIGHT/10, "QUIT",
                         main_font, button_size, WHITE, BLACK)

    play_button.draw(WIN, mouse)
    quit_button.draw(WIN, mouse)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            id = 0
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Play
                if play_button.is_hovered:
                    id = 2
                # Quit
                if quit_button.is_hovered:
                    id = 0
    return id

# Menu 2 = Versus menu


def render_versus_menu(WIN, mouse):
    id = 2
    # Création des instances de Button pour les boutons PLAY et QUIT
    JvJ_button = Button(WIDTH/2, HEIGHT/3, "Player vs Player",
                        main_font, button_size, WHITE, BLACK)

    JvAI_button = Button(WIDTH/2, HEIGHT/3 + HEIGHT/10, "Player vs AI",
                         main_font, button_size, WHITE, BLACK)

    AIvAI_button = Button(WIDTH/2, HEIGHT/3 + 2*HEIGHT/10, "AI vs AI",
                          main_font, button_size, WHITE, BLACK)

    return_button = Button(WIDTH/2, HEIGHT/3 + 3 * HEIGHT/10, "BACK TO MAIN",
                           main_font, button_size, WHITE, BLACK)

    quit_button = Button(WIDTH/2, HEIGHT/3 + 4 * HEIGHT/10, "QUIT",
                         main_font, button_size, WHITE, BLACK)

    JvJ_button.draw(WIN, mouse)
    JvAI_button.draw(WIN, mouse)
    AIvAI_button.draw(WIN, mouse)
    return_button.draw(WIN, mouse)
    quit_button.draw(WIN, mouse)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            id = 0
        if event.type == pygame.MOUSEBUTTONDOWN:
            # PVP
            if JvJ_button.is_hovered:
                id = 3
            # PVAI
            if JvAI_button.is_hovered:
                id = 4
            # AIVAI
            if AIvAI_button.is_hovered:
                id = 5
            # BACK
            if return_button.is_hovered:
                id = 1
            # Quit
            if quit_button.is_hovered:
                id = 0
    return id


def render_PvAI_menu(WIN, mouse):
    id = 4
    write_text(WIN, WIDTH/2, HEIGHT/8 + HEIGHT/10,
               "Who is starting ? (Playing black)", main_font, button_size, BLACK)
    # Création des instances de Button pour les boutons PLAY et QUIT
    playerstarts_button = Button(WIDTH/2, HEIGHT/3, "Player starts",
                                 main_font, button_size, WHITE, BLACK)

    AIstarts_button = Button(WIDTH/2, HEIGHT/3 + HEIGHT/10, "AI starts",
                             main_font, button_size, WHITE, BLACK)

    return_button = Button(WIDTH/2, HEIGHT/3 + 3 * HEIGHT/10, "BACK TO MAIN",
                           main_font, button_size, WHITE, BLACK)

    quit_button = Button(WIDTH/2, HEIGHT/3 + 4 * HEIGHT/10, "QUIT",
                         main_font, button_size, WHITE, BLACK)

    playerstarts_button.draw(WIN, mouse)
    AIstarts_button.draw(WIN, mouse)
    return_button.draw(WIN, mouse)
    quit_button.draw(WIN, mouse)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            id = 0
        if event.type == pygame.MOUSEBUTTONDOWN:
            # PVP
            if playerstarts_button.is_hovered:
                id = 6
            # PVAI
            if AIstarts_button.is_hovered:
                id = 7
            # BACK
            if return_button.is_hovered:
                id = 1
            # Quit
            if quit_button.is_hovered:
                id = 0
    return id


def render_AIdifficulty1_menu(WIN, mouse):
    id = 6
    write_text(WIN, WIDTH/2, HEIGHT/8 + HEIGHT/10,
               "Set the IA strenght", main_font, button_size, BLACK)
    # Création des instances de Button pour les boutons PLAY et QUIT
    easy_button = Button(WIDTH/2, HEIGHT/3, "Easy",
                         main_font, button_size, WHITE, BLACK)

    medium_button = Button(WIDTH/2, HEIGHT/3 + HEIGHT/10, "Medium",
                           main_font, button_size, WHITE, BLACK)

    hard_button = Button(WIDTH/2, HEIGHT/3 + 2*HEIGHT/10, "Hard",
                         main_font, button_size, WHITE, BLACK)

    return_button = Button(WIDTH/2, HEIGHT/3 + 3 * HEIGHT/10, "BACK TO MAIN",
                           main_font, button_size, WHITE, BLACK)

    quit_button = Button(WIDTH/2, HEIGHT/3 + 4 * HEIGHT/10, "QUIT",
                         main_font, button_size, WHITE, BLACK)

    easy_button.draw(WIN, mouse)
    medium_button.draw(WIN, mouse)
    hard_button.draw(WIN, mouse)
    return_button.draw(WIN, mouse)
    quit_button.draw(WIN, mouse)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            id = 0
        if event.type == pygame.MOUSEBUTTONDOWN:
            # PVP
            if easy_button.is_hovered:
                id = 8
            # PVIA
            if medium_button.is_hovered:
                id = 9
            # PVIA
            if hard_button.is_hovered:
                id = 10
            # BACK
            if return_button.is_hovered:
                id = 1
            # Quit
            if quit_button.is_hovered:
                id = 0
    return id


def render_AIdifficulty2_menu(WIN, mouse):
    id = 7
    write_text(WIN, WIDTH/2, HEIGHT/8 + HEIGHT/10,
               "Set the IA strenght", main_font, button_size, BLACK)
    # Création des instances de Button pour les boutons PLAY et QUIT
    easy_button = Button(WIDTH/2, HEIGHT/3, "Easy",
                         main_font, button_size, WHITE, BLACK)

    medium_button = Button(WIDTH/2, HEIGHT/3 + HEIGHT/10, "Medium",
                           main_font, button_size, WHITE, BLACK)

    hard_button = Button(WIDTH/2, HEIGHT/3 + 2*HEIGHT/10, "Hard",
                         main_font, button_size, WHITE, BLACK)

    return_button = Button(WIDTH/2, HEIGHT/3 + 3 * HEIGHT/10, "BACK TO MAIN",
                           main_font, button_size, WHITE, BLACK)

    quit_button = Button(WIDTH/2, HEIGHT/3 + 4 * HEIGHT/10, "QUIT",
                         main_font, button_size, WHITE, BLACK)

    easy_button.draw(WIN, mouse)
    medium_button.draw(WIN, mouse)
    hard_button.draw(WIN, mouse)
    return_button.draw(WIN, mouse)
    quit_button.draw(WIN, mouse)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            id = 0
        if event.type == pygame.MOUSEBUTTONDOWN:
            # PVP
            if easy_button.is_hovered:
                id = 11
            # PVIA
            if medium_button.is_hovered:
                id = 12
            # PVIA
            if hard_button.is_hovered:
                id = 13
            # BACK
            if return_button.is_hovered:
                id = 1
            # Quit
            if quit_button.is_hovered:
                id = 0
    return id


def render_FirstAIdifficulty_menu(WIN, mouse):
    id = 5
    write_text(WIN, WIDTH/2, HEIGHT/8 + HEIGHT/10,
               "Set the strenght of the first (black) IA", main_font, button_size, BLACK)
    # Création des instances de Button pour les boutons PLAY et QUIT
    easy_button = Button(WIDTH/2, HEIGHT/3, "Easy",
                         main_font, button_size, WHITE, BLACK)

    medium_button = Button(WIDTH/2, HEIGHT/3 + HEIGHT/10, "Medium",
                           main_font, button_size, WHITE, BLACK)

    hard_button = Button(WIDTH/2, HEIGHT/3 + 2*HEIGHT/10, "Hard",
                         main_font, button_size, WHITE, BLACK)

    return_button = Button(WIDTH/2, HEIGHT/3 + 3 * HEIGHT/10, "BACK TO MAIN",
                           main_font, button_size, WHITE, BLACK)

    quit_button = Button(WIDTH/2, HEIGHT/3 + 4 * HEIGHT/10, "QUIT",
                         main_font, button_size, WHITE, BLACK)

    easy_button.draw(WIN, mouse)
    medium_button.draw(WIN, mouse)
    hard_button.draw(WIN, mouse)
    return_button.draw(WIN, mouse)
    quit_button.draw(WIN, mouse)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            id = 0
        if event.type == pygame.MOUSEBUTTONDOWN:
            # PVP
            if easy_button.is_hovered:
                id = 14
            # PVIA
            if medium_button.is_hovered:
                id = 15
            # PVIA
            if hard_button.is_hovered:
                id = 16
            # BACK
            if return_button.is_hovered:
                id = 1
            # Quit
            if quit_button.is_hovered:
                id = 0
    return id


def render_SecondAIdifficulty_menu(id_menu, WIN, mouse):
    id = id_menu
    write_text(WIN, WIDTH/2, HEIGHT/8 + HEIGHT/10,
               "Set the strength of the second (White) AI ", main_font, button_size, BLACK)
    # Création des instances de Button pour les boutons PLAY et QUIT
    easy_button = Button(WIDTH/2, HEIGHT/3, "Easy",
                         main_font, button_size, WHITE, BLACK)

    medium_button = Button(WIDTH/2, HEIGHT/3 + HEIGHT/10, "Medium",
                           main_font, button_size, WHITE, BLACK)

    hard_button = Button(WIDTH/2, HEIGHT/3 + 2*HEIGHT/10, "Hard",
                         main_font, button_size, WHITE, BLACK)

    return_button = Button(WIDTH/2, HEIGHT/3 + 3 * HEIGHT/10, "BACK TO MAIN",
                           main_font, button_size, WHITE, BLACK)

    quit_button = Button(WIDTH/2, HEIGHT/3 + 4 * HEIGHT/10, "QUIT",
                         main_font, button_size, WHITE, BLACK)

    easy_button.draw(WIN, mouse)
    medium_button.draw(WIN, mouse)
    hard_button.draw(WIN, mouse)
    return_button.draw(WIN, mouse)
    quit_button.draw(WIN, mouse)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            id = 0
        if event.type == pygame.MOUSEBUTTONDOWN:
            # PVP
            if easy_button.is_hovered:
                id = 17
            # PVIA
            if medium_button.is_hovered:
                id = 18
            # PVIA
            if hard_button.is_hovered:
                id = 19
            # BACK
            if return_button.is_hovered:
                id = 1
            # Quit
            if quit_button.is_hovered:
                id = 0
    return id
