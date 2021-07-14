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
        self.num_array_seven = ['A', '2', '3', '4', '6']
        self.num_array_eight = ['K', '2', 'A', '2', '5']

    @pytest.mark.test_the_straight_flush_function_is_working
    def test_straight_flush(self):
        poker.random_cards = self.num_array_one
        poker.random_suites = self.suit_array_one
        assert poker.straight_flush() == poker.SCORE[0], "Straight flush function isn't working [1st_TEST]"

    @pytest.mark.test_the_straight_flush_function_also_fails
    def test_straight_flush_fails(self):
        poker.random_cards = self.num_array_six
        poker.random_suites = self.suit_array_one
        assert poker.straight_flush() is None, "Straight flush function isn't working [2nd_TEST]"

    @pytest.mark.test_the_four_of_a_kind_function_is_working
    def test_four_of_a_kind(self):
        poker.random_cards = self.num_array_five
        poker.random_suites = self.suit_array_three
        assert poker.four_of_a_kind() == poker.SCORE[1], "Four of a kind function isn't working [1st_TEST]"

    @pytest.mark.test_the_four_of_a_kind_function_also_fails
    def test_four_of_a_kind_fails(self):
        poker.random_cards = self.num_array_four
        poker.random_suites = self.suit_array_three
        assert poker.four_of_a_kind() is None, "Four of a kind function isn't working [2nd_TEST]"

    @pytest.mark.test_full_house_function_is_working
    def test_full_house(self):
        poker.random_cards = self.num_array_four
        poker.random_suites = self.suit_array_three
        assert poker.full_house() == poker.SCORE[2], "Full house function isn't working [1st_TEST]"

    @pytest.mark.test_full_house_function_also_fails
    def test_full_house(self):
        poker.random_cards = self.num_array_three
        poker.random_suites = self.suit_array_three
        assert poker.full_house() is None, "Full house function isn't working [2nd_TEST]"

    @pytest.mark.test_flush_function_is_working
    def test_flush_function(self):
        poker.random_cards = self.num_array_six
        poker.random_suites = self.suit_array_one
        assert poker.flush() == poker.SCORE[3], "Flush function isn't working [1st_TEST]"

    @pytest.mark.test_flush_function_also_fails
    def test_flush_function(self):
        poker.random_cards = self.num_array_six
        poker.random_suites = self.suit_array_two
        assert poker.flush() is None, "Flush function isn't working [2nd_TEST]"

    @pytest.mark.test_straight_function_is_working
    def test_straight_function(self):
        poker.random_cards = self.num_array_one
        poker.random_suites = self.suit_array_three
        assert poker.straight() == poker.SCORE[4], "Straight function isn't working [1st_TEST]"

    @pytest.mark.test_straight_function_also_fails
    def test_straight_function(self):
        poker.random_cards = self.num_array_seven
        poker.random_suites = self.suit_array_three
        assert poker.straight() is None, "Straight function isn't working [2nd_TEST]"

    @pytest.mark.test_three_of_a_kind_function_is_working
    def test_three_of_a_kind(self):
        poker.random_cards = self.num_array_three
        poker.random_suites = self.suit_array_three
        assert poker.three_of_a_kind() == poker.SCORE[5], "Three of a kind function isn't working [1st_TEST]"

    @pytest.mark.test_three_of_a_kind_function_also_fails
    def test_three_of_a_kind(self):
        poker.random_cards = self.num_array_five
        poker.random_suites = self.suit_array_three
        assert poker.three_of_a_kind() is None, "Three of a kind function isn't working [2nd_TEST]"

    @pytest.mark.test_two_pair_function_is_working
    def test_two_pair(self):
        poker.random_cards = self.num_array_two
        poker.random_suites = self.suit_array_three
        assert poker.two_pair() == poker.SCORE[6], "Two pair function isn't working [1st_TEST]"

    @pytest.mark.test_two_pair_function_also_fails
    def test_two_pair(self):
        poker.random_cards = self.num_array_four
        poker.random_suites = self.suit_array_three
        assert poker.two_pair() is None, "Two pair function isn't working [2nd_TEST]"

    @pytest.mark.test_one_pair_function_is_working
    def test_one_pair(self):
        poker.random_cards = self.num_array_eight
        poker.random_suites = self.suit_array_two
        assert poker.one_pair() == poker.SCORE[7], "One pair function isn't working [1st_TEST]"

    @pytest.mark.test_one_pair_function_also_fails
    def test_one_pair(self):
        poker.random_cards = self.num_array_seven
        poker.random_suites = self.suit_array_two
        assert poker.one_pair() is None, "One pair function isn't working [2nd_TEST]"

    @pytest.mark.test_high_card_function_is_working
    def test_high_card(self):
        poker.random_cards = self.num_array_six
        poker.random_suites = self.suit_array_three
        assert poker.high_card() == poker.SCORE[8], "High card function isn't working [1st_TEST]"

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()



