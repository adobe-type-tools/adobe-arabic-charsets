"""
UMich Arabic IPA Romanization Mappings

Standard: UMich Arabic IPA
URL: https://sites.lsa.umich.edu/jalt/ipa-symbols/
Status: Verified 2025-10-22
Total Mappings: 32
"""

from typing import Dict, Tuple

METADATA = {
    'type': 'ipa',
    'table_type': 'arabic',
    'column_name': 'UMich',
}

# Character mappings: Arabic char → (Unicode code, Romanization)
MAPPINGS: Dict[str, Tuple[str, str]] = {
    # Consonants
    'ا': ('0627', 'ā'),
    'ب': ('0628', 'b'),
    'ت': ('062A', 't'),
    'ث': ('062B', 'θ'),
    'ج': ('062C', 'g'),
    'ح': ('062D', 'ħ/ʜ/ḥ'),
    'خ': ('062E', 'x'),
    'د': ('062F', 'd'),
    'ذ': ('0630', 'ð'),
    'ر': ('0631', 'r'),
    'ز': ('0632', 'z'),
    'س': ('0633', 's'),
    'ش': ('0634', 'ʃ/š'),
    'ص': ('0635', 'ş/sˠ/sˤ/ṣ'),
    'ض': ('0636', 'ď/dˠ/dˤ/ḍ'),
    'ط': ('0637', 'ţ/t̃/tˠ/tˤ/ṭ'),
    'ظ': ('0638', 'đ/ð̃/ðˠ/ðˤ/ẓ'),
    'ع': ('0639', 'ʕ/ʢ/ʻ/ʿ'),
    'غ': ('063A', 'ɣ'),
    'ف': ('0641', 'f'),
    'ق': ('0642', 'q/ɢ'),
    'ك': ('0643', 'k'),
    'ل': ('0644', 'l'),
    'م': ('0645', 'm'),
    'ن': ('0646', 'n'),
    'ه': ('0647', 'h'),
    'و': ('0648', 'w/ū'),
    'ي': ('064A', 'y/ī'),
    'ء': ('0621', 'ʔ/ʼ'),

    # Vowels
    '◌َ': ('064E', 'a'),
    '◌ُ': ('064F', 'u'),
    '◌ِ': ('0650', 'i'),
}
