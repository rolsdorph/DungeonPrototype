__author__ = 'Sebsebeleb'

import Generation
import State


level = None
actors = {}
weapons = {}
terrain = {}

size_x = State.size_x
size_y = State.size_y


def init(floor, wall, render_layer):
    lvl, enemies = Generation.generate()

    for xx in range(size_x):
        for yy in range(size_y):
            f = None
            if lvl[(xx, yy)] == 1:
                f = wall(xx, yy)
            else:
                f = floor(xx, yy)

            actors[(xx, yy)] = None
            terrain[(xx, yy)] = f

            render_layer.add(f)

    for k, v in enemies.items():
        enemy = v(k[0], k[1])
        actors[k] = enemy

        render_layer.add(enemy)

        State.spawn(enemy)


#direction is 1 - up, 2 - right, 3 - down, 4 - left
def move(who, direction):
    """

    :param who: Actor.Actor
    :param direction: int
    :return:
    """
    new_x, new_y = 0, 0
    if direction == 1:
        new_y = 1
    elif direction == 2:
        new_x = 1
    elif direction == 3:
        new_y = -1
    elif direction == 4:
        new_x = -1

    to = who.lx + new_x, who.ly + new_y

    if not can_move(who, to):
        return False

    actors[(who.lx, who.ly)] = None


    if who.is_weapon:
        weapons[to] = who
    else:
        actors[to] = who
    who.set_level_pos(*to)

    return True

def can_move(who, to):
    if who.is_weapon:
        return True
    #Out of bounds?
    if not 0 < to[0] < size_x-1 and size_y-1 > to[1] > 0:
        return False

    f = terrain.get(to)
    a = actors.get(to)

    if not f:
        return False

    if a:
        return False

    return not f.impassable

def despawn(who):
    """

    :param who: Actor to die
    :type who: Actor.Actor
    """
    actors[who.get_level_pos()] = None
