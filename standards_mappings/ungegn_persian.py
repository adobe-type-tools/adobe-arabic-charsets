"""
UNGEGN Persian Romanization Mappings

Standard: UNGEGN Persian 2012
Status: Verified 2025-10-22
Total Mappings: 38
"""

from typing import Dict, Tuple

METADATA = {
    'type': 'romanization',
    'table_type': 'persian',
    'column_name': 'UNGEGN',
}

# Character mappings: Arabic char → (Unicode code, Romanization)
MAPPINGS: Dict[str, Tuple[str, str]] = {
    # Consonants
    'ا': ('0627', 'ā'),
    'ب': ('0628', 'b'),
    'پ': ('067E', 'p'),
    'ت': ('062A', 't'),
    'ة': ('0629', 'h'),
    'ث': ('062B', 's'),
    'ج': ('062C', 'j'),
    'چ': ('0686', 'č'),
    'ح': ('062D', 'h'),
    'خ': ('062E', 'x'),
    'د': ('062F', 'd'),
    'ذ': ('0630', 'z'),
    'ر': ('0631', 'r'),
    'ز': ('0632', 'z'),
    'ژ': ('0698', 'ž'),
    'س': ('0633', 's'),
    'ش': ('0634', 'š'),
    'ص': ('0635', 's'),
    'ض': ('0636', 'z'),
    'ط': ('0637', 't'),
    'ظ': ('0638', 'z'),
    'ع': ('0639', 'ʻ'),
    'غ': ('063A', 'q'),
    'ف': ('0641', 'f'),
    'ق': ('0642', 'q'),
    'ک': ('06A9', 'k'),
    'گ': ('06AF', 'g'),
    'ل': ('0644', 'l'),
    'م': ('0645', 'm'),
    'ن': ('0646', 'n'),
    'ه': ('0647', 'h'),
    'و': ('0648', 'v'),
    'ی': ('06CC', 'y'),
    'ء': ('0621', 'ʼ'),

    # Vowels
    '◌َ': ('064E', 'a'),
    '◌ُ': ('064F', 'o'),
    '◌ِ': ('0650', 'e'),

    # Hamza forms
    'آ': ('0622', 'ā'),
}
