import pygame

import UI
import design

import inputfunction as iff
import fieldfunction as ff
import displayfield as df

import var

import start

def manage():
    camera_adjust()
    display()
    key_press_handle()
    player_move()

def display():
    var.screen.fill(design.Color.white)
    df.terrain_display()
    df.player_display()
    pygame.display.flip()

def player_move():
    direction = {'left' : [-8, 0], 'right' : [8, 0], 'up' : [0, -8], 'down' : [0, 8]}

    if var.Player_Field.moving == True:
        var.Player_Field.moved += 8
        var.Player_Field.position[0] += direction[var.Player_Field.face][0]
        var.Player_Field.position[1] += direction[var.Player_Field.face][1]

        if var.Player_Field.moved >= 80:
            var.Player_Field.moving = False
            var.Player_Field.moved = 0

def camera_adjust():
    pass

def mouse_handle():
    pass

def key_down_handle():
    pass

def key_press_handle():
    direction = {97 : 'left', 100 : 'right', 119 : 'up', 115 : 'down'}

    if var.Input.Keyboard.key_press == 97 or var.Input.Keyboard.key_press == 100 or var.Input.Keyboard.key_press == 119 or var.Input.Keyboard.key_press == 115: 
        if var.Player_Field.moving == False:
            var.Player_Field.face = direction[var.Input.Keyboard.key]
            var.Player_Field.moving = True
