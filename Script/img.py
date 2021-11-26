import pygame

place = {}
hero = {}
inventory_tab = {}

def image_load():
    place['home_town'] = pygame.image.load('../Image/Place/HomeTown.png')

    hero['left'] = pygame.image.load('../Image/Character/HeroLeft.png')
    hero['right'] = pygame.image.load('../Image/Character/HeroRight.png')
    hero['up'] = pygame.image.load('../Image/Character/HeroUp.png')
    hero['down'] = pygame.image.load('../Image/Character/HeroDown.png')

    inventory_tab['skill'] = pygame.image.load('../Image/SkillTab.png')
    inventory_tab['card'] = pygame.image.load('../Image/CardTab.png')
    inventory_tab['deck'] = pygame.image.load('../Image/DeckTab.png')
    inventory_tab['equip'] = pygame.image.load('../Image/EquipTab.png')
    inventory_tab['item'] = pygame.image.load('../Image/ItemTab.png')
