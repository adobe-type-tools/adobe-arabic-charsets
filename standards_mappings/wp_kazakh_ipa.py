"""
Wikipedia Kazakh IPA Transcription Mappings

Standard: Wikipedia Kazakh IPA
URL: https://en.wikipedia.org/wiki/Help:IPA/Kazakh
Status: Verified 2025-10-22
Total Mappings: 33
"""

from typing import Dict, Tuple

METADATA = {
    'type': 'ipa',
    'language': 'kazakh',
    'table_type': 'ukk',
    'column_name': 'WP Kazakh',
}

# Character mappings: Arabic char → (Unicode code, IPA)
MAPPINGS: Dict[str, Tuple[str, str]] = {
    'ب': ('0628', 'b'),
    'ش': ('0634', 'ɕ'),
    'د': ('062F', 'd'),
    'ف': ('0641', 'f'),
    'گ': ('06AF', 'ɡ'),
    'ھ': ('06BE', 'h'),
    'ي': ('064A', 'j'),
    'ك': ('0643', 'k'),
    'ل': ('0644', 'l'),
    'م': ('0645', 'm'),
    'ن': ('0646', 'n'),
    'ڭ': ('06AD', 'ɴ'),
    'پ': ('067E', 'p'),
    'ق': ('0642', 'q'),
    'ر': ('0631', 'ɾ'),
    'ع': ('0639', 'ʁ'),
    'س': ('0633', 's'),
    'ت': ('062A', 't'),
    'چ': ('0686', 'tɕ/ʨ'),
    'ۆ': ('06C6', 'v'),
    'ۋ': ('06CB', 'w'),
    'ح': ('062D', 'ꭓ'),
    'ز': ('0632', 'z'),
    'ج': ('062C', 'ʑ'),
    'ا': ('0627', 'ɑ'),
    'ٵ': ('0675', 'æ'),
    'ە': ('06D5', 'e'),
    'ى': ('0649', 'ə'),
    'ٸ': ('0678', 'ɪ'),
    'و': ('0648', 'o'),
    'ٶ': ('0676', 'ø'),
    'ۇ': ('06C7', 'ʊ'),
    'ٷ': ('0677', 'ʏ'),
    # Consonants
    
    # Vowels
}

