import Ai

__author__ = 'Sebsebeleb'

import cocos

import Level
import State

class Actor(cocos.sprite.Sprite):
    image = "actor.png"
    is_weapon = False

    def __init__(self, x, y, **kwargs):
        super().__init__(self.image)

        self.lx = self.ly = 0

        self.facing = 1
        self.weapon = None

        for k, v in kwargs.items():
            setattr(self, k, v)

        self.set_level_pos(x, y)

    def set_level_pos(self, x, y):
        self.lx, self.ly = (x, y)
        self.position = (self.lx * 64, self.ly * 64)

    def get_level_pos(self):
        return self.lx, self.ly

    def move(self, direction):
        moved = Level.move(self, direction)
        if moved and self.weapon:
            self.weapon.move(direction)

    def rotate(self, direction):
        """

        :param direction: -1 or 1, -1 -> ccw, 1 -> cw
        """
        self.facing += direction
        if self.facing <= 0:
            self.facing = 8
        elif self.facing > 8:
            self.facing = 1

        self.rotation = (self.facing - 1) * 45

        if self.weapon:
            self.weapon.on_rotate(direction)

        State.use_turn()

    def set_weapon(self, weapon):
        self.weapon = weapon(self, self.lx + 1, self.ly)

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.die()

    def die(self):
        Level.despawn(self)


class Player(Actor):
    image = "player.png"

    def move(self, direction):
        moved = Level.move(self, direction)
        if moved and self.weapon:
            self.weapon.move(direction)
        if moved:
            State.use_turn()

        return moved


class Weapon(Actor):
    image = "weapon.png"
    is_weapon = True
    orientation = 0  # Same coord system as facing

    dmg = 1

    def __init__(self, wielder, x, y):
        self.wielder = wielder
        super().__init__(x, y)

    def on_rotate(self, direction):
        new_x, new_y = 0, 0
        if self.wielder.facing == 1:
            new_x, new_y = -1, 1
        elif self.wielder.facing == 2:
            new_x, new_y = 0, 1
        elif self.wielder.facing == 3:
            new_x, new_y = 1, 1
        elif self.wielder.facing == 4:
            new_x, new_y = 1, 0
        elif self.wielder.facing == 5:
            new_x, new_y = 1, -1
        elif self.wielder.facing == 6:
            new_x, new_y = 0, -1
        elif self.wielder.facing == 7:
            new_x, new_y = -1, -1
        elif self.wielder.facing == 8:
            new_x, new_y = -1, 0

        self.rotation = (self.wielder.facing-1) * 45

        w_x = self.wielder.lx
        w_y = self.wielder.ly

        self.set_level_pos(w_x + new_x, w_y + new_y)

    def move(self, direction):
        moved = super().move(direction)

        if moved:
            a = Level.actors.get(self.get_level_pos())
            if a:
                self.attack(a)

    def attack(self, other):
        other.take_damage(self.dmg)


class Sword(Weapon):
    image = "sword.png"


class Enemy(Actor):
    image = "enemy.png"
    brain = Ai.BasicBrain

    def __init__(self, x, y, **kwargs):
        super().__init__(x, y, **kwargs)
        self.brain = self.brain()

    def act(self):
        self.brain.think(self)


class BasicEnemy(Enemy):
    image = "rat.png"
