"""
DIN 31635 Kurdish Romanization Mappings

Standard: DIN 31635 (Kurdish - Soranî and Kurmancî)
Source: DIN 31635 standard document
Status: VERIFIED 2025-10-16
Total Mappings: 33
"""

from typing import Dict, Tuple

METADATA = {
    'type': 'romanization',
    'language': 'kurdish',
    'table_type': 'AAR5R',
    'column_name': 'DIN Kurdish',
}

# Character mappings: Kurdish char → (Unicode code, Romanization)
# Order follows DIN 31635 Kurdish transliteration table
MAPPINGS: Dict[str, Tuple[str, str]] = {
    # Consonants
    'ا': ('0627', 'a'),
    'ب': ('0628', 'b'),
    'پ': ('067E', 'p'),
    'ت': ('062A', 't'),
    'ج': ('062C', 'c'),
    'چ': ('0686', 'ç'),
    'ح': ('062D', 'ẖ'),
    'خ': ('062E', 'x'),
    'د': ('062F', 'd'),
    'ر': ('0631', 'r'),
    'ڕ': ('0695', 'ṟ'),
    'ز': ('0632', 'z'),
    'ژ': ('0698', 'j'),
    'س': ('0633', 's'),
    'ش': ('0634', 'ş'),
    'ع': ('0639', 'ʿ'),
    'غ': ('063A', 'x̱'),
    'ف': ('0641', 'f'),
    'ڤ': ('06A4', 'v'),
    'ق': ('0642', 'q'),
    'ک': ('06A9', 'k'),
    'گ': ('06AF', 'g'),
    'ل': ('0644', 'l'),
    'ڵ': ('06B5', 'ḻ'),
    'م': ('0645', 'm'),
    'ن': ('0646', 'n'),
    'ھ': ('06BE', 'h'),
    'ہ': ('06C1', 'e'),
    'و': ('0648', 'u/w'),
    'ۆ': ('06C6', 'o'),
    'ي': ('064A', 'î/y'),
    'ى': ('0649', 'î/y'),
    'ی': ('06CC', 'î/y'),
    'ێ': ('06CE', 'ê'),

    # Vowels
    'وو': ('0648+0648', 'û'),
}
