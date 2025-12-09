"""
EI3 Arabic Romanization Mappings

Standard: EI3 Arabic (Encyclopedia of Islam 3rd Edition)
Status: Verified 2025-10-22
Total Mappings: 31
"""

from typing import Dict, Tuple

METADATA = {
    'type': 'romanization',
    'table_type': 'arabic',
    'column_name': 'EI3',
}

# Character mappings: Arabic char → (Unicode code, Romanization)
MAPPINGS: Dict[str, Tuple[str, str]] = {
    'ا': ('0627', 'ā'),
    'ب': ('0628', 'b'),
    'ت': ('062A', 't'),
    'ة': ('0629', 'a/at'),
    'ث': ('062B', 'th'),
    'ج': ('062C', 'j'),
    'ح': ('062D', 'ḥ'),
    'خ': ('062E', 'kh'),
    'د': ('062F', 'd'),
    'ذ': ('0630', 'dh'),
    'ر': ('0631', 'r'),
    'ز': ('0632', 'z'),
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
    'ل': ('0644', 'l'),
    'م': ('0645', 'm'),
    'ن': ('0646', 'n'),
    'ه': ('0647', 'h'),
    'و': ('0648', 'ū/uww'),
    'ي': ('064A', 'ī/iyy'),
    'ى': ('0649', 'ī/iyy'),
    'ء': ('0621', 'ʾ'),
    # Consonants
}
