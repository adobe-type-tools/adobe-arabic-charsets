"""
UNGEGN Punjabi Romanization Mappings

Standard: UNGEGN Punjabi (Shahmukhi)
Status: Verified 2025-10-22
Total Mappings: 38
"""

from typing import Dict, Tuple

METADATA = {
    'type': 'romanization',
    'language': 'punjabi',
    'table_type': 'panjab',
    'column_name': 'UNGEGN Punjabi',
}

# Character mappings: Arabic char → (Unicode code, Romanization)
MAPPINGS: Dict[str, Tuple[str, str]] = {
    'ا': ('0627', 'ā'),
    'ب': ('0628', 'b'),
    'پ': ('067E', 'p'),
    'ت': ('062A', 't'),
    'ٹ': ('0679', 'ṭ'),
    'ث': ('062B', 's̱'),
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
    'ھ': ('06BE', 'h'),
    'و': ('0648', 'v'),
    'ی': ('06CC', 'y'),
    'ے': ('06D2', 'ē'),
    'ہ': ('06C1', 'h'),
    # Consonants

    # Combined forms
}
