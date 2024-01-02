import pygame

import UI
import design

import battlefunction as bf
import displayfunction as df
import inputfunction as iff

import var

import start

def manage():
    if var.Animation.scene_transition_field == True:
        df.screen_transition_to_field_handle()

    if var.battle_input == '':
        card_pop_handle()

    if var.Animation.scene_transition == True:
        df.screen_transition_to_battle_handle()

    if var.Animation.attack == True:
        df.attack_animation_handle()

    if var.state == 'enemy_turn':
        bf.enemy_AI_handle()
        
    scene_change_field()
    display()

def display():
    var.screen.fill(design.Color.white)

    df.battle_title_display()
    df.battle_field_display()

    df.battle_card_back_display()
    df.button_display()
    df.battle_hand_display()
    df.energy_orb_display()

    if var.state == 'start' or var.state == 'start_confirm':
        df.battle_start_display()

    if var.state == 'result':
        df.battle_result_display()

    df.scene_transtition_display()
    df.scene_transtition_field_display()

    pygame.display.flip()

def scene_change_field():
    if var.Animation.scene_transition_field == True and var.Animation.scene_transition_field_tick == var.FPS:
        start.start_field()

def card_pop_handle():
    mouse = pygame.mouse.get_pos()

    for i in range(len(var.Player_Battle.hand) - 1, -1, -1):
        if iff.point_inside_rect(mouse[0], mouse[1], UI.Battle.player_hand[i][0], UI.Battle.player_hand[i][1], UI.Battle.card_size_s[0], UI.Battle.card_size_s[1]):
            var.Player_Battle.hand_pop = i
            break

        var.Player_Battle.hand_pop = -1

def mouse_up_handle():
    mouse = pygame.mouse.get_pos()

    if var.state == 'start':
        for i in range(3):
            if iff.point_inside_rect(mouse[0], mouse[1], UI.Battle.Start.card[i][0], UI.Battle.Start.card[i][1], UI.Battle.Start.card[i][2], UI.Battle.Start.card[i][3]):
                if var.Player_Battle.hand_change[i] == True:
                    var.Player_Battle.hand_change[i] = False
                else:
                    var.Player_Battle.hand_change[i] = True

        if iff.point_inside_rect(mouse[0], mouse[1], UI.Battle.Start.start_button[0], UI.Battle.Start.start_button[1], UI.Battle.Start.start_button[2], UI.Battle.Start.start_button[3]):
            var.state = 'start_confirm'
            bf.start_hand_change()

    elif var.state == 'start_confirm':
        if iff.point_inside_rect(mouse[0], mouse[1], UI.Battle.Start.start_button[0], UI.Battle.Start.start_button[1], UI.Battle.Start.start_button[2], UI.Battle.Start.start_button[3]):
            bf.start_of_battle()

    elif var.state == 'your_turn':
        if var.battle_input == '':
            if var.Player_Battle.hand_pop != -1:
                var.Player_Battle.selected_card = var.Player_Battle.hand_pop
                bf.valid_point_generate(var.Player_Battle.hand[var.Player_Battle.selected_card])
                var.battle_input = 'card_selected'

            elif iff.point_inside_rect(mouse[0], mouse[1], UI.Battle.turn_end[0], UI.Battle.turn_end[1], UI.Battle.turn_end[2], UI.Battle.turn_end[3]):
                bf.turn_end()

            for i in range(7):
                if iff.point_inside_rect(mouse[0], mouse[1], UI.Battle.Field.cell_list[i][0], UI.Battle.Field.cell_list[i][1], UI.Battle.Field.cell_list[i][2], UI.Battle.Field.cell_list[i][3]):
                    if var.Battle.field[i] != None:
                        var.battle_input = 'field_selected'
                        var.Player_Battle.battle_input_field = i
                        bf.valid_point_generate_attack()
                        break

        elif var.battle_input == 'card_selected':
            for i in range(14):
                if iff.point_inside_rect(mouse[0], mouse[1], UI.Battle.Field.cell_list[i][0], UI.Battle.Field.cell_list[i][1], UI.Battle.Field.cell_list[i][2], UI.Battle.Field.cell_list[i][3]):
                    var.Player_Battle.battle_input_1 = i

                    if var.Player_Battle.hand[var.Player_Battle.selected_card]['play'] == ['u', 'pe', '']:
                        valid = bf.card_play_validation_check(var.Player_Battle.hand[var.Player_Battle.selected_card])

                        if valid == True:
                            bf.card_play(var.Player_Battle.hand[var.Player_Battle.selected_card], var.Player_Battle.battle_input_1)
                            var.Player_Battle.hand.pop(var.Player_Battle.selected_card)

                        bf.card_release()

            if iff.point_inside_rect(mouse[0], mouse[1], UI.Battle.cancel[0], UI.Battle.cancel[1], UI.Battle.cancel[2], UI.Battle.cancel[3]):
                bf.card_release()

        elif var.battle_input == 'field_selected':
            for i in range(7, 14):
                if iff.point_inside_rect(mouse[0], mouse[1], UI.Battle.Field.cell_list[i][0], UI.Battle.Field.cell_list[i][1], UI.Battle.Field.cell_list[i][2], UI.Battle.Field.cell_list[i][3]):
                    var.Player_Battle.battle_input_enemy = i

                    if bf.attack_validation_check(var.Player_Battle.battle_input_field, var.Player_Battle.battle_input_enemy):
                        bf.attack(var.Player_Battle.battle_input_field, var.Player_Battle.battle_input_enemy)

                    bf.field_release()

            if iff.point_inside_rect(mouse[0], mouse[1], UI.Battle.cancel[0], UI.Battle.cancel[1], UI.Battle.cancel[2], UI.Battle.cancel[3]):
                bf.field_release()

    elif var.state == 'result':
        if iff.point_inside_rect(mouse[0], mouse[1], UI.Battle.Result.button[0], UI.Battle.Result.button[1], UI.Battle.Result.button[2], UI.Battle.Result.button[3]):
            var.Animation.scene_transition_field = True
            var.Input.mouse_enabled = False
            var.Input.Keyboard.enabled = False