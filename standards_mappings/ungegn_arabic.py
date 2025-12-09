"""
UNGEGN Arabic Romanization Mappings

Standard: UNGEGN Arabic 2018
Status: Verified 2025-10-22
Total Mappings: 32
"""

from typing import Dict, Tuple

METADATA = {
    'type': 'romanization',
    'table_type': 'arabic',
    'column_name': 'UNGEGN',
}

# Character mappings: Arabic char → (Unicode code, Romanization)
MAPPINGS: Dict[str, Tuple[str, str]] = {
    # Consonants
    'ا': ('0627', 'ā'),
    'ب': ('0628', 'b'),
    'ت': ('062A', 't'),
    'ث': ('062B', 'th'),
    'ج': ('062C', 'j'),
    'ح': ('062D', 'ẖ/ḩ'),
    'خ': ('062E', 'kh'),
    'د': ('062F', 'd'),
    'ذ': ('0630', 'dh'),
    'ر': ('0631', 'r'),
    'ز': ('0632', 'z'),
    'س': ('0633', 's'),
    'ش': ('0634', 'sh'),
    'ص': ('0635', 's̱/ş'),
    'ض': ('0636', 'ḏ/ḑ'),
    'ط': ('0637', 'ṯ/ṭ'),
    'ظ': ('0638', 'd͟h/z̧'),
    'ع': ('0639', 'ʿ'),
    'غ': ('063A', 'gh'),
    'ف': ('0641', 'f'),
    'ق': ('0642', 'q'),
    'ک': ('0643', 'k'),
    'ل': ('0644', 'l'),
    'م': ('0645', 'm'),
    'ن': ('0646', 'n'),
    'ه': ('0647', 'h'),
    'و': ('0648', 'w'),
    'ي': ('064A', 'y'),
    'ء': ('0621', 'ʾ'),

    # Hamza forms
    'آ': ('0622', 'ʾā'),
    'أ': ('0623', 'ʾa'),
    'إ': ('0625', 'ʾi'),
}
