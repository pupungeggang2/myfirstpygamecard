import pygame

pygame.font.init()

class Font():
    title = pygame.font.SysFont('Arial', 60)
    place = pygame.font.SysFont('Arial', 32)
    normal_text_large = pygame.font.SysFont('Arial', 32)
    normal_text_small = pygame.font.SysFont('Arial', 24)
    card_energy = pygame.font.SysFont('Arial', 28)
    card_name = pygame.font.SysFont('Arial', 16)
    card_description = pygame.font.SysFont('Arial', 14)
    card_stat = pygame.font.SysFont('Arial', 24)

class Color():
    black = (0, 0, 0)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    yellow = (255, 255, 0)
    white = (255, 255, 255)
