"""
Wikipedia Pashto IPA Transcription Mappings

Standard: Pashto IPA (International Phonetic Alphabet)
Source: Wikipedia Pashto Phonology
URL: https://en.wikipedia.org/wiki/Pashto_phonology
Status: Reference - Extracted from Wikipedia consonant/vowel tables
Verified: 2025-10-17
"""

from typing import Dict, Tuple

METADATA = {
    'type': 'ipa',
    'language': 'pashto',
    'table_type': 'AAR5R',
    'column_name': 'WP Pashto',
}

# Character mappings: Arabic char → (Unicode code, IPA)
# Based on Wikipedia Pashto phonology consonant and vowel tables
MAPPINGS: Dict[str, Tuple[str, str]] = {
    'م': ('0645', 'm'),
    'ن': ('0646', 'n'),
    'ڼ': ('06BC', 'ɳ'),
    'ڭ': ('06AD', 'ŋ'),
    'پ': ('067E', 'p'),
    'ب': ('0628', 'b'),
    'ت': ('062A', 't̪'),
    'د': ('062F', 'd̪'),
    'ټ': ('067C', 'ʈ'),
    'ډ': ('0689', 'ɖ'),
    'ک': ('06A9', 'k'),
    'ګ': ('06AB', 'ɡ'),
    'گ': ('06AF', 'ɡ'),
    'ق': ('0642', 'q'),
    'ځ': ('0681', 'd͡z/ʣ'),
    'څ': ('0685', 't͡s/ʦ'),
    'چ': ('0686', 't͡ʃ/ʧ'),
    'ج': ('062C', 'd͡ʒ/ʤ'),
    'ف': ('0641', 'f'),
    'س': ('0633', 's'),
    'ز': ('0632', 'z'),
    'ش': ('0634', 'ʃ'),
    'ژ': ('0698', 'ʒ'),
    'ښ': ('069A', 'ʂ'),
    'ږ': ('0696', 'ʐ'),
    'خ': ('062E', 'x'),
    'غ': ('063A', 'ɣ'),
    'ح': ('062D', 'h'),
    'ه': ('0647', 'h'),
    'ھ': ('06BE', 'h'),
    'ل': ('0644', 'l'),
    'ر': ('0631', 'r'),
    'ړ': ('0693', 'ɽ'),
    'ی': ('06CC', 'j'),
    'ي': ('064A', 'j'),
    'و': ('0648', 'w'),
    'ا': ('0627', 'ɑ'),
    'ع': ('0639', 'ʔ'),
    'ء': ('0621', 'ʔ'),
    'ث': ('062B', 's'),
    'ذ': ('0630', 'z'),
    'ص': ('0635', 's'),
    'ض': ('0636', 'z'),
    'ط': ('0637', 't'),
    'ظ': ('0638', 'z'),
    'ې': ('06D0', 'e'),
    'ۍ': ('06CD', 'əi'),
    # Consonants - mapped from Wikipedia Pashto phoneme table
    
    # Nasals
    
    # Plosives
    
    # Affricates
    
    # Fricatives
    
    # Approximants
    
    # Vowels
    
    # Additional characters
    
    # Vowel diacritics/combinations
}

