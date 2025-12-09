"""
BGN/PCGN Arabic Romanization Mappings

Standard: BGN/PCGN Arabic 1956 System (Revised 2019)
Status: Verified 2025-10-22
Total Mappings: 47
"""

from typing import Dict, Tuple

METADATA = {
    'type': 'romanization',
    'table_type': 'arabic',
    'column_name': 'BGN/PCGN',
}

# Character mappings: Arabic char → (Unicode code, Romanization)
MAPPINGS: Dict[str, Tuple[str, str]] = {
    # Consonants
    'ا': ('0627', 'ā'),
    'ٱ': ('0671', 'ʼ'),
    'ب': ('0628', 'b'),
    # 'پ': ('067E', 'p'),  # MOVED: Persian/Urdu specific, belongs in AAR2 module
    'ت': ('062A', 't'),
    'ة': ('0629', 'ah/at'),
    'ث': ('062B', 'th'),
    'ج': ('062C', 'j'),
    # 'چ': ('0686', 'ch'),  # MOVED: Persian/Urdu specific, belongs in AAR2 module
    'ح': ('062D', 'ḩ'),
    'خ': ('062E', 'kh'),
    'د': ('062F', 'd'),
    'ذ': ('0630', 'dh'),
    'ر': ('0631', 'r'),
    'ز': ('0632', 'z'),
    'س': ('0633', 's'),
    'ش': ('0634', 'sh'),
    'ص': ('0635', 'ş'),
    'ض': ('0636', 'ḑ'),
    'ط': ('0637', 'ţ'),
    'ظ': ('0638', 'z̧'),
    'ع': ('0639', 'ʻ'),
    'غ': ('063A', 'gh'),
    'ف': ('0641', 'f'),
    'ڤ': ('06A4', 'v'),
    'ق': ('0642', 'q'),
    'ک': ('06A9', 'k'),
    'گ': ('06AF', 'g', 'Iraq'),
    'ل': ('0644', 'l'),
    'م': ('0645', 'm'),
    'ن': ('0646', 'n'),
    'ه': ('0647', 'h'),
    'و': ('0648', 'w/ū'),
    'ي': ('064A', 'y/ay'),
    'ى': ('0649', 'á/ī'),
    'ء': ('0621', 'ʼ'),
    'ڨ': ('06A8', 'g', 'Tunisia'),
    'ڭ': ('06AD', 'ng', 'Morocco'), # NOTE: the source document has '06B4' but shows ڭ.,

    # Vowels
    'او': ('0627+0648', 'āw/aw'),
    'ای': ('0627+064A', 'āy/ī'),
    '◌َ': ('064E', 'a'),
    '◌ُ': ('064F', 'u'),
    '◌ِ': ('0650', 'i'),

    # Hamza forms
    'آ': ('0622', 'ʼā/ā'),
    'أ': ('0623', 'ʼ'),
    'إ': ('0625', 'ʼ'),
    'ؤ': ('0624', 'ʼ'),
    'ئ': ('0626', 'ʼ'),
}

# ==============================================================================
# Characters excluded from Arabic Core (belong in other modules)
# ==============================================================================
# 
# The following characters appear in BGN/PCGN Arabic romanization but are
# excluded from the Arabic Core module because they are Persian/Urdu specific
# and properly belong in the AAR2 (Urdu + Farsi + Punjabi) module:
#
# 'پ': ('067E', 'p'),   # ARABIC LETTER PEH - Persian/Urdu/Punjabi
# 'چ': ('0686', 'ch'),  # ARABIC LETTER TCHEH - Persian/Urdu
#
