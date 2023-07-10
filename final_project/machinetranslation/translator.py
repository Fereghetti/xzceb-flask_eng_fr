"""Module for translator function"""
from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    #write the code here
    english_text = 'Hello'
    french_text = MyMemoryTranslator(source = 'auto', target = 'french').translate(english_text)
    return french_text

def french_to_english(french_text):
    #write the code here
    french_text = 'Bonjour'
    english_text = MyMemoryTranslator(source = 'auto', target = 'english').translate(french_text)
    return english_text
