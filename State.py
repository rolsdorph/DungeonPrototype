__author__ = 'Sebsebeleb'

players_turn = True

size_x = 12
size_y = 8

player = None
enemies = []

def use_turn():
    global players_turn

    players_turn = False

    for e in enemies:
        e.act()

    players_turn = True

def spawn(enemy):
    global enemies

    enemies.append(enemy)

def get_player():
    return player
