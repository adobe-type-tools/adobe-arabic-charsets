"""
Wikipedia Saraiki IPA Transcription Mappings

Standard: Wikipedia Saraiki IPA (Shahmukhi Script)
URL: https://en.wikipedia.org/wiki/Saraiki_alphabet
Status: Verified 2025-10-22
Total Mappings: 43
"""

from typing import Dict, Tuple

METADATA = {
    'type': 'ipa',
    'language': 'saraiki',
    'table_type': 'AAR4R',
    'column_name': 'WP Saraiki',
}

# Character mappings: Arabic char → (Unicode code, IPA)
MAPPINGS: Dict[str, Tuple[str, str]] = {
    # Consonants
    'ا': ('0627', 'a'),
    'ب': ('0628', 'b'),
    'ٻ': ('067B', 'ɓ'),
    'پ': ('067E', 'p'),
    'ت': ('062A', 't'),
    'ٹ': ('0679', 'ʈ'),
    'ث': ('062B', 's'),
    'ج': ('062C', 'd͡ʒ/ʤ'),
    'ڄ': ('0684', 'ʄ'),
    'چ': ('0686', 't͡ʃ/ʧ'),
    'ح': ('062D', 'ɦ'),
    'خ': ('062E', 'x'),
    'د': ('062F', 'd'),
    'ڈ': ('0688', 'ɖ'),
    'ذ': ('0630', 'z'),
    'ر': ('0631', 'r'),
    'ڑ': ('0691', 'ɽ'),
    'ز': ('0632', 'z'),
    'ژ': ('0698', 'ʒ'),
    'س': ('0633', 's'),
    'ش': ('0634', 'ʃ'),
    'ص': ('0635', 's'),
    'ض': ('0636', 'z'),
    'ط': ('0637', 't'),
    'ظ': ('0638', 'z'),
    'ع': ('0639', '—'),
    'غ': ('063A', 'ɣ'),
    'ف': ('0641', 'f'),
    'ق': ('0642', 'q'),
    'ک': ('06A9', 'k'),
    'ڳ': ('06B3', 'ɠ'),
    'گ': ('06AF', 'g'),
    'ل': ('0644', 'l'),
    'م': ('0645', 'm'),
    'ن': ('0646', 'n'),
    'ں': ('06BA', '◌̃'),
    'ھ': ('06BE', '◌ʰ'),
    'ہ': ('06C1', 'ɦ'),
    'و': ('0648', 'v'),
    'ی': ('06CC', 'j'),
    'ے': ('06D2', 'e'),

    # Other
    'ݙ': ('0759', 'ᶑ'),
    'ݨ': ('0768', 'ɳ'),
}
