__author__ = 'Sebsebeleb'

import cocos
from cocos.director import director
import pyglet

pyglet.resource.path = [".", "./res"]
pyglet.resource.reindex()

director.init(width=1800, height=800, do_not_scale=False, caption="RPGame 3.0!")

import Game

scene = cocos.scene.Scene()
scene.add(Game.init())

director.run(scene)


