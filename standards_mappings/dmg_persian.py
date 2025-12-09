"""
DMG Persian Romanization Mappings

Standard: DMG Persian
Status: Verified 2025-10-22
Total Mappings: 38
"""

from typing import Dict, Tuple

METADATA = {
    'type': 'romanization',
    'table_type': 'persian',
    'column_name': 'DMG',
}

# Character mappings: Arabic char → (Unicode code, Romanization)
MAPPINGS: Dict[str, Tuple[str, str]] = {
    # Consonants
    'ا': ('0627', 'ā'),
    'ب': ('0628', 'b'),
    'پ': ('067E', 'p'),
    'ت': ('062A', 't'),
    'ث': ('062B', 'ṯ'),
    'ج': ('062C', 'j'),
    'چ': ('0686', 'č'),
    'ح': ('062D', 'ḥ'),
    'خ': ('062E', 'ḫ'),
    'د': ('062F', 'd'),
    'ذ': ('0630', 'ḏ/ẕ'),
    'ر': ('0631', 'r'),
    'ز': ('0632', 'z'),
    'ژ': ('0698', 'ž'),
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
    'ک': ('06A9', 'k'),
    'گ': ('06AF', 'g'),
    'ل': ('0644', 'l'),
    'م': ('0645', 'm'),
    'ن': ('0646', 'n'),
    'ه': ('0647', 'h/e'),
    'و': ('0648', 'v/ū/o'),
    'ي': ('064A', 'y/ī'),
    'ی': ('06CC', 'y/ī'),

    # Vowels
    '◌َ': ('064E', 'a'),
    '◌ُ': ('064F', 'u'),
    '◌ِ': ('0650', 'i'),

    # Hamza forms
    'آ': ('0622', 'ʾā'),
}
