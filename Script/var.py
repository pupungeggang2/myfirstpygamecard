screen = None
FPS = 40

scene = 'title'
state = ''
state_inventory = ''
inventory_page = 0

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
    size = [1280, 1280]
    wall = []
    interaction = []
    connection = []

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
        card = [[1001, 2, 0], [1002, 2, 0]]
        equip = []
        item = []

class Player_Battle():
    energy = 0
    energy_max = 0

    hand = []
    deck = []

class Enemy_Battle():
    AI_type = 0
