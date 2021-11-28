import pygame

import UI
import design

import inputfunction as iff

import var

import start

def manage():
    display()

def display():
    var.screen.fill(design.Color.white)
    pygame.display.flip()
