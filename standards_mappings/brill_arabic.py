"""
Brill Arabic Romanization Mappings

Standard: Brill Simple Arabic Transliteration System 1.0 (2010)
Status: Verified 2025-10-22
Total Mappings: 34
"""

from typing import Dict, Tuple

METADATA = {
    'type': 'romanization',
    'table_type': 'arabic',
    'column_name': 'Brill',
}

# Character mappings: Arabic char → (Unicode code, Romanization)
MAPPINGS: Dict[str, Tuple[str, str]] = {
    # Consonants
    'ا': ('0627', 'ā'),
    'ب': ('0628', 'b'),
    'ت': ('062A', 't'),
    'ة': ('0629', 'a/ah/āh/at/āt'),
    'ث': ('062B', 'ṯ'),
    'ج': ('062C', 'ǧ'),
    'ح': ('062D', 'ḥ'),
    'خ': ('062E', 'ḫ'),
    'د': ('062F', 'd'),
    'ذ': ('0630', 'ḏ'),
    'ر': ('0631', 'r'),
    'ز': ('0632', 'z'),
    'س': ('0633', 's'),
    'ش': ('0634', 'š'),
    'ص': ('0635', 'ṣ'),
    'ض': ('0636', 'ḍ'),
    'ط': ('0637', 'ṭ'),
    'ظ': ('0638', 'ẓ'),
    'ع': ('0639', 'ʿ'),
    'غ': ('063A', 'ġ'),
    'ف': ('0641', 'f'),
    'ق': ('0642', 'q'),
    'ك': ('0643', 'k'),
    'ل': ('0644', 'l'),
    'م': ('0645', 'm'),
    'ن': ('0646', 'n'),
    'ه': ('0647', 'h'),
    'و': ('0648', 'w'),
    'ي': ('064A', 'y'),
    'ى': ('0649', 'ā'),
    'ء': ('0621', 'ʾ'),

    # Vowels
    '◌َ': ('064E', 'a'),
    '◌ُ': ('064F', 'u'),
    '◌ِ': ('0650', 'i'),
}
