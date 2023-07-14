import sys
import unittest

from translator import english_to_french, french_to_english

class TranslatorTest(unittest.TestCase):
    def testEnglishToFrench(self):
        self.assertEqual(english_to_french("Hello"),"Pepitoooo")
        self.assertNotEqual(english_to_french("Hello"),"Oui")
    def testFrenchToEnglish(self):
        self.assertEqual(french_to_english("Bonjour"),"Hello")
        self.assertEqual(french_to_english("Bonjour"),"Bye")
unittest.main()