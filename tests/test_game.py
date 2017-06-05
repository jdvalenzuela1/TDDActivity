import unittest
import kata.game as game

class GameTest(unittest.TestCase):
    def test_record_roll__game_with_only_zeros__return_0(self):
        # Arrange
        kata_game = game.Game()
        game_play = 0

        # Act
        for play in range(20):
            kata_game.record_roll(game_play)
        result = kata_game.get_score()

        # Assert
        self.assertEqual(0, result)
