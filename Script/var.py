screen = None

scene = 'title'

class Input():
    class Keyboard():
        enabled = True
        key = -1
        key_press = -1

class Camera():
    x = 0
    y = 0

class Field():
    place = 'home_town'

class Player_Field():
    position = [320, 400]
    face = 'down'

    moving = False
    moved = 0 

class Player_Info():
    level = 1
    exp = 0
    exp_max = 20

    skill_tree = []

    decks = {}

    class Inventory():
        card = []
        equip = []
        item = []

class Player_Battle():
    energy = 0
    energy_max = 0

    hand = []
    deck = []

class Enemy_Battle():
    AI_type = 0
