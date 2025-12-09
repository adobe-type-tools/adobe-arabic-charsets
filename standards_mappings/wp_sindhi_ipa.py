"""
Wikipedia Sindhi IPA Transcription Mappings

Standard: Wikipedia Sindhi IPA (Perso-Arabic Script)
URL: https://en.wikipedia.org/wiki/Sindhi_language#Perso-Arabic_script
Status: Verified 2025-10-22
Total Mappings: 62

Note: Mappings contain IPA values from Wikipedia's Sindhi alphabet table.
Multi-character sequences (digraphs) are included.
Characters marked as loanwords (shaded yellow in Wikipedia) are included but
represent sounds also available through native letters.
"""

from typing import Dict, Tuple

METADATA = {
    'type': 'ipa',
    'language': 'sindhi',
    'table_type': 'AAR5R',
    'column_name': 'WP Sindhi',
}

# Character mappings: Arabic char → (Unicode code, IPA)
MAPPINGS: Dict[str, Tuple[str, str]] = {
    # Consonants - Basic
    'ا': ('0627', 'ʔ/aː'),
    'ب': ('0628', 'b'),
    'ٻ': ('067B', 'ɓ'),
    'ڀ': ('0680', 'bʱ'),
    'ت': ('062A', 't'),
    'ٿ': ('067F', 'tʰ'),
    'ٽ': ('067D', 'ʈ'),
    'ٺ': ('067A', 'ʈʰ'),
    'پ': ('067E', 'p'),
    'ج': ('062C', 'd͡ʑ/ʥ'),
    'ڄ': ('0684', 'ʄ'),
    'ڃ': ('0683', 'ɲ'),
    'چ': ('0686', 't͡ɕ/ʨ'),
    'ڇ': ('0687', 't͡ɕʰ/ʨʰ'),
    'خ': ('062E', 'x'),
    'د': ('062F', 'd'),
    'ڌ': ('068C', 'dʱ'),
    'ڏ': ('068F', 'ɗ'),
    'ڊ': ('068A', 'ɖ'),
    'ڍ': ('068D', 'ɖʱ'),
    'ر': ('0631', 'r'),
    'ڙ': ('0699', 'ɽ'),
    'ز': ('0632', 'z'),
    'س': ('0633', 's'),
    'ش': ('0634', 'ʂ'),
    'غ': ('063A', 'ɣ'),
    'ف': ('0641', 'f'),
    'ڦ': ('06A6', 'pʰ'),
    'ق': ('0642', 'q'),
    'ڪ': ('06AA', 'k'),
    'ک': ('06A9', 'kʰ'),
    'گ': ('06AF', 'ɡ'),
    'ڳ': ('06B3', 'ɠ'),
    'ڱ': ('06B1', 'ŋ'),
    'ل': ('0644', 'l'),
    'م': ('0645', 'm'),
    'ن': ('0646', 'n/◌̃'),
    'ڻ': ('06BB', 'ɳ'),
    'و': ('0648', 'ʋ/ʊ/oː/ɔː/uː'),
    'ھ': ('06BE', 'h'),
    'ی': ('06CC', 'j/iː'),
    'ء': ('0621', 'ʔ'),
    
    # Loanword consonants (also represented by other letters)
    'ث': ('062B', 's'),
    'ح': ('062D', 'h'),
    'ذ': ('0630', 'z'),
    'ژ': ('0698', 'ʒ'),
    'ص': ('0635', 's'),
    'ض': ('0636', 'z'),
    'ط': ('0637', 't'),
    'ظ': ('0638', 'z'),
    'ع': ('0639', 'ɑː/oː/eː/ʔ'),
    
    # Heh variants
    'ه': ('0647', 'h'),
    'ہ': ('06C1', 'ə/əʰ'),
    
    # Digraphs - Aspirated consonants
    'جهہ': ('062C+0647+06C1', 'd͡ʑʰ/ʥʰ'),
    'گهہ': ('06AF+0647+06C1', 'ɡʱ'),
    'ڙهہ': ('0699+0647+06C1', 'ɽʰ'),
    'لهہ': ('0644+0647+06C1', 'lʱ'),
    'مهہ': ('0645+0647+06C1', 'mʰ'),
    'نهہ': ('0646+0647+06C1', 'nʰ'),
    'ڻهہ': ('06BB+0647+06C1', 'ɳʰ'),
    
    # Ligatures
    '۽': ('06FD', 'ãĩ̯'),
    '۾': ('06FE', 'mẽ'),
}

