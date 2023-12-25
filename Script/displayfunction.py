import pygame
import img

import UI
import design

import var
import shop
import carddata as cd

def place_animation_handle():
    if var.Animation.place_box == True:
        var.Animation.place_box_tick += 1
        
        if var.Animation.place_box_tick > 0 and var.Animation.place_box_tick <= 1 * var.FPS :
            var.Animation.place_box_rect[1] += 160 / var.FPS

        elif var.Animation.place_box_tick > 2 * var.FPS and var.Animation.place_box_tick <= 3 * var.FPS:
            var.Animation.place_box_rect[1] -= 160 / var.FPS

        elif var.Animation.place_box_tick >= 3 * var.FPS:
            var.Animation.place_box = False
            var.Animation.place_box_tick = 0
            var.Animation.place_box_rect = [40, -120, 240, 80]

def screen_transition_to_battle_handle():
    if var.Animation.scene_transition == True:
        var.Animation.scene_transition_tick += 1
        var.Animation.scene_transition_rect[1] += 1600 / 2 / var.FPS

        if var.Animation.scene_transition_tick >= 2 * var.FPS:
            var.Animation.scene_transition = False
            var.Animation.scene_transition_tick = 0
            var.Animation.scene_transition_rect = [0, -800, 1280, 800]
            var.Input.mouse_enabled = True
            var.Input.Keyboard.enabled = True

def screen_transition_to_field_handle():
    if var.Animation.scene_transition_field == True:
        var.Animation.scene_transition_field_tick += 1
        var.Animation.scene_transition_field_rect[1] += 1600 / 2 / var.FPS

        if var.Animation.scene_transition_field_tick >= 2 * var.FPS:
            var.Animation.scene_transition_field = False
            var.Animation.scene_transition_field_tick = 0
            var.Animation.scene_transition_field_rect = [0, -800, 1280, 800]
            var.Input.mouse_enabled = True
            var.Input.Keyboard.enabled = True

def attack_animation_handle():
    if var.Animation.attack == True:
        var.Animation.attack_tick += 1
    
        if var.Animation.attack_tick >= 0 and var.Animation.attack_tick < 0.5 * var.FPS:
            full_tick = 0.5 * var.FPS
            var.Animation.attack_frame = int(var.Animation.attack_tick / full_tick * 8)

        elif var.Animation.attack_tick >= 0.5 * var.FPS and var.Animation.attack_tick < 1 * var.FPS:
            full_tick = 0.5 * var.FPS
            tick_shift = 0.5  * var.FPS
            var.Animation.attack_frame = int((var.Animation.attack_tick - tick_shift) / full_tick * 8)

        elif var.Animation.attack_tick >= 1 * var.FPS:
            var.Animation.attack_tick = 0
            var.Animation.attack = False

def place_display():
    pygame.draw.rect(var.screen, design.Color.white, var.Animation.place_box_rect)
    pygame.draw.rect(var.screen, design.Color.black, var.Animation.place_box_rect, 2)
    var.screen.blit(design.Font.place.render(var.Field.place, True, design.Color.black), [var.Animation.place_box_rect[0] + 2, var.Animation.place_box_rect[1] + 20])

def terrain_display():
    var.screen.blit(img.place[var.Field.place], [0 - var.Camera.x, 0 - var.Camera.y])

def interaction_display():
    for i in range(len(var.Field.interaction)):
        var.screen.blit(img.misc['interaction'], [var.Field.interaction[i][0][0] - var.Camera.x, var.Field.interaction[i][0][1] - var.Camera.y])

def player_display():
    var.screen.blit(img.hero[var.Player_Field.face], [var.Player_Field.position[0] - var.Camera.x, var.Player_Field.position[1] - var.Camera.y])

def enemy_display():
    for i in range(len(var.Field.enemy)):
        var.screen.blit(img.enemy['enemy'], [var.Field.enemy[i][0][0] - var.Camera.x, var.Field.enemy[i][0][1] - var.Camera.y])

