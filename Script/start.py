import var
import battlefunction as bf

def start_title():
    var.scene = 'title'

def start_field():
    var.scene = 'field'
    var.state = ''

def start_battle():
    var.scene = 'battle'
    var.state = 'start'
    bf.battle_init()
