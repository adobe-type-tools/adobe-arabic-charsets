"""
EI3 Ottoman Turkish Romanization Mappings

Standard: EI3 Ottoman Turkish (Encyclopedia of Islam 3rd Edition)
Status: Verified 2025-10-22
Total Mappings: 43
"""

from typing import Dict, Tuple

METADATA = {
    'type': 'romanization',
    'table_type': 'turkish',
    'column_name': 'EI3',
}

# Character mappings: Arabic char → (Unicode code, Romanization)
MAPPINGS: Dict[str, Tuple[str, str]] = {
    # Consonants
    'ا': ('0627', 'ʾ/ā'),
    'ب': ('0628', 'b'),
    'پ': ('067E', 'p'),
    'ت': ('062A', 't'),
    'ة': ('0629', 'at'),
    'ث': ('062B', 'th'),
    'ج': ('062C', 'c'),
    'چ': ('0686', 'ç'),
    'ح': ('062D', 'ḥ'),
    'خ': ('062E', 'kh'),
    'د': ('062F', 'd'),
    'ذ': ('0630', 'dh'),
    'ر': ('0631', 'r'),
    'ز': ('0632', 'z'),
    'ژ': ('0698', 'zh'),
    'س': ('0633', 's'),
    'ش': ('0634', 'ş'),
    'ص': ('0635', 'ṣ'),
    'ض': ('0636', 'ḍ'),
    'ط': ('0637', 'ṭ'),
    'ظ': ('0638', 'ẓ'),
    'ع': ('0639', 'ʿ'),
    'غ': ('063A', 'gh'),
    'ف': ('0641', 'f'),
    'ق': ('0642', 'q'),
    'ك': ('0643', 'k/g/ğ/ñ'),
    'ک': ('06A9', 'k/g/ğ/ñ'),
    'ڭ': ('06AD', 'ñ'),
    'گ': ('06AF', 'g'),
    'ل': ('0644', 'l'),
    'م': ('0645', 'm'),
    'ن': ('0646', 'n'),
    'ه': ('0647', 'h/e/at'),
    'و': ('0648', 'v/ū/w'),
    'ي': ('064A', 'ī/iyye'),
    'ى': ('0649', 'ī/iyye'),
    'ی': ('06CC', 'ī/iyye'),
    'ء': ('0621', 'ʾ'),

    # Hamza forms
    'آ': ('0622', 'ʾā'),
    'أ': ('0623', 'ʾa'),
    'إ': ('0625', 'ʾi'),
    'ؤ': ('0624', 'ʾu'),
    'ئ': ('0626', 'ʾi'),
}
