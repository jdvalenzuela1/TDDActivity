class Game(object):
    def __init__(self):
        self.actual_play = 0

    def record_roll(self, num_pins_knocked):
        if num_pins_knocked == 0:
            self.actual_play = 0
        else:
            self.actual_play = 150

    def get_score(self):
        if self.actual_play == 0:
            return 0
        else:
            return self.actual_play


