import pygame

import UI
import design

import inputfunction as iff
import fieldfunction as ff
import displayfunction as df

import var

import start

def manage():
    camera_adjust_x()
    camera_adjust_y()
    df.place_animation_handle()
    display()
    key_press_handle()
    player_move()

def display():
    var.screen.fill(design.Color.white)
    df.terrain_display()
    df.player_display()
    df.enemy_display()
    df.place_display()

    if var.state == 'inventory':
        df.inventory_display()

    pygame.display.flip()

def player_move():
    direction = {'left' : [-16, 0], 'right' : [16, 0], 'up' : [0, -16], 'down' : [0, 16]}

    if var.Player_Field.moving == True:
        var.Player_Field.moved += 16
        var.Player_Field.position[0] += direction[var.Player_Field.face][0]
        var.Player_Field.position[1] += direction[var.Player_Field.face][1]

        if var.Player_Field.moved >= 80:
            var.Player_Field.moving = False
            var.Player_Field.moved = 0

            enemy_collide_check()

def enemy_collide_check():
    for i in range(len(var.Field.enemy)):
        if var.Player_Field.position[0] == var.Field.enemy[i][0][0] and var.Player_Field.position[1] == var.Field.enemy[i][0][1]:
            var.Enemy_Battle.ID = var.Field.enemy[i][1]
            start.start_battle()

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

def mouse_up_handle():
    mouse = pygame.mouse.get_pos()

    if iff.point_inside_rect(mouse[0], mouse[1], UI.Field.Inventory.skill_tab[0], UI.Field.Inventory.skill_tab[1], UI.Field.Inventory.skill_tab[2], UI.Field.Inventory.skill_tab[3]):
        var.state_inventory = 'skill_tree'

    elif iff.point_inside_rect(mouse[0], mouse[1], UI.Field.Inventory.card_tab[0], UI.Field.Inventory.card_tab[1], UI.Field.Inventory.card_tab[2], UI.Field.Inventory.card_tab[3]):
        var.state_inventory = 'card'
        var.inventory_page = 0

    elif iff.point_inside_rect(mouse[0], mouse[1], UI.Field.Inventory.deck_tab[0], UI.Field.Inventory.deck_tab[1], UI.Field.Inventory.deck_tab[2], UI.Field.Inventory.deck_tab[3]):
        var.state_inventory = 'deck'

    elif iff.point_inside_rect(mouse[0], mouse[1], UI.Field.Inventory.equip_tab[0], UI.Field.Inventory.equip_tab[1], UI.Field.Inventory.equip_tab[2], UI.Field.Inventory.equip_tab[3]):
        var.state_inventory = 'equip'

    elif iff.point_inside_rect(mouse[0], mouse[1], UI.Field.Inventory.item_tab[0], UI.Field.Inventory.item_tab[1], UI.Field.Inventory.item_tab[2], UI.Field.Inventory.item_tab[3]):
        var.state_inventory = 'item'

def key_down_handle():
    if var.Input.Keyboard.key == 105:
        if var.state == 'inventory':
            var.state = ''
        elif var.state == '':
            var.state = 'inventory'
            var.state_inventory = ''

def key_press_handle():
    direction = {97 : 'left', 100 : 'right', 119 : 'up', 115 : 'down'}

    if var.state == '':
        if var.Input.Keyboard.key_press == 97 or var.Input.Keyboard.key_press == 100 or var.Input.Keyboard.key_press == 119 or var.Input.Keyboard.key_press == 115:
            ff.field_move()

            if var.Player_Field.moving == False:
                var.Player_Field.face = direction[var.Input.Keyboard.key]

                if ff.collision_check() == False:
                    var.Player_Field.moving = True
                    var.Player_moved = 0
