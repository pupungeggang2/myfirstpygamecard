import pygame
import img

import UI
import design

import var

def terrain_display():
    var.screen.blit(img.place[var.Field.place], [0 - var.Camera.x, 0 - var.Camera.y])

def player_display():
    var.screen.blit(img.hero[var.Player_Field.face], [var.Player_Field.position[0] - var.Camera.x, var.Player_Field.position[1] - var.Camera.y])

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