def scene_transtition_display():
    pygame.draw.rect(var.screen, design.Color.black, var.Animation.scene_transition_rect)

def scene_transtition_field_display():
    pygame.draw.rect(var.screen, design.Color.black, var.Animation.scene_transition_field_rect)

def draw_card(card, position):
    var.screen.blit(img.card['card_frame'], position)
    var.screen.blit(img.card_image[card['ID']], [position[0] + UI.Card.image_position[0], position[1] + UI.Card.image_position[1]] , UI.Card.image)

    var.screen.blit(design.Font.card_energy.render(str(card['energy']), True, design.Color.black), [position[0] + UI.Card.energy_text[0], position[1] + UI.Card.energy_text[1]])
    var.screen.blit(design.Font.card_name.render(str(card['name']), True, design.Color.black), [position[0] + UI.Card.name_text[0], position[1] + UI.Card.name_text[1]])
    var.screen.blit(design.Font.card_description.render(str(card['description']), True, design.Color.black), [position[0] + UI.Card.description_text[0], position[1] + UI.Card.description_text[1]])
    var.screen.blit(design.Font.card_stat.render(str(card['stat'][0]) + '/' + str(card['stat'][1]), True, design.Color.black), [position[0] + UI.Card.stat_text[0], position[1] + UI.Card.stat_text[1]])

def battle_title_display():
    if var.state == 'your_turn':
        var.screen.blit(design.Font.title.render('Your Turn', True, design.Color.black), UI.Battle.title_text)

    elif var.state == 'enemy_turn':
        var.screen.blit(design.Font.title.render('Enemy Turn', True, design.Color.black), UI.Battle.title_text)

def battle_unit_display(unit, position):
    var.screen.blit(img.card_image[unit['ID']], position)
    pygame.draw.rect(var.screen, design.Color.yellow, [position[0] + UI.Battle.Field.stat_box[0], position[1] + UI.Battle.Field.stat_box[1], UI.Battle.Field.stat_box[2], UI.Battle.Field.stat_box[3]])
    var.screen.blit(design.Font.card_stat.render(str(unit['stat'][0]) + '/' + str(unit['stat'][1]), True, design.Color.black), [position[0] + UI.Battle.Field.stat_text[0], position[1] + UI.Battle.Field.stat_text[1]])

def inventory_display():
    pygame.draw.rect(var.screen, design.Color.white, UI.Field.Inventory.player_info)
    pygame.draw.rect(var.screen, design.Color.black, UI.Field.Inventory.player_info, 2)

    #var.screen.blit(img.inventory_tab['skill'], UI.Field.Inventory.skill_tab)
    var.screen.blit(img.inventory_tab['card'], UI.Field.Inventory.card_tab)
    var.screen.blit(img.inventory_tab['deck'], UI.Field.Inventory.deck_tab)
    #var.screen.blit(img.inventory_tab['equip'], UI.Field.Inventory.equip_tab)
    #var.screen.blit(img.inventory_tab['item'], UI.Field.Inventory.item_tab)
    var.screen.blit(img.inventory_tab['map'], UI.Field.Inventory.map_tab)

    pygame.draw.rect(var.screen, design.Color.white, UI.Field.Inventory.content)
    pygame.draw.rect(var.screen, design.Color.black, UI.Field.Inventory.content, 2)

    if var.state_inventory != 'deck' and var.state_inventory != 'deck_edit' and var.state_inventory != 'deck_create':
        player_profile_display()

    if var.state_inventory == 'card':
        inventory_card_display()

    elif var.state_inventory == 'deck':
        inventory_deck_display()

    elif var.state_inventory == 'map':
        inventory_map_display()

    elif var.state_inventory == 'deck_edit' or var.state_inventory == 'deck_create':
        deck_edit_display(var.Player_Info.deck_tmp)

