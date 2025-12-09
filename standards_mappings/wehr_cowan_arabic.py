"""
Wehr/Cowan Arabic Romanization Mappings

Standard: Wehr/Cowan Arabic (Hans Wehr Dictionary, 4th ed. 1994)
Status: Verified 2025-10-22
Total Mappings: 42
"""

from typing import Dict, Tuple

METADATA = {
    'type': 'romanization',
    'table_type': 'arabic',
    'column_name': 'Wehr/Cowan',
}

# Character mappings: Arabic char → (Unicode code, Romanization)
MAPPINGS: Dict[str, Tuple[str, str]] = {
    # Consonants
    'ا': ('0627', 'ā'),
    'ب': ('0628', 'b'),
    # 'پ': ('067E', 'p'),  # MOVED: Persian/Urdu specific, belongs in AAR2 module
    'ت': ('062A', 't'),
    'ة': ('0629', 'ah/at'),
    'ث': ('062B', 'th'),
    'ج': ('062C', 'j'),
    'ح': ('062D', 'ḥ'),
    'خ': ('062E', 'kh'),
    'د': ('062F', 'd'),
    'ذ': ('0630', 'dh'),
    'ر': ('0631', 'r'),
    'ز': ('0632', 'z'),
    # 'ژ': ('0698', 'zh'),  # MOVED: Persian specific, belongs in AAR2 module
    'س': ('0633', 's'),
    'ش': ('0634', 'sh'),
    'ص': ('0635', 'ṣ'),
    'ض': ('0636', 'ḍ'),
    'ط': ('0637', 'ṭ'),
    'ظ': ('0638', 'ẓ'),
    'ع': ('0639', 'ʿ'),
    'غ': ('063A', 'gh'),
    'ف': ('0641', 'f'),
    'ق': ('0642', 'q'),
    'ك': ('0643', 'k'),
    'گ': ('06AF', 'g'),
    'ل': ('0644', 'l'),
    'م': ('0645', 'm'),
    'ن': ('0646', 'n'),
    'ه': ('0647', 'h'),
    'و': ('0648', 'w/ū'),
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
}

# ==============================================================================
# Characters excluded from Arabic Core (belong in other modules)
# ==============================================================================
# 
# The following characters appear in Wehr/Cowan Arabic romanization but are
# excluded from the Arabic Core module because they are Persian/Urdu specific
# and properly belong in the AAR2 (Urdu + Farsi + Punjabi) module:
#
# 'پ': ('067E', 'p'),   # ARABIC LETTER PEH - Persian/Urdu/Punjabi
# 'ژ': ('0698', 'zh'),  # ARABIC LETTER JEH - Persian
#
