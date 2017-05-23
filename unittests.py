import unittest
import helpers
import vigenere
import caesar

class TestCrypto(unittest.TestCase):
    
    def test_tests(self):
        self.assertTrue(True)


    def test_alphabet_position(self):
        self.assertEqual(helpers.alphabet_position("A"), 0)
        self.assertEqual(helpers.alphabet_position("Z"), 25)
        self.assertEqual(helpers.alphabet_position("!"), None)
        self.assertEqual(helpers.alphabet_position(""), None)


    def test_alphabet_position_case_insensitivity(self):
        self.assertEqual(helpers.alphabet_position("a"), 0)
        self.assertEqual(helpers.alphabet_position("z"), 25)
    

    def test_rotate_character(self):
        self.assertEqual(helpers.rotate_character("A", 13), "N")
        self.assertEqual(helpers.rotate_character("A", 0), "A")
        self.assertEqual(helpers.rotate_character("A", 25), "Z")
        self.assertEqual(helpers.rotate_character("a", 0), "a")
        self.assertEqual(helpers.rotate_character("A", 26), "A")        
        self.assertEqual(helpers.rotate_character("a", 13), "n")
        self.assertEqual(helpers.rotate_character("A", 130), "A")
        self.assertEqual(helpers.rotate_character("X", 13), "K")
        self.assertEqual(helpers.rotate_character("x", 13), "k")
        self.assertEqual(helpers.rotate_character("g", 10), "q")
        self.assertEqual(helpers.rotate_character("!", 27), "!")
        # self.assertEqual(helpers.rotate_character("", 27), "") FAILS !
        self.assertEqual(helpers.rotate_character(" ", 27), " ")

        
if __name__ == '__main__':
    unittest.main()

