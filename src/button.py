import pygame

offsetButton = 20  # Ecart entre le texte et le rectangle du bouton


class Button:
    def __init__(self, x, y, text, font, size, text_color, button_color):
        self.x = x
        self.y = y
        self.text = text
        self.font = font
        self.size = size
        self.text_color = text_color
        self.button_color = button_color
        self.is_hovered = False

    # Dessine bloc et le texte a l'interieur et gère la couleur selon le hover
    def draw(self, surface, mouse_pos):
        font = pygame.font.SysFont(self.font, self.size)
        text_surface = font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=(self.x, self.y))
        button_rect = text_rect.inflate(offsetButton, offsetButton)

        if button_rect.collidepoint(mouse_pos):
            self.is_hovered = True
            pygame.draw.rect(surface, self.text_color, button_rect)
            text_surface = font.render(self.text, True, self.button_color)
            surface.blit(text_surface, text_rect)
        else:
            self.is_hovered = False
            pygame.draw.rect(surface, self.button_color, button_rect)
            surface.blit(text_surface, text_rect)


class SizableButton:
    def __init__(self, x, y, text, font, fontSize, text_color, button_color, width, height):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.text = text
        self.font = font
        self.fontSize = fontSize
        self.text_color = text_color
        self.button_color = button_color
        self.is_hovered = False

    # Dessine bloc et le texte a l'interieur et gère la couleur selon le hover
    def draw(self, surface, mouse_pos):
        font = pygame.font.SysFont(self.font, self.fontSize)
        text_surface = font.render(self.text, True, self.text_color)
        rect = text_surface.get_rect(center=(self.x, self.y))

        rect1 = pygame.draw.rect(surface, self.button_color,
                         (self.x - self.width / 2, self.y - self.height / 2, self.width, self.height))

        if rect1.collidepoint(mouse_pos):
            self.is_hovered = True
            pygame.draw.rect(surface, self.text_color, (self.x - self.width/2, self.y - self.height/2, self.width, self.height))
            text_surface = font.render(self.text, True, self.button_color)
            surface.blit(text_surface, rect)
        else:
            self.is_hovered = False
            pygame.draw.rect(surface, self.button_color, (self.x - self.width/2, self.y - self.height/2, self.width, self.height))
            text_surface = font.render(self.text, True, self.text_color)
            surface.blit(text_surface, rect)
