"""
DMG Arabic Romanization Mappings

Standard: DMG Arabic
Status: Verified 2025-10-22
Total Mappings: 46
"""

from typing import Dict, Tuple

METADATA = {
    'type': 'romanization',
    'table_type': 'arabic',
    'column_name': 'DMG',
}

# Character mappings: Arabic char → (Unicode code, Romanization)
MAPPINGS: Dict[str, Tuple[str, str]] = {
    # Consonants
    'ا': ('0627', 'ā'),
    'ب': ('0628', 'b'),
    # 'پ': ('067E', 'p'),  # MOVED: Persian/Urdu specific, belongs in AAR2 module
    'ت': ('062A', 't'),
    'ة': ('0629', 'h/t'),
    'ث': ('062B', 'ṯ/s̱'),
    'ج': ('062C', 'ǧ'),
    # 'چ': ('0686', 'č'),  # MOVED: Persian/Urdu specific, belongs in AAR2 module
    'ح': ('062D', 'ḥ'),
    'خ': ('062E', 'ḫ'),
    'د': ('062F', 'd'),
    'ذ': ('0630', 'ḏ/ẕ'),
    'ر': ('0631', 'r'),
    'ز': ('0632', 'z'),
    # 'ژ': ('0698', 'ž'),  # MOVED: Persian specific, belongs in AAR2 module
    'س': ('0633', 's'),
    'ش': ('0634', 'š'),
    'ص': ('0635', 'ṣ'),
    'ض': ('0636', 'ḍ/ż'),
    'ط': ('0637', 'ṭ'),
    'ظ': ('0638', 'ẓ'),
    'ع': ('0639', 'ʿ'),
    'غ': ('063A', 'ġ'),
    'ف': ('0641', 'f'),
    'ق': ('0642', 'q'),
    'ك': ('0643', 'k'),
    'گ': ('06AF', 'g'),
    'ل': ('0644', 'l'),
    'م': ('0645', 'm'),
    'ن': ('0646', 'n'),
    'ه': ('0647', 'h'),
    'و': ('0648', 'w/v/ū'),
    'ي': ('064A', 'y/ī'),
    'ى': ('0649', 'ā'),
    'ء': ('0621', 'ʾ'),

    # Vowels
    '◌َ': ('064E', 'a'),
    '◌ُ': ('064F', 'u'),
    '◌ِ': ('0650', 'i'),

    # Hamza forms
    'آ': ('0622', 'ʾā'),
    'أ': ('0623', 'ʾa'),
    'إ': ('0625', 'ʾi'),
    'ؤ': ('0624', 'ʾu'),
    'ئ': ('0626', 'ʾi'),

    # Diacritics
    '◌ً': ('064B', 'an'),
    '◌ٌ': ('064C', 'un'),
    '◌ٍ': ('064D', 'in'),
}

# ==============================================================================
# Characters excluded from Arabic Core (belong in other modules)
# ==============================================================================
# 
# The following characters appear in DMG Arabic romanization but are
# excluded from the Arabic Core module because they are Persian/Urdu specific
# and properly belong in the AAR2 (Urdu + Farsi + Punjabi) module:
#
# 'پ': ('067E', 'p'),   # ARABIC LETTER PEH - Persian/Urdu/Punjabi
# 'چ': ('0686', 'č'),   # ARABIC LETTER TCHEH - Persian/Urdu
# 'ژ': ('0698', 'ž'),   # ARABIC LETTER JEH - Persian
#
