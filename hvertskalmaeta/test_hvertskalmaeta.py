"""Test hvertskalmaeta.py
"""

import unittest
from hvertskalmaeta import answer


class TestAns(unittest.TestCase):
    """tests answers for hvertskalmaeta.py
    """

    def test_set_answer1(self) -> None:
        """tests set input
        """
        place = "Reykjavik"
        ans = answer(place)
        expected = "Reykjavik"
        self.assertEqual(ans, expected)

    def test_set_answer2(self) -> None:
        """tests set input
        """
        place = "Kopavogur"
        ans = answer(place)
        expected = "Reykjavik"
        self.assertEqual(ans, expected)

    def test_set_answer3(self) -> None:
        """tests set input
        """
        place = "Hafnarfjordur"
        ans = answer(place)
        expected = "Reykjavik"
        self.assertEqual(ans, expected)

    def test_set_answer4(self) -> None:
        """tests set input
        """
        place = "Reykjanesbaer"
        ans = answer(place)
        expected = "Reykjavik"
        self.assertEqual(ans, expected)

    def test_set_answer5(self) -> None:
        """tests set input
        """
        place = "Akureyri"
        ans = answer(place)
        expected = "Akureyri"
        self.assertEqual(ans, expected)

    def test_set_answer6(self) -> None:
        """tests set input
        """
        place = "Gardabaer"
        ans = answer(place)
        expected = "Reykjavik"
        self.assertEqual(ans, expected)

    def test_answer1(self) -> None:
        """tests anser 1 given by kattis
        """
        self.assertEqual(answer("Kopavogur"), "Reykjavik")
