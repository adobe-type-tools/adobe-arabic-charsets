"""
Wikipedia Kyrgyz IPA Transcription Mappings

Standard: Wikipedia Kyrgyz IPA
URL: https://en.wikipedia.org/wiki/Help:IPA/Kyrgyz
Status: Verified 2025-10-22
Total Mappings: 32
"""

from typing import Dict, Tuple

METADATA = {
    'type': 'ipa',
    'language': 'kyrgyz',
    'table_type': 'ukk',
    'column_name': 'WP Kyrgyz',
}

# Character mappings: Arabic char → (Unicode code, IPA)
MAPPINGS: Dict[str, Tuple[str, str]] = {
    # Consonants
    'ا': ('0627', 'ɑ'),
    'ە': ('06D5', 'e'),
    'ب': ('0628', 'b'),
    'پ': ('067E', 'p'),
    'ت': ('062A', 't'),
    'ج': ('062C', 'dʒ/ʤ'),
    'چ': ('0686', 'tʃ/ʧ'),
    'ح': ('062D', 'ꭓ'),
    'د': ('062F', 'd'),
    'ر': ('0631', 'r'),
    'ز': ('0632', 'z'),
    'س': ('0633', 's'),
    'ش': ('0634', 'ʃ'),
    'ع': ('0639', 'ʁ'),
    'ف': ('0641', 'f'),
    'ق': ('0642', 'q'),
    'ك': ('0643', 'k'),
    'ڭ': ('06AD', 'ŋ'),
    'گ': ('06AF', 'g'),
    'ل': ('0644', 'l'),
    'م': ('0645', 'm'),
    'ن': ('0646', 'n'),
    'و': ('0648', 'o'),
    'ۅ': ('06C5', 'ø'),
    'ۆ': ('06C6', 'v'),
    'ۇ': ('06C7', 'u'),
    'ۉ': ('06C9', 'y'),
    'ي': ('064A', 'j'),
    'ى': ('0649', 'ɯ'),

    # Digraphs
    'تس': ('062A+0633', 'ts/ʦ'),
    'شچ': ('0634+0686', 'ʃtʃ/ʃʧ'),

    # Hamza forms
    'ئ': ('0626', 'i'),
}
