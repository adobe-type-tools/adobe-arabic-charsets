"""
UNGEGN Urdu Romanization Mappings

Standard: UNGEGN Urdu 1972
Status: Verified 2025-10-22
Total Mappings: 39
"""

from typing import Dict, Tuple

METADATA = {
    'type': 'romanization',
    'language': 'urdu',
    'table_type': 'panjab',
    'column_name': 'UNGEGN Urdu',
}

# Character mappings: Arabic char → (Unicode code, Romanization)
MAPPINGS: Dict[str, Tuple[str, str]] = {
    # Consonants
    'ا': ('0627', 'ā'),
    'ب': ('0628', 'b'),
    'پ': ('067E', 'p'),
    'ت': ('062A', 't'),
    'ٹ': ('0679', 'ṭ'),
    'ث': ('062B', 's'),
    'ج': ('062C', 'j'),
    'چ': ('0686', 'ch'),
    'ح': ('062D', 'h'),
    'خ': ('062E', 'ḳh'),
    'د': ('062F', 'd'),
    'ڈ': ('0688', 'ḍ'),
    'ذ': ('0630', 'z'),
    'ر': ('0631', 'r'),
    'ڑ': ('0691', 'ṙ'),
    'ز': ('0632', 'z'),
    'ژ': ('0698', 'ỵ'),
    'س': ('0633', 's'),
    'ش': ('0634', 'sh'),
    'ص': ('0635', 's'),
    'ض': ('0636', 'z'),
    'ط': ('0637', 't'),
    'ظ': ('0638', 'z'),
    'ع': ('0639', 'ʻ'),
    'غ': ('063A', 'gḥ'),
    'ف': ('0641', 'f'),
    'ق': ('0642', 'q'),
    'ک': ('06A9', 'k'),
    'گ': ('06AF', 'g'),
    'ل': ('0644', 'l'),
    'م': ('0645', 'm'),
    'ن': ('0646', 'n'),
    'ں': ('06BA', 'n'),
    'ھ': ('06BE', 'h'),
    'ہ': ('06C1', 'h'),
    'و': ('0648', 'v/ẉ'),
    'ى': ('0649', 'y'),
    'ے': ('06D2', 'e/ai'),

    # Vowels
    '◌َ': ('064E', 'a'),
    '◌ُ': ('064F', 'u'),
    '◌ِ': ('0650', 'i'),
}
