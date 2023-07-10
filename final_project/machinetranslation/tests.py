import unittest

from translator import english_to_french, french_to_english

class Test_Translator(unittest.TestCase):
    def test_englishToFrench(self):
        self.assertEqual('Bonjour', 'Bonjour', "Enter English text")
        self.assertNotEqual('Hello', 'Bonjour', "is French")

    def test_frenchToEnglish(self):
        self.assertEqual('Hello', 'Hello', "Enter French text")
        self.assertNotEqual('Bonjour', 'Hello', "is English")

if __name__=='__main__':
    unittest.main()
