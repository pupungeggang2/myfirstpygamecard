screen = None
FPS = 40

scene = 'title'
state = ''
state_inventory = ''
state_player = 'portrait'
inventory_page = 0
battle_input = ''

class Animation():
    place_box = False
    place_box_tick = 0
    place_box_rect = [40, -120, 240, 80]
    scene_transition = False
    scene_transition_tick = 0
    scene_transition_rect = [0, -800, 1280, 800]

class Input():
    mouse_enabled = True

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

    deck = [{'name' : 'basic_deck', 'back' : 'basic_1', 'card' : [[10001, 2, 0], [10002, 2, 0], [10003, 2, 0], [10004, 2, 0]]}]
    selected_deck = 0

    class Inventory():
        card = [[10001, 2, 0], [10002, 2, 0], [10003, 2, 0], [10004, 2, 0]]
        equip = []
        item = []

class Player_Battle():
    energy = 0
    energy_max = 0
    
    hand_change = [False, False, False]

    hand = []
    deck = []

    hand_pop = -1
    selected_card = -1
    battle_input_1 = -1
    battle_input_2 = -1

    valid_point = []

class Enemy_Battle():
    ID = 0
    AI_type = 0
    
class Battle():
    turn_number = 0
    field = [None, None, None, None, None, None, None, None, None, None, None, None, None, None]