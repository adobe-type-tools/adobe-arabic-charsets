"""
Wikipedia Uyghur IPA Transcription Mappings

Standard: Wikipedia Uyghur IPA
URL: https://en.wikipedia.org/wiki/Uyghur_Arabic_alphabet
Status: Verified 2025-10-22
Total Mappings: 33
"""

from typing import Dict, Tuple

METADATA = {
    'type': 'ipa',
    'language': 'uyghur',
    'table_type': 'ukk',
    'column_name': 'WP Uyghur',
}

# Character mappings: Arabic char → (Unicode code, IPA)
MAPPINGS: Dict[str, Tuple[str, str]] = {
    # Consonants
    'ا': ('0627', 'ɑ'),
    'ە': ('06D5', 'ɛ'),
    'ب': ('0628', 'b'),
    'پ': ('067E', 'p'),
    'ت': ('062A', 't'),
    'ج': ('062C', 'd͡ʒ/ʤ'),
    'چ': ('0686', 't͡ʃ/ʧ'),
    'خ': ('062E', 'ꭓ'),
    'د': ('062F', 'd'),
    'ر': ('0631', 'r'),
    'ز': ('0632', 'z'),
    'ژ': ('0698', 'ʒ'),
    'س': ('0633', 's'),
    'ش': ('0634', 'ʃ'),
    'غ': ('063A', 'ʁ'),
    'ف': ('0641', 'f'),
    'ۋ': ('06CB', 'v'),
    'ق': ('0642', 'q'),
    'ك': ('0643', 'k'),
    'ڭ': ('06AD', 'ŋ'),
    'گ': ('06AF', 'ɡ'),
    'ل': ('0644', 'l'),
    'م': ('0645', 'm'),
    'ن': ('0646', 'n'),
    'ھ': ('06BE', 'h'),
    'و': ('0648', 'o'),
    'ۆ': ('06C6', 'ø'),
    'ۇ': ('06C7', 'u'),
    'ۈ': ('06C8', 'y'),
    'ي': ('064A', 'j'),
    'ى': ('0649', 'i'),
    'ې': ('06D0', 'e'),

    # Hamza forms
    'ئ': ('0626', 'ʔ'),
}
