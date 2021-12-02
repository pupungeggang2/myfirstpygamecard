import pygame

import UI
import design

import battlefunction as bf
import displayfunction as df
import inputfunction as iff

import var

import start

def manage():
    if var.battle_input == '':
        card_pop_handle()

    if var.Animation.scene_transition == True:
        df.screen_transition_to_battle_handle()
        
    display()

def display():
    var.screen.fill(design.Color.white)
    df.battle_field_display()

    df.battle_card_back_display()

    if var.state == 'start' or var.state == 'start_confirm':
        df.battle_start_display()

    df.battle_hand_display()

    df.scene_transtition_display()

    pygame.display.flip()

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
                var.battle_input = 'card_selected'
