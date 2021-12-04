import random

import var
import carddata as cd
import herodata as hd

def battle_init():
    var.Battle.field = [None, None, None, None, None, None, None, None, None, None, None, None, None, None]
    var.Battle.field[0] = {'ID' : 1000, 'name' : 'Hero', 'type' : 'hero', 'element' : 'normal', 'rarity' : 'basic', 'energy' : 0, 'stat' : [0, 20, 20], 'effect' : '', 'status' : ''}
    tmp_ID = var.Enemy_Battle.ID
    var.Battle.field[7] = {'ID' : var.Enemy_Battle.ID,
                           'name' : hd.enemy_hero[tmp_ID]['name'],
                           'type' : 'hero',
                           'element' : hd.enemy_hero[tmp_ID]['element'],
                           'rarity' : hd.enemy_hero[tmp_ID]['rarity'],
                           'energy' : 0,
                           'stat' : [0, hd.enemy_hero[tmp_ID]['life'], hd.enemy_hero[tmp_ID]['life']],
                           'effect' : '',
                           'status' : ''}

    var.Player_Battle.hand_change = [False, False, False]
    var.Battle.turn_number = 0
    var.Player_Battle.energy = 0
    var.Player_Battle.energy_max = 0

    battle_deck_generate()
    player_deck_shuffle()

def battle_deck_generate():
    var.Player_Battle.deck = []

    for i in range(len(var.Player_Info.deck[var.Player_Info.selected_deck]['card'])):
        for j in range(var.Player_Info.deck[var.Player_Info.selected_deck]['card'][i][1]):
            tmp_ID = var.Player_Info.deck[var.Player_Info.selected_deck]['card'][i][0]
            tmp_card = {'ID' : var.Player_Info.deck[var.Player_Info.selected_deck]['card'][i][0],
                        'name' : cd.card[tmp_ID]['name'],
                        'type' : cd.card[tmp_ID]['type'],
                        'element' : cd.card[tmp_ID]['element'],
                        'rarity' : cd.card[tmp_ID]['rarity'],
                        'energy' : cd.card[tmp_ID]['energy'],
                        'stat' : [cd.card[tmp_ID]['stat'][0], cd.card[tmp_ID]['stat'][1]],
                        'effect' : cd.card[tmp_ID]['effect'],
                        'play' : [cd.card[tmp_ID]['play'][0], cd.card[tmp_ID]['play'][1], cd.card[tmp_ID]['play'][2]],
                        'description' : cd.card_description[tmp_ID]}
            var.Player_Battle.deck.append(tmp_card)

def player_deck_shuffle():
    tmp_deck = []

    for i in range(len(var.Player_Battle.deck)):
        tmp_card = var.Player_Battle.deck[i]
        tmp_deck.append(tmp_card)
        tmp_card = {}

    var.Player_Battle.deck = []

    while len(tmp_deck) > 0:
        tmp_index = random.randint(0, len(tmp_deck) - 1)
        var.Player_Battle.deck.append(tmp_deck.pop(tmp_index))

def start_hand_change():
    if len(var.Player_Battle.deck) >= 6:
        for i in range(3):
            if var.Player_Battle.hand_change[i] == True:
                tmp_card = var.Player_Battle.deck[i]
                var.Player_Battle.deck[i] = var.Player_Battle.deck[i + 3]
                var.Player_Battle.deck[i + 3] = tmp_card

def start_of_battle():
    var.Player_Battle.energy_max = 0 
    var.Player_Battle.energy = var.Player_Battle.energy_max
    
    for i in range(3):
        draw_card_from_deck()

    turn_start()

def turn_start():
    var.state = 'your_turn'

    var.Battle.turn_number += 1

    if var.Player_Battle.energy_max < 8:
        var.Player_Battle.energy_max += 1

    var.Player_Battle.energy = var.Player_Battle.energy_max

    draw_card_from_deck()

def draw_card_from_deck():
    if len(var.Player_Battle.deck) > 0:
        tmp_card = var.Player_Battle.deck.pop(0)

        if len(var.Player_Battle.hand) < 8:
            var.Player_Battle.hand.append(tmp_card)

def valid_point_generate(card):
    var.Player_Battle.valid_point = []

    if card['play'] == ['u', 'pe', '']:
        for i in range(7):
            if var.Battle.field[i] == None:
                var.Player_Battle.valid_point.append(i)

def card_play_validation_check(card):
    if var.Player_Battle.energy < card['energy']:
        return False

    if card['play'] == ['u', 'pe', '']:
        for i in range(len(var.Player_Battle.valid_point)):
            if var.Player_Battle.battle_input_1 == var.Player_Battle.valid_point[i]:
                break

            if i == len(var.Player_Battle.valid_point) - 1:
                return False

    return True

def card_play(card, input):
    var.Player_Battle.energy -= card['energy']

    if card['play'] == ['u', 'pe', '']:
        tmp_unit = {'ID' : card['ID'],
                    'type' : card['type'],
                    'name' : card['name'],
                    'element' : card['element'],
                    'rarity' : card['rarity'],
                    'energy' : card['energy'],
                    'stat' : [card['stat'][0], card['stat'][1], card['stat'][1]],
                    'effect' : card['effect'],
                    'attack' : 0}
        summon_unit(tmp_unit, input)

def card_release():
    var.battle_input = ''
    var.Player_Battle.selected_card = -1
    var.Player_Battle.hand_pop = -1
    var.Player_Battle.valid_point = []

def summon_unit(unit, position):
    if var.Battle.field[position] == None:
        var.Battle.field[position] = unit
