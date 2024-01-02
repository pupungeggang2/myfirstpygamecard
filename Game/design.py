import pygame

pygame.font.init()

class Font():
    title = pygame.font.Font('Font/neodgm.ttf', 60)
    place = pygame.font.Font('Font/neodgm.ttf', 32)
    normal_text_large = pygame.font.Font('Font/neodgm.ttf', 32)
    normal_text_small = pygame.font.Font('Font/neodgm.ttf', 24)
    card_energy = pygame.font.Font('Font/neodgm.ttf', 28)
    card_name = pygame.font.Font('Font/neodgm.ttf', 16)
    card_description = pygame.font.Font('Font/neodgm.ttf', 14)
    card_stat = pygame.font.Font('Font/neodgm.ttf', 24)

class Color():
    black = (0, 0, 0)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    yellow = (255, 255, 0)
    white = (255, 255, 255)
