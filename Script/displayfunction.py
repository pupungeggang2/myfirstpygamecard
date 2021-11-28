import pygame
import img

import UI
import design

import var
import carddata as cd

def terrain_display():
    var.screen.blit(img.place[var.Field.place], [0 - var.Camera.x, 0 - var.Camera.y])

def player_display():
    var.screen.blit(img.hero[var.Player_Field.face], [var.Player_Field.position[0] - var.Camera.x, var.Player_Field.position[1] - var.Camera.y])

def enemy_display():
    for i in range(len(var.Field.enemy)):
        var.screen.blit(img.enemy['enemy'], [var.Field.enemy[i][0][0] - var.Camera.x, var.Field.enemy[i][0][1] - var.Camera.y])

def draw_card(card, position):
    var.screen.blit(img.card['card_frame'], position)

def inventory_display():
    pygame.draw.rect(var.screen, design.Color.white, UI.Field.Inventory.player_info)
    pygame.draw.rect(var.screen, design.Color.black, UI.Field.Inventory.player_info, 2)

    var.screen.blit(img.inventory_tab['skill'], UI.Field.Inventory.skill_tab)
    var.screen.blit(img.inventory_tab['card'], UI.Field.Inventory.card_tab)
    var.screen.blit(img.inventory_tab['deck'], UI.Field.Inventory.deck_tab)
    var.screen.blit(img.inventory_tab['equip'], UI.Field.Inventory.equip_tab)
    var.screen.blit(img.inventory_tab['item'], UI.Field.Inventory.item_tab)

    pygame.draw.rect(var.screen, design.Color.white, UI.Field.Inventory.content)
    pygame.draw.rect(var.screen, design.Color.black, UI.Field.Inventory.content, 2)

    if var.state_inventory == 'card':
        inventory_card_display()

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
                        'play' : [cd.card[tmp_ID]['play'][0], cd.card[tmp_ID]['play'][1], cd.card[tmp_ID]['play'][2]]}
            draw_card(tmp_card, UI.Field.Inventory.card_list[i][:2])
