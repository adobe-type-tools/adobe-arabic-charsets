"""
ISO 233-2 Arabic Romanization Mappings

Standard: ISO 233-2:1993 (Simplified romanization)
URL: https://en.wikipedia.org/wiki/Romanization_of_Arabic
Status: Verified 2025-10-22
Total Mappings: 42
"""

from typing import Dict, Tuple

METADATA = {
    'type': 'romanization',
    'table_type': 'arabic',
    'column_name': 'ISO 233-2',
}

# Character mappings: Arabic char → (Unicode code, Romanization)
MAPPINGS: Dict[str, Tuple[str, str]] = {
    # Consonants
    'ا': ('0627', 'ʾ'),
    'ب': ('0628', 'b'),
    'ت': ('062A', 't'),
    'ة': ('0629', 'ẗ'),
    'ث': ('062B', 'ṯ'),
    'ج': ('062C', 'ǧ'),
    'ح': ('062D', 'ḥ'),
    'خ': ('062E', 'ẖ'),
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
    'ى': ('0649', 'ỳ'),
    'ء': ('0621', 'ˈ/ˌ'),

    # Vowels
    '◌َ': ('064E', 'a'),
    '◌ُ': ('064F', 'u'),
    '◌ِ': ('0650', 'i'),

    # Hamza forms
    'آ': ('0622', 'ʾā/ā'),
    'أ': ('0623', 'ʾa'),
    'إ': ('0625', 'ʾi'),
    'ؤ': ('0624', 'ʾu'),
    'ئ': ('0626', 'ʾi'),

    # Diacritics
    '◌ً': ('064B', 'an'),
    '◌ٌ': ('064C', 'un'),
    '◌ٍ': ('064D', 'in'),
}
