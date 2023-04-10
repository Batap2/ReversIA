import pygame

# Setup de base de la grille de jeu
WIDTH, HEIGHT = 800, 800  # Largeur et hauteur du board
SIZE = 8  # Taille du damier SIZE x SIZE
SQUARE_SIZE = WIDTH//SIZE  # Taille d'un coté d'une case

# Couleurs
GREY = (200, 200, 200)

BOARDGREEN = pygame.Color("#5B8C5A")
WHITEPAWN = pygame.Color("#FFEEDB")
BLACKPAWN = pygame.Color("#242328")