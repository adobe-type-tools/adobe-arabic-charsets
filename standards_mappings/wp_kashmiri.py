"""
Wikipedia Kashmiri Romanization Mappings

Standard: Wikipedia Kashmiri IPA (Perso-Arabic Script)
URL: https://en.wikipedia.org/wiki/Kashmiri_language  # Perso-Arabic_script
Status: Verified 2025-10-22
Total Mappings: 45
"""

from typing import Dict, Tuple

METADATA = {
    'type': 'romanization',
    'language': 'kashmiri',
    'table_type': 'AAR4R',
    'column_name': 'WP Kashmiri',
}

# Character mappings: Arabic char → (Unicode code, Romanization/IPA)
MAPPINGS: Dict[str, Tuple[str, str]] = {
    # Consonants
    'ا': ('0627', '–'),
    'ب': ('0628', 'b'),
    'پ': ('067E', 'p'),
    'ت': ('062A', 't'),
    'ٹ': ('0679', 'ʈ'),
    'ث': ('062B', 's'),
    'ج': ('062C', 'j'),
    'چ': ('0686', 'ch/č'),
    'ح': ('062D', 'h'),
    'خ': ('062E', 'kh'),
    'د': ('062F', 'd'),
    'ڈ': ('0688', 'ḍ'),
    'ذ': ('0630', 'z'),
    'ر': ('0631', 'r'),
    'ڑ': ('0691', 'ṛ'),
    'ز': ('0632', 'z'),
    'ژ': ('0698', 'ts'),
    'س': ('0633', 's'),
    'ش': ('0634', 'sh/š'),
    'ص': ('0635', 's'),
    'ض': ('0636', 'z'),
    'ط': ('0637', 't'),
    'ظ': ('0638', 'z'),
    'ع': ('0639', '–'),
    'غ': ('063A', 'g/ğ'),
    'ف': ('0641', 'f'),
    'ق': ('0642', 'q'),
    'ک': ('0643', 'k'),
    'گ': ('06AF', 'g'),
    'ل': ('0644', 'l'),
    'م': ('0645', 'm'),
    'ن': ('0646', 'n'),
    'ں': ('06BA', 'ñ'),
    'و': ('0648', 'v/w'),
    'ہ': ('06C1', 'h'),
    'ی': ('06CC', 'y'),
    'ے': ('06D2', 'y'),
    'ؠ': ('0620', 'ʹ'),

    # Digraphs
    'پھ': ('067E+06BE', 'ph'),
    'تھ': ('062A+06BE', 'th'),
    'ٹھ': ('0679+06BE', 'ṭh'),
    'چھ': ('0686+06BE', 'chh/čh'),
    'ژھ': ('0698+06BE', 'tsh'),
    'کھ': ('0643+06BE', 'kh'),
}
