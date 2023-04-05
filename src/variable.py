import pygame

# Setup de base de la grille de jeu
WIDTH, HEIGHT = 800, 800  # Largeur et hauteur du board
SIZE = 8  # Taille du damier SIZE x SIZE
SQUARE_SIZE = WIDTH//SIZE  # Taille d'un coté d'une case

# Couleurs
COLOR = (35, 180, 35)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (125, 125, 125)

# 0 = count
HEURISTIC_MODE = 0