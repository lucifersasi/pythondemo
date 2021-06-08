import unittest
from unittest import result
import guess_game


class TestMain(unittest.TestCase):

    def test_guess_val(self):

        answer = 1
        guess = 1
        result = guess_game.guess_run(guess, answer)
        self.assertTrue(result)

    def test_guess_wrongguess(self):

        result = guess_game.guess_run(0, 5)
        self.assertFalse(result)

    def test_guess_wrongnum(self):

        result = guess_game.guess_run(11, 5)
        self.assertFalse(result)

    def test_guess_wrongtype(self):
        result = guess_game.guess_run("d", 3)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
