# Adobe Arabic Character Sets

### Notice

These character sets are informative, not normative. They are guidelines.
We reserve the right to update, modify, replace or withdraw them at any time without prior notice.

---

# [Adobe Arabic Character Sets](http://adobe-type-tools.github.io/adobe-arabic-charsets)

In general, these are character sets and not glyph sets, although some character variants are documented to indicate basic language support. At this time, positional forms (initial, medial, final, isolated) are not captured by these character sets.

## Character Set Architecture

Adobe Arabic script and romanization character sets feature a parallel modular structure:

- **Core** — Arabic script foundation / romanization extends Adobe Latin 3
- **Urdu + Farsi + Punjabi** — extends Core
- **Kashmiri + Saraiki + Balti** — extends Core + Urdu + Farsi + Punjabi (Nastaliq script style)
- **Uyghur + Kazakh + Kyrgyz** — extends Core
- **Extended** — extends Core + Urdu + Farsi + Punjabi (Naskh script style)

---

## [Adobe Arabic Core](index.html#arabic-core) (AAR1)

The Adobe Arabic Core character set forms the foundation for Perso-Arabic script support. It contains 101 single characters (99 Unicode characters + 2 alternate glyphs) and 21 character combinations considered required for Arabic text. It is intended to be a minimal set and, as such, only supports the Arabic language.

