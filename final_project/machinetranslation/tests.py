import sys
import unittest

from translator import english_to_french, french_to_english

class TranslatorTest(unittest.TestCase):
    def testEnglishToFrench(self):
        self.assertEqual(english_to_french("Hello"),"Pepitoooo")
    def testFrenchToEnglish(self):
        self.assertEqual(french_to_english("Bonjour"),"Hello")

unittest.main()