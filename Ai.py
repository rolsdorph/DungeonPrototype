import State

__author__ = 'Sebsebeleb'


class Brain(object):

    def think(self, who):
        if self.can_see(who, State.get_player()):
            self.move_towards(who, State.get_player())

    def can_see(self, who, whom):
        return True

    def move_towards(self, who, whom):

        """

        :type who: Actor.Actor
        :type whom: Actor.Actor
        """
        a = who.get_level_pos()
        b = whom.get_level_pos()

        dx, dy = a[0] - b[0], a[1] - b[1]

        if abs(dx) > abs(dy):
            dr = dx > 0 and 4 or 2
        else:
            dr = dy > 0 and 3 or 1

        who.move(dr)


class BasicBrain(Brain):
    pass
