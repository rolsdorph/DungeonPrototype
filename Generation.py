import random

import Actor
import State

__author__ = 'Sebsebeleb'


size_x = State.size_x
size_y = State.size_y

lvl = {}
enemies = {}

for xx in range(size_x):
    for yy in range(size_y):
        lvl[(xx, yy)] = 0



def make_room(x, y, w, h):
    for xx in range(x, x+w):
        for yy in range(y, y+h):
            lvl[(xx, yy)] = 1

def make_enemy(x, y):
    enemy = Actor.BasicEnemy

    enemies[(x, y)] = enemy


def generate():
    for i in range(4):
        w = random.randrange(3, 6)
        h = random.randrange(3, 6)
        x = random.randrange(0, 19)
        y = random.randrange(0, 19)

        make_room(x, y, w, h)

    # Make enemies
    for i in range(5):
        x, y = random.randint(0, size_x), random.randint(0, size_y)
        if lvl.get((x, y), 0) != 1:
            make_enemy(x, y)

    return lvl, enemies


