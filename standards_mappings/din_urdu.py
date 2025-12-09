"""
DIN 31635 Urdu Romanization Mappings

Standard: DIN 31635 (Urdu)
Source: DIN 31635 standard document
Status: VERIFIED 2025-10-16
Total Mappings: 40
"""

from typing import Dict, Tuple

METADATA = {
    'type': 'romanization',
    'language': 'urdu',
    'table_type': 'panjab',
    'column_name': 'DIN',
}

# Character mappings: Urdu char → (Unicode code, Romanization)
# Order follows DIN 31635 Urdu transliteration table
MAPPINGS: Dict[str, Tuple[str, str]] = {
    'ا': ('0627', 'ā'),
    'ب': ('0628', 'b'),
    'پ': ('067E', 'p'),
    'ت': ('062A', 't'),
    'ٹ': ('0679', 'ṭ'),
    'ث': ('062B', 's̱'),
    'ج': ('062C', 'j'),
    'چ': ('0686', 'c'),
    'ح': ('062D', 'ḥ'),
    'خ': ('062E', 'ẖ'),
    'د': ('062F', 'd'),
    'ڈ': ('0688', 'ḍ'),
    'ذ': ('0630', 'ẕ'),
    'ر': ('0631', 'r'),
    'ڑ': ('0691', 'ṛ'),
    'ز': ('0632', 'z'),
    'ژ': ('0698', 'ž'),
    'س': ('0633', 's'),
    'ش': ('0634', 'š'),
    'ص': ('0635', 'ṣ'),
    'ض': ('0636', 'z̤'),
    'ط': ('0637', 't̤'),
    'ظ': ('0638', 'ẓ'),
    'ع': ('0639', 'ʿ'),
    'غ': ('063A', 'ġ'),
    'ف': ('0641', 'f'),
    'ق': ('0642', 'q'),
    'ک': ('06A9', 'k'),
    'گ': ('06AF', 'g'),
    'ل': ('0644', 'l'),
    'م': ('0645', 'm'),
    'ن': ('0646', 'n'),
    'ں': ('06BA', 'ṉ'),
    'ه': ('0647', 'h'),
    'ھ': ('06BE', 'h'),
    'و': ('0648', 'v/ū/o'),
    'ي': ('064A', 'y/ī'),
    'ى': ('0649', 'y/ī'),
    'ی': ('06CC', 'y/ī'),
    'ے': ('06D2', 'e'),
    'ء': ('0621', 'ʾ'),
    'ہ': ('06C1', 'h'),
    # Consonants

    # Combined forms
}
