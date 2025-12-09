"""
EI3 Urdu/Punjabi Romanization Mappings

Standard: EI3 Urdu/Punjabi (Encyclopedia of Islam 3rd Edition)
Status: Verified 2025-10-22
Total Mappings: 51
"""

from typing import Dict, Tuple, List, Union

METADATA = {
    'type': 'romanization',
    'language': ['urdu', 'punjabi'],
    'table_type': 'panjab',
    'column_name': 'EI3',
}

# Character mappings: Arabic char → (Unicode code, Romanization)
MAPPINGS: Dict[str, Tuple[str, str]] = {
    # Consonants
    'ا': ('0627', 'ā'),
    'ب': ('0628', 'b'),
    'پ': ('067E', 'p'),
    'ت': ('062A', 't'),
    'ٹ': ('0679', 'ṭ'),
    'ث': ('062B', 'th'),
    'ج': ('062C', 'j'),
    'چ': ('0686', 'ch'),
    'ح': ('062D', 'ḥ'),
    'خ': ('062E', 'kh'),
    'د': ('062F', 'd'),
    'ڈ': ('0688', 'ḍ'),
    'ذ': ('0630', 'dh'),
    'ر': ('0631', 'r'),
    'ڑ': ('0691', 'ṛ'),
    'ز': ('0632', 'z'),
    'ژ': ('0698', 'zh'),
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
    'ک': ('06A9', 'k'),
    'گ': ('06AF', 'g'),
    'ل': ('0644', 'l'),
    'م': ('0645', 'm'),
    'ن': ('0646', 'n'),
    'ں': ('06BA', 'ṅ'),
    'ه': ('0647', 'h'),
    'ھ': ('06BE', 'h'),
    'و': ('0648', 'w'),
    'ی': ('06CC', 'y'),
    'ے': ('06D2', 'ē'),
    'ء': ('0621', 'ʾ'),

    # Digraphs
    'بھ': ('0628+06BE', 'b͟h'),
    'پھ': ('067E+06BE', 'p͟h'),
    'تھ': ('062A+06BE', 't͟h'),
    'جھ': ('062C+06BE', 'j͟h'),
    'چھ': ('0686+06BE', 'c͟h͟h'),
    'دھ': ('062F+06BE', 'd͟h'),
    'ڈھ': ('0688+06BE', 'ď͟h'),
    'کھ': ('06A9+06BE', 'k͟h'),
    'گھ': ('06AF+06BE', 'g͟h'),
    'لھ': ('0644+06BE', 'l͟h'),
    'نھ': ('0646+06BE', 'n͟h'),

    # Hamza forms
    'آ': ('0622', 'ʾā'),
}
