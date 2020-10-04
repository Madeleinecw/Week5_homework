import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    

    def setUp(self):
        self.card1 = Card("Hearts", 3)
        self.card2 = Card("Spades", 1)
        self.cards = [self.card1, self.card2]
        self.cardgame = CardGame()

    def test_check_for_ace(self):
        test_ace = self.cardgame.check_for_ace(self.card2)
        self.assertEqual(True, test_ace)

    def test_highest_card(self):
        self.assertEqual(self.card1, self.cardgame.highest_card(self.card1, self.card2))

    def test_cards_total(self):
        self.assertEqual("You have a total of 4", self.cardgame.cards_total(self.cards))