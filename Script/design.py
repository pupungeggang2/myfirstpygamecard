import pygame

pygame.font.init()

class Font():
    title = pygame.font.SysFont('Arial', 60)
    place = pygame.font.SysFont('Arial', 32)
    card_energy = pygame.font.SysFont('Arial', 28)
    card_name = pygame.font.SysFont('Arial', 16)
    card_description = pygame.font.SysFont('Arial', 16)
    card_stat = pygame.font.SysFont('Arial', 24)

class Color():
    black = (0, 0, 0)
    white = (255, 255, 255)
