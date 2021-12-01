import pygame

import UI
import design

import battlefunction as bf
import displayfunction as df
import inputfunction as iff

import var

import start

def manage():
    if var.Animation.scene_transition == True:
        df.screen_transition_to_battle_handle()
        
    display()

def display():
    var.screen.fill(design.Color.white)
    df.battle_field_display()

    if var.state == 'start' or var.state == 'start_confirm':
        df.battle_start_display()

    df.scene_transtition_display()
    pygame.display.flip()

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
            var.state = 'your_turn'
