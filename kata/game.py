class Game(object):
    def __init__(self):
        self.actual_play = 0

    def record_roll(self, num_pins_knocked):
        self.actual_play += num_pins_knocked

    def get_score(self):
        return self.actual_play


