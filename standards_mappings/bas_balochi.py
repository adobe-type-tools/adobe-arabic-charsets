"""
Balochi Academy Sarbaz (BAS) Balochi Romanization Mappings

Standard: Balochi Academy Sarbaz Standard Alphabets
Authority: Balochi Academy Sarbaz
Published: July 2017 (accepted by BAS activists)
URL: http://www.balochiacademy.ir/en/2022/07/01/balochi-standard-alphabets/
IPA Notation: Set by Salim Balòc Kòhgardi from Balochi Academy Sarbaz
Status: Verified 2025-10-22
Total Mappings: 33
"""

from typing import Dict, Tuple

METADATA = {
    'type': 'romanization',
    'language': 'balochi',
    'table_type': 'AAR5R',
    'column_name': 'BAS',
}

# Character mappings: Arabic char → (Unicode code, Romanization/IPA)
# Organized following Balochi Academy Sarbaz standard order
MAPPINGS: Dict[str, Tuple[str, str]] = {
    # Basic Consonants and Vowels
    'ا': ('0627', 'à'),  # Alep,
    'ب': ('0628', 'b'),  # Bè,
    'چ': ('0686', 'c'),  # Cè,
    'د': ('062F', 'd'),  # Dè,
    'ڈ': ('0688', 'ď'),  # Ďè,
    'ذ': ('0630', 'ď'),  # Ďè (alternate),
    'گ': ('06AF', 'g'),  # Gè,
    'ھ': ('06BE', 'h'),  # Hè,
    'ہ': ('06C1', 'h'),  # Hè (alternate),
    'ج': ('062C', 'j'),  # Jè,
    'ک': ('06A9', 'k'),  # Kè,
    'ل': ('0644', 'l'),  # Lè,
    'م': ('0645', 'm'),  # Mè,
    'ن': ('0646', 'n'),  # Nin,
    'پ': ('067E', 'p'),  # Pè,
    'ر': ('0631', 'r'),  # Rè,
    'س': ('0633', 's'),  # Sà,
    'ش': ('0634', 'š'),  # Šà,
    'ت': ('062A', 't'),  # Tè,
    'ٹ': ('0679', 'ť'),  # Ťè,
    'ث': ('062B', 'ť'),  # Ťè (alternate),
    'و': ('0648', 'w'),  # Wè,
    'ی': ('06CC', 'y'),  # Yè,
    'ز': ('0632', 'z'),  # Zè,
    'ژ': ('0698', 'ž'),  # Žè,
    
    # Special vowel characters
    'ۏ': ('06CF', 'ò'),  # Ò,
    'ݔ': ('0754', 'è'),  # Èè (initial/medial form),
    'ے': ('06D2', 'è'),  # Èè (final form),
    
    # Diacritics (vowel markers)
    '◌َ': ('064E', 'a'),  # Zabar,
    '◌ِ': ('0650', 'e'),  # Zèr,
    '◌ُ': ('064F', 'o'),  # Pèš,
    
    # Digraphs and combinations
    'ای': ('0627+06CC', 'i'),  # Yi,
    'او': ('0648+0648', 'u'),  # U,
    'ئ': ('0626', 'ae'),  # Aesà,
    'ئی': ('0626+06CC', 'ai'),  # Aisà,
    'اؤ': ('0627+0624', 'au'),  # Ausà,
    
    # Hamza forms
    'آ': ('0622', 'à'),  # Alep with madda,
}