def player_profile_display():
    var.screen.blit(img.card_image[1000], UI.Field.Inventory.player_profile_image)
    var.screen.blit(design.Font.normal_text_large.render('Lv.' + str(var.Player_Info.level), True, design.Color.black), UI.Field.Inventory.player_level_text)
    exp_percentage = int(var.Player_Info.exp / var.Player_Info.exp_max * 100)
    var.screen.blit(design.Font.normal_text_large.render('Exp : ' + str(var.Player_Info.exp) + 
    '/' + str(var.Player_Info.exp_max) + ' ' + str(exp_percentage) + '%', True, design.Color.black), UI.Field.Inventory.player_exp_text)
    var.screen.blit(img.bar['exp_empty'], UI.Field.Inventory.player_exp_bar)
    var.screen.blit(img.bar['exp_full'], UI.Field.Inventory.player_exp_bar, [0, 0, int(320 * exp_percentage / 100), 80])
    var.screen.blit(img.misc['gold'], UI.Field.Inventory.gold_image)
    var.screen.blit(design.Font.normal_text_large.render(str(var.Player_Info.gold), True, design.Color.black), UI.Field.Inventory.player_gold_text)

def inventory_card_display():
    for i in range(8):
        if var.inventory_page * 8 + i < len(var.Player_Info.Inventory.card):
            tmp_ID = var.Player_Info.Inventory.card[var.inventory_page * 8 + i][0]
            tmp_card = {'ID' : var.Player_Info.Inventory.card[var.inventory_page * 8 + i][0],
                        'name' : cd.card[tmp_ID]['name'],
                        'type' : cd.card[tmp_ID]['type'],
                        'element' : cd.card[tmp_ID]['element'],
                        'rarity' : cd.card[tmp_ID]['rarity'],
                        'energy' : cd.card[tmp_ID]['energy'],
                        'stat' : [cd.card[tmp_ID]['stat'][0], cd.card[tmp_ID]['stat'][1]],
                        'effect' : cd.card[tmp_ID]['effect'],
                        'description' : cd.card_description[tmp_ID],
                        'play' : [cd.card[tmp_ID]['play'][0], cd.card[tmp_ID]['play'][1], cd.card[tmp_ID]['play'][2]]}
            draw_card(tmp_card, UI.Field.Inventory.card_list[i][:2])

def inventory_deck_display():
    for i in range(8):
        if i < len(var.Player_Info.deck):
            var.screen.blit(img.card_back[var.Player_Info.deck[i]['back']], UI.Field.Inventory.card_list[i][:2])
            var.screen.blit(design.Font.card_name.render(var.Player_Info.deck[i]['name'], True, design.Color.black), UI.Field.Inventory.deck_text[i])

    var.screen.blit(img.misc['add'], UI.Field.Inventory.add_tab)
    var.screen.blit(img.misc['remove'], UI.Field.Inventory.remove_tab)
    var.screen.blit(img.misc['ok_small'], UI.Field.Inventory.ok_tab)

    if var.Player_Info.selected_deck != -1 and var.Player_Info.selected_deck < len(var.Player_Info.deck):
        deck_display(var.Player_Info.deck[var.Player_Info.selected_deck])

    if var.Player_Info.selected_deck != -1:
        var.screen.blit(img.misc['select_frame_card'], UI.Field.Inventory.card_list[var.Player_Info.selected_deck])

def inventory_map_display():
    var.screen.blit(img.place['map'], UI.Field.Inventory.map)

    var.map_surface = pygame.Surface(UI.map_places[var.Field.place][2:])
    var.map_surface.set_alpha(128)
    var.map_surface.fill(design.Color.green)
    var.screen.blit(var.map_surface, UI.map_places[var.Field.place][:2])

