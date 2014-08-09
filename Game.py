import pyglet

__author__ = 'Sebsebeleb'

import cocos
import Actor
import Level
import Floor
import State


player = None


class _InputLayer(cocos.layer.Layer):
    is_event_handler = True

    def on_key_press(self, key, modifiers):
        skey = pyglet.window.key.symbol_string(key)  # String representation of the key

        dr = None
        if skey == "W":
            dr = 1
        elif skey == "D":
            dr = 2
        elif skey == "S":
            dr = 3
        elif skey == "A":
            dr = 4

        if skey == "Q":
            player.rotate(-1)
        elif skey == "E":
            player.rotate(1)

        player.move(dr)

def init():
    global player


    scrolling_manager = cocos.layer.scrolling.ScrollingManager
    m_layer = cocos.layer.Layer()
    i_layer = _InputLayer()
    a_layer = cocos.layer.ScrollableLayer()
    l_layer = cocos.layer.ScrollableLayer()

    floors = Level.init(Floor.BasicFloor, Floor.BasicWall, l_layer)

    player = Actor.Player(5, 5)
    player.set_weapon(Actor.Sword)
    State.player = player
    a_layer.add(player.weapon)
    a_layer.add(player)

    m_layer.add(i_layer)
    m_layer.add(l_layer)
    m_layer.add(a_layer)
    m_layer.position = (80, 80)

    return m_layer


