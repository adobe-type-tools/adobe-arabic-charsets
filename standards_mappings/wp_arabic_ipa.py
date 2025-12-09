"""
Wikipedia Arabic IPA Transcription Mappings

Standard: Wikipedia Arabic IPA (Modern Standard Arabic)
URL: https://en.wikipedia.org/wiki/Help:IPA/Arabic
Status: Verified 2025-10-22
Total Mappings: 37
"""

from typing import Dict, Tuple

METADATA = {
    'type': 'ipa',
    'table_type': 'arabic',
    'column_name': 'WP',
}

# Character mappings: Arabic char → (Unicode code, Romanization)
MAPPINGS: Dict[str, Tuple[str, str]] = {
    # Consonants
    'ا': ('0627', 'aː'),
    'ب': ('0628', 'b'),
    'ت': ('062A', 't'),
    'ة': ('0629', 'a/ah'),
    'ث': ('062B', 'θ'),
    'ج': ('062C', 'd͡ʒ/ʤ'),
    'ح': ('062D', 'ħ'),
    'خ': ('062E', 'x'),
    'د': ('062F', 'd'),
    'ذ': ('0630', 'ð'),
    'ر': ('0631', 'r'),
    'ز': ('0632', 'z'),
    'س': ('0633', 's'),
    'ش': ('0634', 'ʃ'),
    'ص': ('0635', 'sˤ'),
    'ض': ('0636', 'dˤ'),
    'ط': ('0637', 'tˤ'),
    'ظ': ('0638', 'ðˤ'),
    'ع': ('0639', 'ʕ'),
    'غ': ('063A', 'ɣ'),
    'ف': ('0641', 'f'),
    'ق': ('0642', 'q'),
    'ك': ('0643', 'k'),
    'ل': ('0644', 'l'),
    'م': ('0645', 'm'),
    'ن': ('0646', 'n'),
    'ه': ('0647', 'h'),
    'و': ('0648', 'w'),
    'ي': ('064A', 'j'),
    'ى': ('0649', 'aː'),
    'ء': ('0621', 'ʔ'),

    # Vowels
    '◌َ': ('064E', 'a'),
    '◌ُ': ('064F', 'u'),
    '◌ِ': ('0650', 'i'),

    # Hamza forms
    'آ': ('0622', 'ʔaː'),

    # Diacritics
    '◌ً': ('064B', 'an'),
    '◌ٌ': ('064C', 'un'),
    '◌ٍ': ('064D', 'in'),
}
