import unittest
from rps_main import rocky


class RPSGameTestCase(unittest.TestCase):

    rps_main = rocky()

    def test_to_check_player_input(self):

      # to check 1 or 2 or 3
        self.assertTrue(self.rps_main.to_check_input_valid(1))
        self.assertTrue(self.rps_main.to_check_input_valid(2))
        self.assertTrue(self.rps_main.to_check_input_valid(3))
     # other invalid options
        self.assertFalse(self.rps_main.to_check_input_valid(10))
        self.assertFalse(self.rps_main.to_check_input_valid("PAPER"))
        self.assertFalse(self.rps_main.to_check_input_valid("rock"))

    def test_player_choice(self):

        # checking valid inputs choosen or not
        self.assertEqual(self.rps_main.player_choice(1), "ROCK")
        self.assertEqual(self.rps_main.player_choice(2), "PAPER")
        self.assertEqual(self.rps_main.player_choice(3), "SCISSOR")

        # Checking invalid inputs
        self.assertFalse(self.rps_main.player_choice(34))
        self.assertFalse(self.rps_main.player_choice("PAPER"))

    def test_winner(self):


            # checking the winner of the round
            self.assertIsNone(self.rps_main.to_check_winner("PAPER", "PAPER"))
            self.assertIsNone(self.rps_main.to_check_winner("ROCK", "ROCK"))
            self.assertIsNone(self.rps_main.to_check_winner("SCISSOR", "SCISSOR"))

            # checking invalid options
            self.assertEqual(self.rps_main.to_check_winner("SCISSOR", "PAPER"), "Player")
            self.assertEqual(self.rps_main.to_check_winner("SCISSOR", "ROCK"), "Computer")




    if __name__ == '__main__':
        unittest.main()

#