def deck_edit_display(deck):
    inventory_card_display()
    deck_display(deck)

    pygame.draw.rect(var.screen, design.Color.white, UI.Field.Inventory.deck_temp_name_rect)
    pygame.draw.rect(var.screen, design.Color.black, UI.Field.Inventory.deck_temp_name_rect, 2)
    var.screen.blit(design.Font.normal_text_large.render(var.Player_Info.deck_tmp['name'], True, design.Color.black), UI.Field.Inventory.deck_temp_name_text)

    var.screen.blit(img.misc['ok_small'], UI.Field.Inventory.add_tab)
    var.screen.blit(img.misc['cancel_small'], UI.Field.Inventory.remove_tab)

def deck_display(deck):
    for i in range(8):
        if i < len(deck['card']):
            pygame.draw.rect(var.screen, design.Color.black, UI.Field.Inventory.deck_card_list[i], 2)
            tmp_txt = str(cd.card[deck['card'][i][0]]['energy']) + '. ' + cd.card[deck['card'][i][0]]['name']
            var.screen.blit(design.Font.card_name.render(tmp_txt, True, design.Color.black), UI.Field.Inventory.deck_card_name_text[i])
            var.screen.blit(design.Font.card_name.render('x' + str(deck['card'][i][1]), True, design.Color.black), UI.Field.Inventory.deck_card_amount_text[i])

def shop_display():
    pygame.draw.rect(var.screen, design.Color.white, UI.Field.Shop.rect)
    pygame.draw.rect(var.screen, design.Color.black, UI.Field.Shop.rect, 2)

    for i in range(5):
        pygame.draw.rect(var.screen, design.Color.black, UI.Field.Shop.item_list[i], 2)
        pygame.draw.rect(var.screen, design.Color.black, UI.Field.Shop.buy_button[i], 2)

        if i < len(shop.shop[var.Field.shop_ID]['item_list']):
            tmp_ID = shop.shop[var.Field.shop_ID]['item_list'][i]['ID']
            
            if shop.shop[var.Field.shop_ID]['item_list'][i]['sold'] == False:
                pygame.draw.rect(var.screen, design.Color.green, UI.Field.Shop.buy_button[i])

            else:
                pygame.draw.rect(var.screen, design.Color.red, UI.Field.Shop.buy_button[i])

            var.screen.blit(img.misc['gold'], UI.Field.Shop.item_gold_image[i])
            var.screen.blit(design.Font.normal_text_large.render(shop.item[tmp_ID]['name'], True, design.Color.black), UI.Field.Shop.item_name_text[i])
            var.screen.blit(design.Font.normal_text_large.render(str(shop.item[tmp_ID]['gold']), True, design.Color.black), UI.Field.Shop.item_gold_text[i])

        var.screen.blit(img.misc['gold'], UI.Field.Shop.gold_image)
        var.screen.blit(design.Font.normal_text_large.render(str(var.Player_Info.gold), True, design.Color.black), UI.Field.Shop.player_gold_text)

def battle_start_display():
    pygame.draw.rect(var.screen, design.Color.white, UI.Battle.Start.rect)
    pygame.draw.rect(var.screen, design.Color.black, UI.Battle.Start.rect, 2)
    
    for i in range(3):
        draw_card(var.Player_Battle.deck[i], UI.Battle.Start.card[i][:2])

    for i in range(3):
        if var.state == 'start':
            if var.Player_Battle.hand_change[i] == True:
                var.screen.blit(img.misc['return'], UI.Battle.Start.card[i][:2])

    pygame.draw.rect(var.screen, design.Color.yellow, UI.Battle.Start.start_button)
    pygame.draw.rect(var.screen, design.Color.black, UI.Battle.Start.start_button, 2)
    var.screen.blit(design.Font.normal_text_large.render('OK', False, design.Color.black), UI.Battle.Start.start_text)

