"""
ALA-LC Jawi (Malay) Romanization Mappings

Standard: ALA-LC Jawi-Pegon 2013
URL: https://loc.gov/catdir/cpso/romanization/malay.pdf
Status: New implementation
Total Mappings: ~50

Notes:
- Focuses on Malay pronunciations (not Arabic loanword variations)
- Alif behavior: represents initial vowel or 'a' following consonant
- Hamzah generally omitted in romanization
- Schwa (ĕ/pepet) is contextual, no specific Jawi marker
- Letters marked with (*) in source have different romanizations for Arabic words,
  but this mapping focuses on Malay context only
"""

from typing import Dict, Tuple

METADATA = {
    'type': 'romanization',
    'language': 'malay',
    'table_type': 'AAR5R',
    'column_name': 'ALA-LC Jawi',
}

MAPPINGS = {
    # Consonants - Jawi-specific characters
    'چ': ('0686', 'c'),           # ca/cha,
    'ڎ': ('068E', 'dh'),          # dha (Pegon/Jawi),
    'ڟ': ('069F', 'th'),          # tha (Pegon/Jawi),
    'ڠ': ('06A0', 'ng'),          # nga,
    'ڤ': ('06A4', 'p'),           # pa,
    'ۏ': ('06CF', 'v'),           # va,
    'ڽ': ('06BD', 'ny'),          # nya,
    
    # Standard Arabic letters - Malay pronunciations
    'ا': ('0627', 'a/i/u/e/o'),   # alif (vowel carrier),
    'ب': ('0628', 'b'),
    'ت': ('062A', 't'),
    'ث': ('062B', 's'),           # Malay: s (not th),
    'ج': ('062C', 'j'),
    'ح': ('062D', 'h'),
    'خ': ('062E', 'kh'),
    'د': ('062F', 'd'),
    'ذ': ('0630', 'z'),           # Malay: z (not dh),
    'ر': ('0631', 'r'),
    'ز': ('0632', 'z'),
    'س': ('0633', 's'),
    'ش': ('0634', 'sy'),          # Malay: sy (not sh),
    'ص': ('0635', 's'),           # Malay: s (not ṣ),
    'ض': ('0636', 'd'),           # Malay: d (not ḍ),
    'ط': ('0637', 't'),           # Malay: t (not ṭ),
    'ظ': ('0638', 'l/z'),         # Malay: l or z (not ẓ),
    'ع': ('0639', '—'),           # omitted in Malay,
    'غ': ('063A', 'gh'),
    'ف': ('0641', 'p'),           # Malay: p (not f),
    'ق': ('0642', 'k'),           # Malay: k (not q),
    'ك': ('0643', 'k'),
    'گ': ('06AF', 'g'),
    'ل': ('0644', 'l'),
    'م': ('0645', 'm'),
    'ن': ('0646', 'n'),
    'ه': ('0647', 'h'),
    'و': ('0648', 'w/u/o'),       # wau/vowel,
    'ي': ('064A', 'y/i/e'),       # ya/vowel,
    
    # Vowels and diacritics
    '◌َ': ('064E', 'a'),          # fatha,
    '◌ُ': ('064F', 'u'),          # damma,
    '◌ِ': ('0650', 'i'),          # kasra,
    'اَ': ('0627+064E', 'a'),
    'وُ': ('0648+064F', 'u'),
    'يِ': ('064A+0650', 'i'),
    
    # Diphthongs
    'وَْو': ('0648+064E+0652+0648', 'o'),
    'يَْي': ('064A+064E+0652+064A', 'e/ai'),
    '◌َوْ': ('064E+0648+0652', 'au'),
    '◌َيْ': ('064E+064A+0652', 'ai'),
}

