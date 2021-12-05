import pygame

place = {}
hero = {}
npc = {}
enemy = {}
inventory_tab = {}
card = {}
card_back = {}
card_image = {}
energy = {}
button = {}
misc = {}

def image_load():
    place['home_town'] = pygame.image.load('../Image/Place/HomeTown.png')
    place['field_1'] = pygame.image.load('../Image/Place/Field01.png')
    place['field_village'] = pygame.image.load('../Image/Place/FieldVillage.png')

    hero['left'] = pygame.image.load('../Image/Character/HeroLeft.png')
    hero['right'] = pygame.image.load('../Image/Character/HeroRight.png')
    hero['up'] = pygame.image.load('../Image/Character/HeroUp.png')
    hero['down'] = pygame.image.load('../Image/Character/HeroDown.png')

    enemy['enemy'] = pygame.image.load('../Image/Character/Enemy.png')

    inventory_tab['skill'] = pygame.image.load('../Image/SkillTab.png')
    inventory_tab['card'] = pygame.image.load('../Image/CardTab.png')
    inventory_tab['deck'] = pygame.image.load('../Image/DeckTab.png')
    inventory_tab['equip'] = pygame.image.load('../Image/EquipTab.png')
    inventory_tab['item'] = pygame.image.load('../Image/ItemTab.png')

    card['card_frame'] = pygame.image.load('../Image/Card/CardFrame.png')

    card_back['basic_1'] = pygame.image.load('../Image/Card/CardBack01.png')

    card_image[1000] = pygame.image.load('../Image/Card/HeroImage.png')
    card_image[1001] = pygame.image.load('../Image/Card/EnemyHero1001.png')
    card_image[10001] = pygame.image.load('../Image/Card/Card10001.png')
    card_image[10002] = pygame.image.load('../Image/Card/Card10002.png')
    card_image[10003] = pygame.image.load('../Image/Card/Card10003.png')
    card_image[10004] = pygame.image.load('../Image/Card/Card10004.png')
    card_image[20001] = pygame.image.load('../Image/Card/Card20001.png')

    energy['full'] = pygame.image.load('../Image/EnergyOrbFull.png')
    energy['empty'] = pygame.image.load('../Image/EnergyOrbEmpty.png')
    energy['void'] = pygame.image.load('../Image/EnergyOrbVoid.png')

    button['cancel'] = pygame.image.load('../Image/Button/Cancel.png')
    button['turn_end'] = pygame.image.load('../Image/Button/TurnEnd.png')
    
    misc['return'] = pygame.image.load('../Image/Return.png')
    misc['select_frame_card'] = pygame.image.load('../Image/SelectFrameCard.png')
    misc['select_frame'] = pygame.image.load('../Image/SelectFrame.png')
    misc['attack_frame'] = pygame.image.load('../Image/AttackFrame.png')