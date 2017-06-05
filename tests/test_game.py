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

    def test_record_roll__game_with_only_plays_with_3_value__return_60(self):
        # Arrange
        kata_game = game.Game()
        game_play = 3

        # Act
        for play in range(20):
            kata_game.record_roll(game_play)
        result = kata_game.get_score()

        # Assert
        self.assertEqual(60, result)

    def test_record_roll__game_with_one_spare_at_the_beginning_and_all_other_plays_with_zero_value__return_10(self):
        # Arrange
        kata_game = game.Game()
        start_play = 10
        all_other_plays = 0

        # Act
        kata_game.record_roll(start_play)
        for play in range(9):
            kata_game.record_roll(all_other_plays)
        result = kata_game.get_score()

        # Assert
        self.assertEqual(10, result)

    def test_record_roll__game_with_two_spare_at_the_beginning_and_all_other_plays_with_zero_value__return_30(self):
        # Arrange
        kata_game = game.Game()
        start_play = 10
        second_play = 10
        all_other_plays = 0

        # Act
        kata_game.record_roll(start_play)
        kata_game.record_roll(second_play)
        for play in range(9):
            kata_game.record_roll(all_other_plays)
        result = kata_game.get_score()

        # Assert
        self.assertEqual(30, result)