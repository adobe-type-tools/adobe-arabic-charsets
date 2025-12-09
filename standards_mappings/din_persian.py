"""
DIN 31635 Persian Romanization Mappings

Standard: DIN 31635 (Persian)
Source: DIN 31635 standard document
Status: VERIFIED 2025-10-16
Total Mappings: 35
"""

from typing import Dict, Tuple

METADATA = {
    'type': 'romanization',
    'table_type': 'persian',
    'column_name': 'DIN',
}

# Character mappings: Persian char → (Unicode code, Romanization)
# Order follows DIN 31635 Persian transliteration table
MAPPINGS: Dict[str, Tuple[str, str]] = {
    'ا': ('0627', 'ā'),
    'ب': ('0628', 'b'),
    'پ': ('067E', 'p'),
    'ت': ('062A', 't'),
    'ث': ('062B', 'ṯ'),
    'ج': ('062C', 'ǧ'),
    'چ': ('0686', 'č'),
    'ح': ('062D', 'ḥ'),
    'خ': ('062E', 'ḫ'),
    'د': ('062F', 'd'),
    'ذ': ('0630', 'ḏ'),
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
    'ک': ('06A9', 'k'),
    'گ': ('06AF', 'g'),
    'ل': ('0644', 'l'),
    'م': ('0645', 'm'),
    'ن': ('0646', 'n'),
    'ه': ('0647', 'h'),
    'و': ('0648', 'w/ū'),
    'ي': ('064A', 'y/ī'),
    'ى': ('0649', 'y/ī'),
    'ی': ('06CC', 'y/ī'),
    'ء': ('0621', 'ʾ'),
    # Consonants
}
