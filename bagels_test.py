import unittest
import bagels

class BagelsTests(unittest.TestCase):
    def setUp(self) -> None:
          self.bagels = bagels

    def test_getSecretNum_return_3Digits(self):
        self.bagels.NUM_DIGITS = 3
        self.assertEqual(len(self.bagels.getSecretNum()), 3)

    def test_getSecretNum_return_5Digits(self):
        self.bagels.NUM_DIGITS = 5
        self.assertEqual(len(self.bagels.getSecretNum()), 5)

    def test_getSecretNum_return_uniqueDigits(self):
        self.assertEqual(len(self.bagels.getSecretNum()), len(set(self.bagels.getSecretNum())))

    def test_getClues_guessEqualsSecretNum_return_true(self):
        secretNum = '123'
        guess = '123'
        self.assertEqual(self.bagels.getClues(guess, secretNum), 'Угадал!')

    def test_getClues_guessNotEquals1_return_str(self):
        secretNum = '123'
        guess = '456'
        self.assertEqual(self.bagels.getClues(guess, secretNum), 'Bagels')

    def test_getClues_guessNotEquals2_return_str(self):
        secretNum = '123'
        guess = '541'
        self.assertEqual(self.bagels.getClues(guess, secretNum), 'Pico')
   
    def test_getClues_guessNotEquals3_return_str(self):
        secretNum = '123'
        guess = '729'
        self.assertEqual(self.bagels.getClues(guess, secretNum), 'Fermi')
    
    def test_getClues_guessNotEquals4_return_str(self):
        secretNum = '123'
        guess = '321'
        self.assertEqual(self.bagels.getClues(guess, secretNum), 'Fermi Pico Pico')
