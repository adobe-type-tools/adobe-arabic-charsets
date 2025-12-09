"""
BGN/PCGN Uyghur Romanization Mappings

Standard: BGN/PCGN Uyghur 2024
Status: Verified 2025-10-22
Total Mappings: 40
"""

from typing import Dict, Tuple

METADATA = {
    'type': 'romanization',
    'language': 'uyghur',
    'table_type': 'ukk',
    'column_name': 'BGN/PCGN',
}

# Character mappings: Arabic char → (Unicode code, Romanization)
MAPPINGS: Dict[str, Tuple[str, str]] = {
    # Consonants
    'ا': ('0627', 'a'),
    'ە': ('06D5', 'e'),
    'ب': ('0628', 'b'),
    'پ': ('067E', 'p'),
    'ت': ('062A', 't'),
    'ج': ('062C', 'j'),
    'چ': ('0686', 'ch'),
    'خ': ('062E', 'x'),
    'د': ('062F', 'd'),
    'ر': ('0631', 'r'),
    'ز': ('0632', 'z'),
    'ژ': ('0698', 'zh'),
    'س': ('0633', 's'),
    'ش': ('0634', 'sh'),
    'غ': ('063A', 'gh'),
    'ف': ('0641', 'f'),
    'ۋ': ('06CB', 'w'),
    'ق': ('0642', 'q'),
    'ك': ('0643', 'k'),
    'ڭ': ('06AD', 'ng'),
    'گ': ('06AF', 'g'),
    'ل': ('0644', 'l'),
    'م': ('0645', 'm'),
    'ن': ('0646', 'n'),
    'ھ': ('06BE', 'h'),
    'و': ('0648', 'o'),
    'ۆ': ('06C6', 'ö'),
    'ۇ': ('06C7', 'u'),
    'ۈ': ('06C8', 'ü'),
    'ي': ('064A', 'y'),
    'ى': ('0649', 'i'),
    'ې': ('06D0', 'ë'),

    # Hamza forms
    'ئا': ('0626+0627', 'a'),
    'ئې': ('0626+06D0', 'ë'),
    'ئە': ('0626+06D5', 'e'),
    'ئى': ('0626+0649', 'i'),
    'ئو': ('0626+0648', 'o'),
    'ئۆ': ('0626+06C6', 'ö'),
    'ئۇ': ('0626+06C7', 'u'),
    'ئۈ': ('0626+06C8', 'ü'),
}
