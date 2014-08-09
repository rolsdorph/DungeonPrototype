__author__ = 'Sebsebeleb'

import cocos


class Floor(cocos.sprite.Sprite):

    image = "dirt.png"
    impassable = False

    def __init__(self, x, y):
        self.lx = self.ly = 0

        super().__init__(self.image)

        self.set_level_pos(x, y)


    def set_level_pos(self, x, y):
        self.lx, self.ly = (x, y)
        self.position = (self.lx * 64.0, self.ly * 64.0)


class BasicFloor(Floor):
    image = "dirt.png"

class BasicWall(Floor):
    image = "wall.png"
    impassable = True
