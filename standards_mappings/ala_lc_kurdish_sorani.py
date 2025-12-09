"""
ALA-LC Kurdish (Sorani) Romanization Mappings

Standard: ALA-LC Kurdish (Sorani) 2012
URL: https://loc.gov/catdir/cpso/romanization/kurdish.pdf
Status: Verified 2025-10-22
Total Mappings: 42
Note: Removed presentation form entries (ﯪ ﰄ ﯲ ﯮ ﮪ) which had incorrect
      Unicode codes (Telugu/Tibetan). These are visual forms of base sequences
      already mapped (hamza combinations and base letters).
"""

from typing import Dict, Tuple

METADATA = {
    'type': 'romanization',
    'language': 'kurdish',
    'table_type': 'AAR5R',
    'column_name': 'ALA-LC Kurdish',
}

MAPPINGS = {
    # Consonants
    'ا': ('0627', 'a'),
    'ب': ('0628', 'b'),
    'پ': ('067E', 'p/pʼ'),
    'ت': ('062A', 't/tʼ'),
    'ج': ('062C', 'c'),
    'چ': ('0686', 'ç'),
    'ح': ('062D', 'ḧ/hʼ'),
    'خ': ('062E', 'x'),
    'د': ('062F', 'd'),
    'ر': ('0631', 'r'),
    'ڕ': ('0695', 'r̄'),
    'ز': ('0632', 'z'),
    'ژ': ('0698', 'j'),
    'س': ('0633', 's'),
    'ش': ('0634', 'ș/ş'),
    'ص': ('0635', 'ṣ'),
    'ض': ('0636', 'ḍ'),
    'ط': ('0637', 'ṭ'),
    'ع': ('0639', "ʻ"),
    'غ': ('063A', 'ẍ'),
    'ف': ('0641', 'f'),
    'ڤ': ('06A4', 'v'),
    'ق': ('0642', 'q'),
    'ك': ('0643', 'k'),
    'ک': ('06A9', 'k/kʼ'),
    'گ': ('06AF', 'g'),
    'ل': ('0644', 'l'),
    'ڵ': ('06B5', 'ł'),
    'م': ('0645', 'm'),
    'ن': ('0646', 'n'),
    'ه': ('0647', 'e'),
    'ھ': ('06BE', 'h'),
    'و': ('0648', 'u/w'),
    'ۆ': ('06C6', 'o'),
    'ي': ('064A', 'î/y'),
    'ی': ('06CC', 'î/y'),
    'ێ': ('06CE', 'ê'),

    # Vowels
    'ﻋﻪ': ('0639+0647', "ʻe/eʼ"),
    'وو': ('0648+0648', 'û'),
    '◌ِ': ('0650', 'i'),

    # Hamza forms (initial vowels begin with kursî hamza ئ)
    'ﺋێ': ('0626+06CE', 'ê'),
    'ﺋﻪ': ('0626+0647', 'e'),
    'ﺋِ': ('0626+0650', 'i'),
}
