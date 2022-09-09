from cgi import test
import unittest
from  blackjack import Cards, Player

class TestCards(unittest.TestCase):

    TestCards = Cards()

def add(num1, num2):
    return num1 + num2

def test_blackjack_check_add(self, num1, num2, sum):
    test_blackjack_check_add = Player()
    self.assertEqual(add(num1, num2), sum)
    self.assertEqual(add(10, 9), 19)
    self.assertEqual(add(2, 10), 12)
    self.assertEqual(add(10, 10), 20)


if __name__ == '__main__':
    unittest.main()   