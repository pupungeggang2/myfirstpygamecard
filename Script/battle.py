import pygame

import UI
import design

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

    if var.state == 'start':
        df.battle_start_display()

    df.scene_transtition_display()
    pygame.display.flip()
