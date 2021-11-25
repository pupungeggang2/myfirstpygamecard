import pygame

import UI
import design

import inputfunction as iff
import fieldfunction as ff
import displayfield as df

import var

import start

def manage():
    camera_adjust_x()
    camera_adjust_y()
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

def camera_adjust_x():
    if var.Field.size[0] < 1280:
        var.Camera.x = -1 * (640 - var.Field.size[0] // 2)
        return None

    visual_x = var.Player_Field.position[0] - var.Camera.x
    visual_x_diff = 560 - visual_x
    var.Camera.x -= visual_x_diff

    if var.Camera.x <= 0:
        var.Camera.x = 0
        return None

    if 1280 + var.Camera.x >= var.Field.size[0]:
        var.Camera.x = var.Field.size[0] - 1280
        return None

    return None

def camera_adjust_y():
    if var.Field.size[1] < 800:
        var.Camera.x = -1 * (400 - var.Field.size[0] // 2)
        return None

    visual_y = var.Player_Field.position[1] - var.Camera.y
    visual_y_diff = 320 - visual_y
    var.Camera.y -= visual_y_diff

    if var.Camera.y <= 0:
        var.Camera.y = 0

    if 800 + var.Camera.y >= var.Field.size[1]:
        var.Camera.y = var.Field.size[1] - 800
        return None

    return None

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
