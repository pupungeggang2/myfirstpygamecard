import var

import shop
import carddata as cd
import fielddata as fd

def field_load(place):
    var.Field.place = place
    var.Field.size = [fd.size[place][0], fd.size[place][1]]
    var.Field.wall = []
    var.Field.interaction = []
    var.Field.connection = []
    var.Field.enemy = []
    temp = []
    
    for i in range(len(fd.wall[place])):
        temp = []
        
        for j in range(len(fd.wall[place][i])):
            temp.append(fd.wall[place][i][j])

        var.Field.wall.append(temp)

    for i in range(len(fd.connection[place])):
        var.Field.connection.append([[fd.connection[place][i][0][0], fd.connection[place][i][0][1], fd.connection[place][i][0][2], fd.connection[place][i][0][3]], fd.connection[place][i][1], fd.connection[place][i][2], [fd.connection[place][i][3][0], fd.connection[place][i][3][1]]])

    for i in range(len(fd.interaction[place])):
        var.Field.interaction.append([[fd.interaction[place][i][0][0], fd.interaction[place][i][0][1]], fd.interaction[place][i][1], fd.interaction[place][i][2]])

    for i in range(len(fd.enemy[place])):
        var.Field.enemy.append([[fd.enemy[place][i][0][0], fd.enemy[place][i][0][1]], fd.enemy[place][i][1]])

def collision_check():
    player_row = var.Player_Field.position[1] // 80
    player_column = var.Player_Field.position[0] // 80

    direction = {'left' : [0, -1], 'right' : [0, 1], 'up' : [-1, 0], 'down' : [1, 0]}

    target_position = [player_row + direction[var.Player_Field.face][0], player_column + direction[var.Player_Field.face][1]]

    if target_position[0] < 0 or target_position[0] >= len(var.Field.wall) or target_position[1] < 0 or target_position[1] >= len(var.Field.wall[0]):
        return True

    if var.Field.wall[target_position[0]][target_position[1]] == 0:
        return False

    return True

def field_move():
    for i in range(len(var.Field.connection)):
        if var.Player_Field.position[0] >= var.Field.connection[i][0][0] and var.Player_Field.position[0] <= var.Field.connection[i][0][2] and var.Player_Field.position[1] >= var.Field.connection[i][0][1] and var.Player_Field.position[1] <= var.Field.connection[i][0][3]:
            if var.Player_Field.face == var.Field.connection[i][1]:
                if var.Field.connection[i][3][0] == -1:
                    var.Player_Field.position[0] += 0

                elif var.Field.connection[i][3][0] == -2:
                    var.Player_Field.position[0] -= 1280

                elif var.Field.connection[i][3][0] == -3:
                    var.Player_Field.position[0] += 1280

                else:
                    var.Player_Field.position[0] = var.Field.connection[i][3][0]

                if var.Field.connection[i][3][1] == -1:
                    var.Player_Field.position[1] += 0

                elif var.Field.connection[i][3][1] == -2:
                    var.Player_Field.position[1] -= 1280

                elif var.Field.connection[i][3][1] == -3:
                    var.Player_Field.position[1] += 1280

                else:
                    var.Player_Field.position[1] = var.Field.connection[i][3][1]

                var.Field.place = var.Field.connection[i][2]
                field_load(var.Field.place)
                var.Animation.place_box = True
                var.Animation.place_box_tick = 0
                var.Animation.place_box_rect = [40, -120, 240, 80]

                break

def tmp_deck_copy():
    var.Player_Info.deck_tmp = {}
    var.Player_Info.deck_tmp['name'] = var.Player_Info.deck[var.Player_Info.selected_deck]['name']
    var.Player_Info.deck_tmp['back'] = 'basic_1'
    var.Player_Info.deck_tmp['card'] = []

    for i in range(len(var.Player_Info.deck[var.Player_Info.selected_deck]['card'])):
        var.Player_Info.deck_tmp['card'].append([var.Player_Info.deck[var.Player_Info.selected_deck]['card'][i][0], var.Player_Info.deck[var.Player_Info.selected_deck]['card'][i][1], var.Player_Info.deck[var.Player_Info.selected_deck]['card'][i][2]])

def add_card_to_deck(card_ID):
    if len(var.Player_Info.deck_tmp['card']) == 0:
        var.Player_Info.deck_tmp['card'].append([card_ID, 1, 0])

    else:
        for i in range(len(var.Player_Info.deck_tmp['card'])):
            if card_ID == var.Player_Info.deck_tmp['card'][i][0]:
                if var.Player_Info.deck_tmp['card'][i][1] < 2:
                    var.Player_Info.deck_tmp['card'][i][1] += 1
                break

            if i == len(var.Player_Info.deck_tmp['card']) - 1:
                var.Player_Info.deck_tmp['card'].append([card_ID, 1, 0])
                tmp_deck_sort()

def remove_card_from_deck(position):
    if var.Player_Info.deck_tmp['card'][position][1] == 1:
        var.Player_Info.deck_tmp['card'].pop(position)

    else:
        var.Player_Info.deck_tmp['card'][position][1] -= 1

def tmp_deck_sort():
    for i in range(len(var.Player_Info.deck_tmp['card']) - 1, 0, -1):
        for j in range(0, i):
            energy_1 = cd.card[var.Player_Info.deck_tmp['card'][j][0]]['energy']
            energy_2 = cd.card[var.Player_Info.deck_tmp['card'][j + 1][0]]['energy']
            
            if energy_1 > energy_2 or (energy_1 == energy_2 and var.Player_Info.deck_tmp['card'][j][0] > var.Player_Info.deck_tmp['card'][j + 1][0]):
                tmp = var.Player_Info.deck_tmp['card'][j]
                var.Player_Info.deck_tmp['card'][j] = var.Player_Info.deck_tmp['card'][j + 1]
                var.Player_Info.deck_tmp['card'][j + 1] = tmp

def deck_save(add_mode):
    if add_mode == 1:
        var.Player_Info.deck.append(var.Player_Info.deck_tmp)

    else:
        var.Player_Info.deck[var.Player_Info.selected_deck] = var.Player_Info.deck_tmp

    var.Player_Info.deck_tmp = {'name' : '', 'back' : 'basic_1', 'card' : []}
    var.state_inventory = 'deck'
    var.Player_Info.selected_deck = -1

def deck_discard():
    var.Player_Info.deck_tmp = {'name' : '', 'back' : 'basic_1', 'card' : []}
    var.state_inventory = 'deck'
    var.Player_Info.selected_deck = -1

def interaction_handle():
    for i in range(len(var.Field.interaction)):
        if var.Player_Field.position[0] == var.Field.interaction[i][0][0] and var.Player_Field.position[1] == var.Field.interaction[i][0][1]:
            if var.Field.interaction[i][1] == 'shop':
                var.state = 'shop'
                var.Field.shop_ID = var.Field.interaction[i][2]

def buy_item(shop_position):
    if shop_position < len(shop.shop[var.Field.shop_ID]['item_list']):
        tmp_item = shop.item[shop.shop[var.Field.shop_ID]['item_list'][shop_position]['ID']]

        if var.Player_Info.gold >= tmp_item['gold'] and shop.shop[var.Field.shop_ID]['item_list'][shop_position]['sold'] == False:
            var.Player_Info.gold -= tmp_item['gold']
            shop.shop[var.Field.shop_ID]['item_list'][shop_position]['sold'] = True

            if tmp_item['type'] == 'card':
                var.Player_Info.Inventory.card.append([tmp_item['item_ID'], 2, 0])