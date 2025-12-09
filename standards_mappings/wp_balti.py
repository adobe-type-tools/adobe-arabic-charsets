"""
Wikipedia Balti Romanization Mappings

Standard: Wikipedia Balti IPA (Perso-Arabic Script)
URL: https://en.wikipedia.org/wiki/Balti_language  # Perso-Arabic_alphabet
Status: Verified 2025-10-22
Total Mappings: 45
"""

from typing import Dict, Tuple

METADATA = {
    'type': 'romanization',
    'language': 'balti',
    'table_type': 'AAR4R',
    'column_name': 'WP Balti',
}

# Character mappings: Arabic char → (Unicode code, Romanization/IPA)
MAPPINGS: Dict[str, Tuple[str, str]] = {
    # Consonants
    'ا': ('0627', 'ā/a/e/o'),
    'ب': ('0628', 'b'),
    'پ': ('067E', 'p'),
    'ت': ('062A', 't'),
    'ٹ': ('0679', 'ṭ'),
    'ث': ('062B', 's'),
    'ج': ('062C', 'j'),
    'ڃ': ('0683', 'ž'),
    'ڇ': ('0687', 'č̣'),
    'چ': ('0686', 'č'),
    'ح': ('062D', 'h'),
    'خ': ('062E', 'x'),
    'د': ('062F', 'd'),
    'ڈ': ('0688', 'ḍ'),
    'ذ': ('0630', 'z'),
    'ر': ('0631', 'r'),
    'ڑ': ('0691', 'ṛ'),
    'ڗ': ('0697', 'đ/dz'),
    'ز': ('0632', 'z'),
    'ژ': ('0698', 'c/ts'),
    'س': ('0633', 's'),
    'ش': ('0634', 'š'),
    'ݜ': ('075C', 'ʂ'),
    'ص': ('0635', 's'),
    'ض': ('0636', 'z'),
    'ط': ('0637', 't'),
    'ظ': ('0638', 'z'),
    'ع': ('0639', 'ā/a/e/o'),
    'غ': ('063A', 'ǧ'),
    'ف': ('0641', 'f'),
    'ق': ('0642', 'q'),
    'ک': ('06A9', 'k'),
    'کٔ': ('06A9+0654', 'ǩ/ṡ'),
    'گ': ('06AF', 'g'),
    'ل': ('0644', 'l'),
    'م': ('0645', 'm'),
    'ن': ('0646', 'n'),
    'ݨ': ('0768', 'ŋ/ng'),
    'ݩ': ('0769', 'ň/ny'),
    'و': ('0648', 'w/u'),
    'ھ': ('06BE', 'h'),
    'ہ': ('06C1', 'h'),
    'ی': ('06CC', 'y/i'),
    'ے': ('06D2', 'e/ay'),
}
