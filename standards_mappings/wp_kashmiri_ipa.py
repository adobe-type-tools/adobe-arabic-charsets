"""
Wikipedia Kashmiri IPA Transcription Mappings

Standard: Wikipedia Kashmiri IPA (Perso-Arabic Script)
URL: https://en.wikipedia.org/wiki/Kashmiri_language  # Perso-Arabic_script
Status: Verified 2025-10-22
Total Mappings: 45
"""

from typing import Dict, Tuple

METADATA = {
    'type': 'ipa',
    'language': 'kashmiri',
    'table_type': 'AAR4R',
    'column_name': 'WP Kashmiri IPA',
}

# Character mappings: Arabic char → (Unicode code, Romanization/IPA)
MAPPINGS: Dict[str, Tuple[str, str]] = {
    # Consonants
    'ا': ('0627', '–'),
    'ب': ('0628', 'b'),
    'پ': ('067E', 'p'),
    'ت': ('062A', 't̪'),
    'ٹ': ('0679', 'ʈ'),
    'ث': ('062B', 's'),
    'ج': ('062C', 'd͡ʒ/ʤ'),
    'چ': ('0686', 't͡ʃ/ʧ'),
    'ح': ('062D', 'h'),
    'خ': ('062E', 'x/kʰ'),
    'د': ('062F', 'd̪'),
    'ڈ': ('0688', 'ɖ'),
    'ذ': ('0630', 'z'),
    'ر': ('0631', 'r'),
    'ڑ': ('0691', 'ɽ'),
    'ز': ('0632', 'z'),
    'ژ': ('0698', 't͡s/ʦ'),
    'س': ('0633', 's'),
    'ش': ('0634', 'ʃ'),
    'ص': ('0635', 's'),
    'ض': ('0636', 'z'),
    'ط': ('0637', 't̪'),
    'ظ': ('0638', 'z'),
    'ع': ('0639', '–'),
    'غ': ('063A', 'ɣ/ɡ'),
    'ف': ('0641', 'f/pʰ'),
    'ق': ('0642', 'q/k'),
    'ک': ('0643', 'k'),
    'گ': ('06AF', 'ɡ'),
    'ل': ('0644', 'l'),
    'م': ('0645', 'm'),
    'ن': ('0646', 'n/◌̃'),
    'ں': ('06BA', '◌̃'),
    'و': ('0648', 'ʋ'),
    'ہ': ('06C1', 'h'),
    'ی': ('06CC', 'j'),
    'ے': ('06D2', 'j'),
    'ؠ': ('0620', 'ʲ'),

    # Digraphs
    'پھ': ('067E+06BE', 'pʰ'),
    'تھ': ('062A+06BE', 't̪ʰ'),
    'ٹھ': ('0679+06BE', 'ʈʰ'),
    'چھ': ('0686+06BE', 't͡ʃʰ/ʧʰ'),
    'ژھ': ('0698+06BE', 't͡sʰ/ʦʰ'),
    'کھ': ('0643+06BE', 'kʰ'),
}
