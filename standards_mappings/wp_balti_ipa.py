"""
Wikipedia Balti IPA Transcription Mappings

Standard: Wikipedia Balti IPA (Perso-Arabic Script)
URL: https://en.wikipedia.org/wiki/Balti_language  # Perso-Arabic_alphabet
Status: Verified 2025-10-22
Total Mappings: 45
"""

from typing import Dict, Tuple

METADATA = {
    'type': 'ipa',
    'language': 'balti',
    'table_type': 'AAR4R',
    'column_name': 'WP Balti IPA',
}

# Character mappings: Arabic char → (Unicode code, Romanization/IPA)
MAPPINGS: Dict[str, Tuple[str, str]] = {
    # Consonants
    'ا': ('0627', 'ɑ/ə/e/o'),
    'ب': ('0628', 'b'),
    'پ': ('067E', 'p'),
    'ت': ('062A', 't'),
    'ٹ': ('0679', 'ʈ'),
    'ث': ('062B', 's'),
    'ج': ('062C', 'd͡ʒ/ʤ'),
    'ڃ': ('0683', 'ʒ'),
    'ڇ': ('0687', 'ʈ͡ʂ/ꭧ'),
    'چ': ('0686', 't͡ʃ/ʧ'),
    'ح': ('062D', 'h'),
    'خ': ('062E', 'x'),
    'د': ('062F', 'd'),
    'ڈ': ('0688', 'ɖ'),
    'ذ': ('0630', 'z'),
    'ر': ('0631', 'ɾ'),
    'ڑ': ('0691', 'ɽ'),
    'ڗ': ('0697', 'd͡z/ʣ'),
    'ز': ('0632', 'z'),
    'ژ': ('0698', 't͡s/ʦ'),
    'س': ('0633', 's'),
    'ش': ('0634', 'ʃ'),
    'ݜ': ('075C', 'ʂ'),
    'ص': ('0635', 's'),
    'ض': ('0636', 'z'),
    'ط': ('0637', 't'),
    'ظ': ('0638', 'z'),
    'ع': ('0639', 'ɑ/ə/e/o'),
    'غ': ('063A', 'ʁ/ɢ'),
    'ف': ('0641', 'pʰ/f'),
    'ق': ('0642', 'q'),
    'ک': ('06A9', 'k'),
    'کٔ': ('06A9+0654', 'ɕ'),
    'گ': ('06AF', 'ɡ'),
    'ل': ('0644', 'l/ɭ/ɫ'),
    'م': ('0645', 'm'),
    'ن': ('0646', 'n'),
    'ݨ': ('0768', 'ŋ'),
    'ݩ': ('0769', 'ɲ'),
    'و': ('0648', 'w/u'),
    'ھ': ('06BE', 'ʰ/ʱ'),
    'ہ': ('06C1', 'h'),
    'ی': ('06CC', 'j/i'),
    'ے': ('06D2', 'e'),

    # Other
}
