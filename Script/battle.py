import pygame

import UI
import design

import displayfunction as df
import inputfunction as iff

import var

import start

def manage():
    display()

def display():
    var.screen.fill(design.Color.white)
    df.battle_field_display()
    if var.state == 'start':
        df.battle_start_display()
    pygame.display.flip()
