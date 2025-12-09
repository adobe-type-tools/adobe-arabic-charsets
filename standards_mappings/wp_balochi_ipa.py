"""
Wikipedia Balochi IPA Transcription Mappings

Standard: Wikipedia Balochi IPA
URL: https://en.wikipedia.org/wiki/Balochi_alphabets
Status: Verified 2025-10-22
Total Mappings: 32
"""

from typing import Dict, Tuple

METADATA = {
    'type': 'ipa',
    'language': 'balochi',
    'table_type': 'AAR5R',
    'column_name': 'WP Balochi',
}

# Character mappings: Arabic char → (Unicode code, IPA)
MAPPINGS: Dict[str, Tuple[str, str]] = {
    # Consonants
    'ا': ('0627', 'a'),
    'ب': ('0628', 'b'),
    'پ': ('067E', 'p'),
    'ت': ('062A', 't̪'),
    'ٹ': ('0679', 'ʈ'),
    'ج': ('062C', 'd͡ʒ/ʤ'),
    'چ': ('0686', 't͡ʃ/ʧ'),
    'د': ('062F', 'd̪'),
    'ڈ': ('0688', 'ɖ'),
    'ر': ('0631', 'ɾ'),
    'ز': ('0632', 'z'),
    'ژ': ('0698', 'ʒ'),
    'س': ('0633', 's'),
    'ش': ('0634', 'ʃ'),
    'ف': ('0641', 'f'),
    'ک': ('06A9', 'k'),
    'گ': ('06AF', 'ɡ'),
    'ل': ('0644', 'l'),
    'م': ('0645', 'm'),
    'ن': ('0646', 'n'),
    'ھ': ('06BE', 'h'),
    'ہ': ('06C1', 'h'),
    'و': ('0648', 'w'),
    'ی': ('06CC', 'j'),
    'ے': ('06D2', 'eː'),
    'ۏ': ('06CF', 'oː'),

    # Vowels
    '◌َ': ('064E', 'a'),
    '◌ُ': ('064F', 'o'),
    '◌ِ': ('0650', 'e'),

    # Hamza forms
    'آ': ('0622', 'ɑ'),
    'ؤ': ('0624', 'ɑuː'),
    'ئ': ('0626', 'ɛ'),
    'ئی': ('0626+06CC', 'ɑiː'),
}
