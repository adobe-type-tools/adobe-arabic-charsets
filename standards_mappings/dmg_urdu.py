"""
DMG Urdu Romanization Mappings

Standard: DMG Urdu
Status: Verified 2025-10-22
Total Mappings: 50

CRITICAL: Retroflex=Oberpunkt (ṫ/ḋ/ṙ dot above), Emphatic=Unterpunkt (ṭ/ḍ dot below)
Nasalization: ṇ (dot below), not ṅ (dot above)
"""

from typing import Dict, Tuple

METADATA = {
    'type': 'romanization',
    'language': 'urdu',
    'table_type': 'panjab',
    'column_name': 'DMG',
}

# Character mappings: Arabic char → (Unicode code, Romanization)
MAPPINGS: Dict[str, Tuple[str, str]] = {
    # Consonants
    'ا': ('0627', 'ā'),
    'ب': ('0628', 'b'),
    'پ': ('067E', 'p'),
    'ت': ('062A', 't'),
    'ٹ': ('0679', 'ṫ'),
    'ث': ('062B', 's̱'),
    'ٿ': ('067F', 'ṫ'),
    'ج': ('062C', 'ǧ'),
    'چ': ('0686', 'č'),
    'ح': ('062D', 'ḥ'),
    'خ': ('062E', 'ḫ'),
    'د': ('062F', 'd'),
    'ڈ': ('0688', 'ḋ'),
    'ذ': ('0630', 'ẕ'),
    'ر': ('0631', 'r'),
    'ڑ': ('0691', 'ṙ'),
    'ز': ('0632', 'z'),
    'ژ': ('0698', 'ž'),
    'س': ('0633', 's'),
    'ش': ('0634', 'š'),
    'ص': ('0635', 'ṣ'),
    'ض': ('0636', 'ż'),
    'ط': ('0637', 'ṭ'),
    'ظ': ('0638', 'ẓ'),
    'ع': ('0639', 'ʿ'),
    'غ': ('063A', 'ġ'),
    'ف': ('0641', 'f'),
    'ق': ('0642', 'q'),
    'ك': ('0643', 'k'),
    'ک': ('06A9', 'k'),
    'گ': ('06AF', 'g'),
    'ل': ('0644', 'l'),
    'م': ('0645', 'm'),
    'ن': ('0646', 'n/ṇ'),
    'ں': ('06BA', 'ṇ'),
    'ھ': ('06BE', 'h'),
    'ہ': ('06C1', 'h'),
    'و': ('0648', 'w/ū/o/ō'),
    'ي': ('064A', 'y/ī'),
    'ی': ('06CC', 'y/ī'),
    'ے': ('06D2', 'e/ē'),
    'ء': ('0621', 'ʾ'),

    # Vowels
    '◌َ': ('064E', 'a'),
    '◌ُ': ('064F', 'u'),
    '◌ِ': ('0650', 'i'),

    # Hamza forms
    'آ': ('0622', 'ʾā'),
    'أ': ('0623', 'ʾa'),
    'إ': ('0625', 'ʾi'),
    'ؤ': ('0624', 'ʾu'),
    'ئ': ('0626', 'ʾi'),
}
