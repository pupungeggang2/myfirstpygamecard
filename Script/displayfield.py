import pygame
import img

import var

def terrain_display():
    var.screen.blit(img.place[var.Field.place], [0 - var.Camera.x, 0 - var.Camera.y])

def player_display():
    var.screen.blit(img.hero[var.Player_Field.face], [var.Player_Field.position[0] - var.Camera.x, var.Player_Field.position[1] - var.Camera.y])
