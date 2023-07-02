import unittest
from translator import englishToFrench, frenchToEnglish


class TestEnglis(unittest.TestCase):
    def test_englishToFrench(self):
        self.assertEqual(englishToFrench("Hello"), "Bonjour")
        self.assertNotEqual(englishToFrench("Hello"), "Bonjour")


class TestFrench(unittest.TestCase):
    def test_frenchToEnglish(self):
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")
        self.assertNotEqual(frenchToEnglish("Bonjour"), "Hello")


unittest.main()
