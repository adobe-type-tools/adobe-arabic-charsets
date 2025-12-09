"""
OSU Arabic IPA Romanization Mappings

Standard: OSU Arabic IPA (Egyptian Arabic)
Status: Verified 2025-10-22
Total Mappings: 32
"""

from typing import Dict, Tuple

METADATA = {
    'type': 'ipa',
    'table_type': 'arabic',
    'column_name': 'OSU',
}

# Character mappings: Arabic char → (Unicode code, Romanization)
MAPPINGS: Dict[str, Tuple[str, str]] = {
    # Consonants
    'ا': ('0627', 'aː'),
    'ب': ('0628', 'b'),
    'ت': ('062A', 't'),
    'ث': ('062B', 'θ'),
    'ج': ('062C', 'g/ʒ'),
    'ح': ('062D', 'ħ'),
    'خ': ('062E', 'x/ꭓ'),
    'د': ('062F', 'd'),
    'ذ': ('0630', 'ð'),
    'ر': ('0631', 'ɾ/r'),
    'ز': ('0632', 'z'),
    'س': ('0633', 's'),
    'ش': ('0634', 'ʃ'),
    'ص': ('0635', 'sˤ'),
    'ض': ('0636', 'dˤ'),
    'ط': ('0637', 'tˤ'),
    'ظ': ('0638', 'zˤ'),
    'ع': ('0639', 'ʕ'),
    'غ': ('063A', 'ɣ'),
    'ف': ('0641', 'f'),
    'ق': ('0642', 'q'),
    'ك': ('0643', 'kʰ'),
    'ل': ('0644', 'l/ɫ'),
    'م': ('0645', 'm'),
    'ن': ('0646', 'n'),
    'ه': ('0647', 'h'),
    'و': ('0648', 'w/o'),
    'ي': ('064A', 'j/e'),
    'ء': ('0621', 'ʔ'),

    # Vowels
    '◌َ': ('064E', 'a/æ/ɑ'),
    '◌ُ': ('064F', 'u/ʊ'),
    '◌ِ': ('0650', 'i/ɨ/ʉ/ɪ'),
}
