"""
Wikipedia Kurdish IPA Transcription Mappings

Standard: Wikipedia Kurdish IPA (Central Kurdish/Sorani)
URL: https://en.wikipedia.org/wiki/Help:IPA/Kurdish
Status: Verified 2025-10-22
Total Mappings: 35
"""

from typing import Dict, Tuple

METADATA = {
    'type': 'ipa',
    'language': 'kurdish',
    'table_type': 'AAR5R',
    'column_name': 'WP Kurdish',
}

# Character mappings: Arabic char → (Unicode code, IPA)
MAPPINGS: Dict[str, Tuple[str, str]] = {
    # Consonants
    'ا': ('0627', 'ɑː'),
    'ە': ('06D5', 'ɛ'),
    'ب': ('0628', 'b'),
    'پ': ('067E', 'p'),
    'ت': ('062A', 't'),
    'ج': ('062C', 'd͡ʒ/ʤ'),
    'چ': ('0686', 't͡ʃ/ʧ'),
    'ح': ('062D', 'ħ'),
    'خ': ('062E', 'x'),
    'د': ('062F', 'd'),
    'ر': ('0631', 'ɾ'),
    'ڕ': ('0695', 'r'),
    'ز': ('0632', 'z'),
    'ژ': ('0698', 'ʒ'),
    'س': ('0633', 's'),
    'ش': ('0634', 'ʃ'),
    'غ': ('063A', 'ɣ'),
    'ف': ('0641', 'f'),
    'ڤ': ('06A4', 'v'),
    'ق': ('0642', 'q'),
    'ک': ('06A9', 'k'),
    'گ': ('06AF', 'ɡ'),
    'ل': ('0644', 'l'),
    'ڵ': ('06B5', 'ɫ'),
    'م': ('0645', 'm'),
    'ن': ('0646', 'n'),
    'ھ': ('06BE', 'h'),
    'و': ('0648', 'w'),
    'ۆ': ('06C6', 'oː'),
    'ى': ('0649', 'iː'),
    'ی': ('06CC', 'j'),
    'ێ': ('06CE', 'eː'),

    # Vowels
    'نٚ': ('0646+065A', 'ŋ'),
    'وو': ('0648+0648', 'uː'),
}
