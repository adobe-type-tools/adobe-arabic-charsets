"""
DMG Turkish Romanization Mappings

Standard: DMG Turkish (Ottoman Turkish adaptation)
Status: Verified 2025-10-22
Total Mappings: 49

Turkish-specific adaptations: غ=ğ, و=v (consonant), ق=k
Emphatic letters simplified: ص=s, ض=d, ط=t, ظ=z (no diacritics)
Vowel harmony: short vowels adapt to Turkish phonetics
Long vowels marked with circumflex: â, î, û
"""

from typing import Dict, Tuple

METADATA = {
    'type': 'romanization',
    'table_type': 'turkish',
    'column_name': 'DMG',
}

# Character mappings: Arabic char → (Unicode code, Romanization)
MAPPINGS: Dict[str, Tuple[str, str]] = {
    # Consonants
    'ا': ('0627', 'â'),
    'ب': ('0628', 'b'),
    'پ': ('067E', 'p'),
    'ت': ('062A', 't'),
    'ة': ('0629', 't'),
    'ث': ('062B', 's'),
    'ج': ('062C', 'ǧ'),
    'چ': ('0686', 'č'),
    'ح': ('062D', 'h'),
    'خ': ('062E', 'ḫ'),
    'د': ('062F', 'd'),
    'ذ': ('0630', 'z'),
    'ر': ('0631', 'r'),
    'ز': ('0632', 'z'),
    'ژ': ('0698', 'ž'),
    'س': ('0633', 's'),
    'ش': ('0634', 'š'),
    'ص': ('0635', 's'),
    'ض': ('0636', 'd'),
    'ط': ('0637', 't/d'),
    'ظ': ('0638', 'z'),
    'ع': ('0639', 'ʿ'),
    'غ': ('063A', 'ġ'),
    'ف': ('0641', 'f'),
    'ق': ('0642', 'q'),
    'ك': ('0643', 'k/g'),
    'ک': ('06A9', 'k/g'),
    'ڭ': ('06AD', 'j̈/ŋ'),
    'گ': ('06AF', 'g'),
    'ل': ('0644', 'l'),
    'م': ('0645', 'm'),
    'ن': ('0646', 'n'),
    'ه': ('0647', 'h'),
    'و': ('0648', 'v'),
    'ي': ('064A', 'y'),
    'ى': ('0649', 'y'),
    'ی': ('06CC', 'y'),
    'ء': ('0621', 'ʾ'),

    # Vowels
    '◌َ': ('064E', 'a'),
    '◌ُ': ('064F', 'u/o'),
    '◌ِ': ('0650', 'e/i'),

    # Hamza forms
    'آ': ('0622', 'ʾâ'),
    'أ': ('0623', 'ʾa'),
    'إ': ('0625', 'ʾi'),
    'ؤ': ('0624', 'ʾu'),
    'ئ': ('0626', 'ʾi'),

    # Diacritics
    '◌ً': ('064B', 'an'),
    '◌ٌ': ('064C', 'un'),
    '◌ٍ': ('064D', 'in'),
}
