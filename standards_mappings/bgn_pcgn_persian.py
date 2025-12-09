"""
BGN/PCGN Persian Romanization Mappings

Standard: BGN/PCGN Persian 1958 (Revised 2019)
Status: Corrected 2025-10-21 (fixed U+0674→U+0654)
Total Mappings: 38
"""

from typing import Dict, Tuple

METADATA = {
    'type': 'romanization',
    'table_type': 'persian',
    'column_name': 'BGN/PCGN',
}

# Character mappings: Arabic char → (Unicode code, Romanization)
MAPPINGS: Dict[str, Tuple[str, str]] = {
    # Consonants
    'ا': ('0627', 'ā'),
    'ب': ('0628', 'b'),
    'پ': ('067E', 'p'),
    'ت': ('062A', 't'),
    'ث': ('062B', 's̄'),
    'ج': ('062C', 'j'),
    'چ': ('0686', 'ch'),
    'ح': ('062D', 'ḩ'),
    'خ': ('062E', 'kh'),
    'د': ('062F', 'd'),
    'ذ': ('0630', 'z̄'),
    'ر': ('0631', 'r'),
    'ز': ('0632', 'z'),
    'ژ': ('0698', 'zh'),
    'س': ('0633', 's'),
    'ش': ('0634', 'sh'),
    'ص': ('0635', 'ş'),
    'ض': ('0636', 'ẕ'),
    'ط': ('0637', 'ţ'),
    'ظ': ('0638', 'z̧'),
    'ع': ('0639', 'ʻ'),
    'غ': ('063A', 'gh'),
    'ف': ('0641', 'f'),
    'ق': ('0642', 'q'),
    'ک': ('06A9', 'k'),
    'گ': ('06AF', 'g'),
    'ل': ('0644', 'l'),
    'م': ('0645', 'm'),
    'ن': ('0646', 'n'),
    'ه': ('0647', 'h'),
    'و': ('0648', 'v/ū/ow'),
    'ى': ('0649', 'y/ī/ey'),
    'ی': ('06CC', 'y'),
    '◌ٔ': ('0654', 'ʼ/e/ye'),

    # Vowels
    '◌َ': ('064E', 'a'),
    '◌ُ': ('064F', 'o'),
    '◌ِ': ('0650', 'e'),

    # Hamza forms
    'آ': ('0622', 'ā/ʼā'),
}