Languages supported by Adobe Arabic Core: [Arabic](https://en.wikipedia.org/wiki/Arabic_language).

## [Adobe Urdu + Farsi + Punjabi Module](index.html#adobe-urdu-farsi-punjabi) (AAR2)

This module adds 37 characters (35 unique characters + 2 alternate glyphs) which, in conjunction with the Adobe Arabic Core character set, provide full support for Urdu, Farsi (Persian) and Punjabi (Shahmukhi).

Languages supported by Adobe Arabic Core + Adobe Urdu + Farsi + Punjabi Module: [Urdu](https://en.wikipedia.org/wiki/Urdu), [Persian (Farsi & Dari)](https://en.wikipedia.org/wiki/Persian_language), [Punjabi (Shahmukhi)](https://en.wikipedia.org/wiki/Shahmukhi_alphabet), and [Azerbaijani (South Azerbaijani)](https://en.wikipedia.org/wiki/Azerbaijani_language#South_Azerbaijani).

## [Adobe Uyghur + Kazakh + Kyrgyz Module](index.html#uyghur-kazakh-kyrgyz-module) (AAR3)

This module adds 22 characters which, in conjunction with the Adobe Arabic Core character set, provide full support for Arabic orthographies of Uyghur, Kazakh, and Kyrgyz as used in China. This covers the Arabic script requirements portion of China's GB 18030 character standard.

Languages supported by Adobe Arabic Core + Adobe Uyghur + Kazakh + Kyrgyz Module: [Uyghur](https://en.wikipedia.org/wiki/Uyghur_Arabic_alphabet), [Kazakh (Arabic script)](https://en.wikipedia.org/wiki/Kazakh_alphabets#Arabic_script) and [Kyrgyz (Arabic script)](https://en.wikipedia.org/wiki/Kyrgyz_alphabet#Arabic_script).

## [Adobe Kashmiri + Saraiki + Balti Module](index.html#kashmiri-saraiki-balti) (AAR4)

This module comprises 43 characters which, in conjunction with the Adobe Arabic Core character set *and* the Adobe Urdu + Farsi + Punjabi Module, provide full support for Nastaliq-style languages: Kashmiri, Saraiki, and Balti.

Languages supported by Adobe Arabic Core + Adobe Urdu + Farsi + Punjabi Module + Adobe Kashmiri + Saraiki + Balti Module: [Kashmiri](https://en.wikipedia.org/wiki/Kashmiri_language), [Saraiki](https://en.wikipedia.org/wiki/Saraiki_language), [Balti](https://en.wikipedia.org/wiki/Balti_language).

## [Adobe Arabic Extended Module](index.html#arabic-extended-module) (AAR5)

This module comprises 43 characters which, in conjunction with the Adobe Arabic Core character set *and* the Adobe Urdu + Farsi + Punjabi Module, provide full support for the target languages: Pashto, Sindhi, Kurdish (Sorani), Balochi, and Malay (Jawi script).

Languages supported by Adobe Arabic Core + Adobe Urdu + Farsi + Punjabi Module + Adobe Arabic Extended Module: [Pashto](https://en.wikipedia.org/wiki/Pashto_alphabet) (~50M), [Sindhi](https://en.wikipedia.org/wiki/Sindhi_language) (~20M), [Kurdish (Sorani)](https://en.wikipedia.org/wiki/Sorani_alphabet) (~8M), [Balochi](https://en.wikipedia.org/wiki/Balochi_language) (~8M), [Malay (Jawi script)](https://en.wikipedia.org/wiki/Jawi_alphabet) (~3-8M).

---

## Romanization Modules

The Arabic romanization modules extend [Adobe Latin 3](https://adobe-type-tools.github.io/adobe-latin-charsets/adobe-latin-3.html) with Latin characters for transcribing Arabic-script text. Each module contains two types of characters:

- **Romanization characters** support major romanization standards (BGN/PCGN, UNGEGN, ALA-LC, DIN, ISO, DMG, &c).
- **IPA characters (optional)** provide International Phonetic Alphabet symbols for phonetic transcription and detailed linguistic analysis.

Both character types are combined in each module to avoid unnecessarily multiplying the number of modules.

## [Adobe Arabic Romanization Module](index.html#arabic-core-romanization) (AAR1R+AAR1P)

This module adds **69 new Latin characters** (33 essential + 36 optional IPA) on top of [Adobe Latin 3](https://adobe-type-tools.github.io/adobe-latin-charsets/adobe-latin-3.html) for romanizing Arabic script text.

**Supported Standards**: [BGN/PCGN](https://en.wikipedia.org/wiki/BGN/PCGN_romanization), [UNGEGN](https://en.wikipedia.org/wiki/UNGEGN), [ALA-LC](https://en.wikipedia.org/wiki/ALA-LC_romanization), [DIN 31635](https://en.wikipedia.org/wiki/DIN_31635), [ISO 233-2](https://en.wikipedia.org/wiki/ISO_233-2), [DMG](https://en.wikipedia.org/wiki/Deutsche_Morgenl%C3%A4ndische_Gesellschaft), [Hans Wehr](https://en.wikipedia.org/wiki/Hans_Wehr), [Brill Simple Arabic](https://referenceworks.brillonline.com/entries/encyclopaedia-of-islam-3/*-COM_23875), [Encyclopedia of Islam (EI3)](https://referenceworks.brillonline.com/entries/encyclopaedia-of-islam-3/*-COM_23875), [Arabic IPA](https://en.wikipedia.org/wiki/International_Phonetic_Alphabet) ([multiple sources](documentation/arabic-roman-standards.md#phonetic-representation-systems)).

Languages supported by Adobe Arabic Romanization Module: [Arabic](https://en.wikipedia.org/wiki/Arabic_language).

## [Adobe Urdu + Farsi + Punjabi Romanization Module](index.html#urdu-farsi-punjabi-romanization) (AAR2R+AAR2P)

This module adds **66 new characters** (40 essential + 26 optional IPA) on top of the [Adobe Arabic Romanization Module](index.html#arabic-core-romanization) and [Adobe Latin 3](https://adobe-type-tools.github.io/adobe-latin-charsets/adobe-latin-3.html) for romanizing Urdu, Farsi (Persian), and Punjabi script text.

**Supported Standards**: 
- **Persian**: [ISO 233-3](https://en.wikipedia.org/wiki/ISO_233-3), [UNGEGN Persian](https://en.wikipedia.org/wiki/UNGEGN), [BGN/PCGN Persian](https://en.wikipedia.org/wiki/BGN/PCGN_romanization), [ALA-LC Persian](https://en.wikipedia.org/wiki/ALA-LC_romanization), [Encyclopedia of Islam (EI3)](https://referenceworks.brillonline.com/entries/encyclopaedia-of-islam-3/*-COM_23875), [Persian IPA](https://en.wikipedia.org/wiki/International_Phonetic_Alphabet) ([OSU](documentation/arabic-roman-standards.md#persian-ipa-osu))
- **Urdu**: [BGN/PCGN Urdu](https://en.wikipedia.org/wiki/BGN/PCGN_romanization), [ALA-LC Urdu](https://en.wikipedia.org/wiki/ALA-LC_romanization), [UNGEGN Urdu](https://en.wikipedia.org/wiki/UNGEGN), [Encyclopedia of Islam (EI3)](https://referenceworks.brillonline.com/entries/encyclopaedia-of-islam-3/*-COM_23875), [Urdu IPA](https://en.wikipedia.org/wiki/International_Phonetic_Alphabet) ([CLE, Wikipedia](documentation/arabic-roman-standards.md#urdu-standards))
- **Punjabi**: [UNGEGN Punjabi](https://en.wikipedia.org/wiki/UNGEGN), [Encyclopedia of Islam (EI3)](https://referenceworks.brillonline.com/entries/encyclopaedia-of-islam-3/*-COM_23875), [Punjabi IPA](https://en.wikipedia.org/wiki/International_Phonetic_Alphabet) ([Wikipedia](documentation/arabic-roman-standards.md#punjabi-standards))

Languages supported by Adobe Arabic Romanization Module + Adobe Urdu + Farsi + Punjabi Romanization Module: [Urdu](https://en.wikipedia.org/wiki/Urdu), [Persian (Farsi & Dari)](https://en.wikipedia.org/wiki/Persian_language), [Punjabi (Shahmukhi)](https://en.wikipedia.org/wiki/Shahmukhi_alphabet), and [Azerbaijani (South Azerbaijani)](https://en.wikipedia.org/wiki/Azerbaijani_language#South_Azerbaijani).

## [Adobe Uyghur + Kazakh + Kyrgyz Romanization Module](index.html#uyghur-kazakh-kyrgyz-romanization) (AAR3R+AAR3P)

This module adds **14 new IPA characters** on top of the [Adobe Arabic Romanization Module](index.html#arabic-core-romanization) and [Adobe Latin 3](https://adobe-type-tools.github.io/adobe-latin-charsets/adobe-latin-3.html) for romanizing Uyghur, Kazakh, and Kyrgyz script text. The basic Latin alphabet needed by these languages is already provided by AL3.

**Supported Standards**: 
- **Uyghur**: [BGN/PCGN Uyghur](https://en.wikipedia.org/wiki/BGN/PCGN_romanization), [Uyghur IPA](https://en.wikipedia.org/wiki/International_Phonetic_Alphabet) ([Wikipedia](documentation/arabic-roman-standards.md#uyghur-ipa-wikipedia))
- **Kazakh**: [Kazakh IPA](https://en.wikipedia.org/wiki/International_Phonetic_Alphabet) ([Wikipedia](documentation/arabic-roman-standards.md#kazakh-ipa-wikipedia))
- **Kyrgyz**: [Kyrgyz IPA](https://en.wikipedia.org/wiki/International_Phonetic_Alphabet) ([Wikipedia](documentation/arabic-roman-standards.md#kyrgyz-ipa-wikipedia))

Languages supported by Adobe Arabic Romanization Module + Adobe Uyghur + Kazakh + Kyrgyz Romanization Module: [Uyghur](https://en.wikipedia.org/wiki/Uyghur_Arabic_alphabet), [Kazakh (Arabic script)](https://en.wikipedia.org/wiki/Kazakh_alphabets#Arabic_script) and [Kyrgyz (Arabic script)](https://en.wikipedia.org/wiki/Kyrgyz_alphabet#Arabic_script).

## [Adobe Kashmiri + Saraiki + Balti Romanization Module](index.html#kashmiri-saraiki-balti-romanization) (AAR4R+AAR4P)

This module adds **32 new characters** (20 exclusive + 12 overlapping with Extended) on top of [Adobe Latin 3](https://adobe-type-tools.github.io/adobe-latin-charsets/adobe-latin-3.html), the [Adobe Arabic Romanization Module](index.html#arabic-core-romanization), and the [Adobe Urdu + Farsi + Punjabi Romanization Module](index.html#urdu-farsi-punjabi-romanization) for romanizing Kashmiri, Saraiki, and Balti script text.

**Supported Standards**: [ALA-LC Kashmiri](https://en.wikipedia.org/wiki/ALA-LC_romanization), [Kashmiri IPA](https://en.wikipedia.org/wiki/International_Phonetic_Alphabet), [Saraiki IPA](https://en.wikipedia.org/wiki/International_Phonetic_Alphabet), [Balti IPA](https://en.wikipedia.org/wiki/International_Phonetic_Alphabet).

Languages supported by Adobe Arabic Romanization Module + Adobe Urdu + Farsi + Punjabi Romanization Module + Adobe Kashmiri + Saraiki + Balti Romanization Module: [Kashmiri](https://en.wikipedia.org/wiki/Kashmiri_language), [Saraiki](https://en.wikipedia.org/wiki/Saraiki_language), [Balti](https://en.wikipedia.org/wiki/Balti_language).

## [Adobe Arabic Extended Romanization Module](index.html#arabic-extended-romanization) (AAR5R+AAR5P)

This module adds **57 new characters** (45 exclusive + 12 overlapping with Nastaliq) on top of the [Adobe Arabic Romanization Module](index.html#arabic-core-romanization), the [Adobe Urdu + Farsi + Punjabi Romanization Module](index.html#urdu-farsi-punjabi-romanization), and [Adobe Latin 3](https://adobe-type-tools.github.io/adobe-latin-charsets/adobe-latin-3.html) for romanizing Pashto, Sindhi, Kurdish, and Balochi script text.

**Supported Standards**: [ALA-LC](https://en.wikipedia.org/wiki/ALA-LC_romanization), [Extended Arabic IPA](https://en.wikipedia.org/wiki/International_Phonetic_Alphabet), and [language-specific systems](documentation/arabic-roman-standards.md#extended-arabic-script-standards) for [Pashto](https://en.wikipedia.org/wiki/Pashto_alphabet), [Sindhi](https://en.wikipedia.org/wiki/Sindhi_language), [Kurdish](https://en.wikipedia.org/wiki/Sorani_alphabet), [Balochi](https://en.wikipedia.org/wiki/Balochi_language).

Languages supported by Adobe Arabic Romanization Module + Adobe Urdu + Farsi + Punjabi Romanization Module + Adobe Arabic Extended Romanization Module: [Pashto](https://en.wikipedia.org/wiki/Pashto_alphabet), [Sindhi](https://en.wikipedia.org/wiki/Sindhi_language), [Kurdish (Sorani)](https://en.wikipedia.org/wiki/Sorani_alphabet), [Balochi](https://en.wikipedia.org/wiki/Balochi_language), [Malay (Jawi script)](https://en.wikipedia.org/wiki/Jawi_alphabet).

---

## Documentation & Resources

- **[User Guide](documentation/USER_GUIDE.md)** - How to use the character sets programmatically
- **[Romanization Tables](documentation/arabic-roman-source.md)** - Lookup tables for romanization mappings
- **[Standards Reference](documentation/arabic-roman-standards.md)** - Complete library of romanization standards