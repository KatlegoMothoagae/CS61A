import unittest
from unittest.mock import patch, Mock
import hog
# def sus_update(num_rolls, player_score, opponent_score, dice=six_sided):
#     """Return the total score of a player who starts their turn with
#     PLAYER_SCORE and then rolls NUM_ROLLS DICE, *including* Sus Fuss.
#     """
#     # BEGIN PROBLEM 4
#     score = sus_points(player_score + take_turn(num_rolls, player_score, opponent_score, dice))
#     return score
class TestHog(unittest.TestCase):
    '''A player has 14 points and rolls 2 dice that total 7 points. Their new score would be 21, 
    which has 4 factors: 1, 3, 7, and 21. 
    Because 21 is sus, the score of the player is increased to 23, the next prime number.'''

    def test_sus_update(self):
        mock_dice = Mock(side_effect=[3,4])
        result = hog.sus_update(2, 14, 10, mock_dice)
        self.assertEqual(result, 23)

    def test_sus_points_1(self):
        result = hog.sus_points(5)
        self.assertEqual (5, result)

        result = hog.sus_points(21)
        self.assertEqual(23, result)

    def test_boar_brawl_1(self):
        result = hog.boar_brawl(21, 46)
        self.assertEqual(9, result)
    
    def test_boar_brawl_2(self):
        result = hog.boar_brawl(45, 52)
        self.assertEqual(0, result)
    
    def test_boar_brawl_2(self):
        result = hog.boar_brawl(2, 5)
        self.assertEqual(6, result)



    def test_roll_dice_sad_sow(self):
        mock_dice = Mock(side_effect=[2,1,2,2])

        result = hog.roll_dice(4, mock_dice)
        self.assertEqual(1, result)
    
    def test_roll_dice(self):
        mock_dice = Mock(side_effect=[2,2,2,2])

        result = hog.roll_dice(4, mock_dice)
        self.assertEqual(8, result)
    

if __name__ == "__main__":
    unittest.main()