def battle_result_display():
    pygame.draw.rect(var.screen, design.Color.white, UI.Battle.Result.rect)
    pygame.draw.rect(var.screen, design.Color.black, UI.Battle.Result.rect, 2)

    var.screen.blit(design.Font.normal_text_large.render('You gained ' + str(var.Battle.exp_gain) + 'EXP!', True, design.Color.black), UI.Battle.Result.exp_text)
    var.screen.blit(design.Font.normal_text_large.render('You gained ' + str(var.Battle.gold_gain) + 'gold!', True, design.Color.black), UI.Battle.Result.gold_text)

    pygame.draw.rect(var.screen, design.Color.yellow, UI.Battle.Result.button)
    pygame.draw.rect(var.screen, design.Color.black, UI.Battle.Result.button, 2)
    var.screen.blit(design.Font.normal_text_large.render('Continue', True, design.Color.black), UI.Battle.Result.continue_text)

def battle_field_display():
    for i in range(14):
        pygame.draw.rect(var.screen, design.Color.black, UI.Battle.Field.cell_list[i], 2)

        if var.Battle.field[i] != None:
            battle_unit_display(var.Battle.field[i], UI.Battle.Field.cell_list[i])

            if var.Battle.field[i]['attack'] > 0:
                var.screen.blit(img.misc['attack_frame'], UI.Battle.Field.cell_list[i][:2])

    for i in range(len(var.Player_Battle.valid_point)):
        pos = var.Player_Battle.valid_point[i]
        var.screen.blit(img.misc['select_frame'], UI.Battle.Field.cell_list[pos])

    if var.Animation.attack == True:
        if var.Animation.attack_tick >= 0 and var.Animation.attack_tick < 0.5 * var.FPS:
            var.screen.blit(img.animation['attack'][var.Animation.attack_frame], UI.Battle.Field.cell_list[var.Animation.attack_position_2])

        elif var.Animation.attack_tick >= 0.5 * var.FPS and var.Animation.attack_tick < 1 * var.FPS:
            var.screen.blit(img.animation['attack'][var.Animation.attack_frame], UI.Battle.Field.cell_list[var.Animation.attack_position_1])

def battle_hand_display():
    for i in range(len(var.Player_Battle.hand)):
        if i != var.Player_Battle.hand_pop:
            draw_card(var.Player_Battle.hand[i], UI.Battle.player_hand[i])

    if var.Player_Battle.hand_pop != -1:
        draw_card(var.Player_Battle.hand[var.Player_Battle.hand_pop], UI.Battle.player_hand_pop[var.Player_Battle.hand_pop][:2])

    if var.battle_input == 'card_selected':
        var.screen.blit(img.misc['select_frame_card'], UI.Battle.player_hand_pop[var.Player_Battle.selected_card])

def battle_card_back_display():
    if len(var.Player_Battle.deck) > 0:
        var.screen.blit(img.card_back['basic_1'], UI.Battle.player_card_back[0])

    if len(var.Player_Battle.deck) > 3:
        var.screen.blit(img.card_back['basic_1'], UI.Battle.player_card_back[1])

    if len(var.Player_Battle.deck) > 6:
        var.screen.blit(img.card_back['basic_1'], UI.Battle.player_card_back[2])

    if len(var.Player_Battle.deck) > 9:
        var.screen.blit(img.card_back['basic_1'], UI.Battle.player_card_back[3])

    if len(var.Player_Battle.deck) > 12:
        var.screen.blit(img.card_back['basic_1'], UI.Battle.player_card_back[4])

def energy_orb_display():
    for i in range(8):
        if i < var.Player_Battle.energy:
            var.screen.blit(img.energy['full'], UI.Battle.energy_orb[i])

        elif i < var.Player_Battle.energy_max:
            var.screen.blit(img.energy['empty'], UI.Battle.energy_orb[i])

        else:
            var.screen.blit(img.energy['void'], UI.Battle.energy_orb[i])

def button_display():
    var.screen.blit(img.button['cancel'], UI.Battle.cancel)
    var.screen.blit(img.button['turn_end'], UI.Battle.turn_end)