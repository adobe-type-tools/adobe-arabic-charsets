"""
ALA-LC Persian Romanization Mappings

Standard: ALA-LC Persian 2012
Status: Verified 2025-10-22
Total Mappings: 32
"""

from typing import Dict, Tuple

METADATA = {
    'type': 'romanization',
    'table_type': 'persian',
    'column_name': 'ALA-LC',
}

# Character mappings: Arabic char → (Unicode code, Romanization)
MAPPINGS: Dict[str, Tuple[str, str]] = {
    'ا': ('0627', 'ā'),
    'ب': ('0628', 'b'),
    'پ': ('067E', 'p'),
    'ت': ('062A', 't'),
    'ث': ('062B', 's̱'),
    'ج': ('062C', 'j'),
    'چ': ('0686', 'ch'),
    'ح': ('062D', 'ḥ'),
    'خ': ('062E', 'kh'),
    'د': ('062F', 'd'),
    'ذ': ('0630', 'ẕ'),
    'ر': ('0631', 'r'),
    'ز': ('0632', 'z'),
    'ژ': ('0698', 'zh'),
    'س': ('0633', 's'),
    'ش': ('0634', 'sh'),
    'ص': ('0635', 'ṣ'),
    'ض': ('0636', 'z̤'),
    'ط': ('0637', 'ṭ'),
    'ظ': ('0638', 'ẓ'),
    'ع': ('0639', 'ʿ'),
    'غ': ('063A', 'gh'),
    'ف': ('0641', 'f'),
    'ق': ('0642', 'q'),
    'ک': ('06A9', 'k'),
    'گ': ('06AF', 'g'),
    'ل': ('0644', 'l'),
    'م': ('0645', 'm'),
    'ن': ('0646', 'n'),
    'ه': ('0647', 'h'),
    'و': ('0648', 'v/ū/aw'),
    'ی': ('064A', 'y/ī/ay'),
    # Consonants
}
