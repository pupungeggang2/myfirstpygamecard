screen = None
FPS = 40

scene = 'title'
state = ''
state_inventory = ''
state_player = 'portrait'
inventory_page = 0

class Animation():
    place_box = False
    place_box_tick = 0
    place_box_rect = [40, -120, 240, 80]

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

    deck = [{'name' : 'basic_deck', 'back' : 'basic_1', 'card' : [[1001, 2, 0], [1002, 2, 0], [1003, 2, 0], [1004, 2, 0]]}]
    selected_deck = 0

    class Inventory():
        card = [[1001, 2, 0], [1002, 2, 0], [1003, 2, 0], [1004, 2, 0]]
        equip = []
        item = []

class Player_Battle():
    energy = 0
    energy_max = 0

    hand = []
    deck = []

class Enemy_Battle():
    ID = 0
    AI_type = 0
    
class Battle():
    turn_number = 0
    field = [None, None, None, None, None, None, None, None, None, None, None, None, None, None]