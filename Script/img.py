import pygame

place = {}
hero = {}

def image_load():
    place['home_town'] = pygame.image.load('../Image/Place/HomeTown.png')

    hero['left'] = pygame.image.load('../Image/Character/HeroLeft.png')
    hero['right'] = pygame.image.load('../Image/Character/HeroRight.png')
    hero['up'] = pygame.image.load('../Image/Character/HeroUp.png')
    hero['down'] = pygame.image.load('../Image/Character/HeroDown.png')
