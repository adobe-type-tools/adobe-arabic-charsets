"""
OSU Persian IPA Romanization Mappings

Standard: OSU Persian IPA
Status: Verified 2025-10-22
Total Mappings: 30

Persian phonetic transcription from Ohio State University.
Includes phonemic and allophonic variants.
Symbols in brackets represent non-phonemic sounds.
"""

from typing import Dict, Tuple

METADATA = {
    'type': 'ipa',
    'table_type': 'persian',
    'column_name': 'OSU',
}

# Character mappings: Arabic char → (Unicode code, Romanization)
MAPPINGS: Dict[str, Tuple[str, str]] = {
    # Consonants
    'ا': ('0627', 'ɒ'),
    'ب': ('0628', 'b'),
    'پ': ('067E', 'pʰ'),
    'ت': ('062A', 'tʰ'),
    'ث': ('062B', 's'),
    'ج': ('062C', 'd͡ʒ'),
    'چ': ('0686', 't͡ʃ'),
    'ح': ('062D', 'h'),
    'خ': ('062E', 'x'),
    'د': ('062F', 'd'),
    'ر': ('0631', 'ɾ/r/ɹ'),
    'ژ': ('0698', 'ʒ'),
    'ش': ('0634', 'ʃ'),
    'ظ': ('0638', 'z'),
    'ف': ('0641', 'f'),
    'ق': ('0642', 'ɢ'),
    'ک': ('06A9', 'kʰ'),
    'گ': ('06AF', 'ɡ'),
    'ل': ('0644', 'l'),
    'م': ('0645', 'm'),
    'ن': ('0646', 'n'),
    'ه': ('0647', 'h/æ'),
    'و': ('0648', 'v/u/oʊ'),
    'ى': ('0649', 'i/eɪ'),
    'ی': ('06CC', 'j/i/eɪ'),
    'ء': ('0621', 'ʔ'),

    # Vowels
    '◌َ': ('064E', 'æ'),
    '◌ُ': ('064F', 'u'),
    '◌ِ': ('0650', 'i'),

    # Hamza forms
    'آ': ('0622', 'ʔɒ'),
}
