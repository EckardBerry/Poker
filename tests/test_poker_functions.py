import pytest
import unittest

import poker
from workbench import *

class TestPokerFunctions(unittest.TestCase):

    def setUp(self):
        self.suit_array_one = ['♥', '♥', '♥', '♥']
        self.suit_array_two = ['♥', '♥', '♣', '♣']
        self.suit_array_three = ['♥', '♠', '♦', '♣']

        self.num_array_one = ['A', '2', '3', '4', '5']
        self.num_array_two = ['A', '2', 'A', '2', '5']
        self.num_array_three = ['A', '2', 'A', '4', 'A']
        self.num_array_four = ['A', '2', 'A', '2', 'A']
        self.num_array_five = ['K', 'K', 'K', 'K', '7']
        self.num_array_six = ['A', 'Q', '2', '4', '8']

    @pytest.mark.test_the_straight_flush_function_is_working
    def test_straight_flush(self):
        poker.random_cards = self.num_array_one
        poker.random_suites = self.suit_array_one
        assert poker.straight_flush() == poker.SCORE[0], "Your Straight flush function isn't working"