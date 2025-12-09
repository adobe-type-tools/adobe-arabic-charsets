# Arabic Transliteration Standards Reference

**Version:** 1.1.0  
**Last updated: 2025-10-22**

> **MASTER REFERENCE**: Authoritative URLs for all standards. Referenced by `arabic-roman-source.md` for romanization data tables.
>
> **System Status**: ✅ Complete - 1529/1529 mappings verified (100%) across 45+ integrated standards
> **Implementation**: Python mapping files in `standards_mappings/` (auto-discovered)

## Arabic International Standards

### BGN/PCGN:1956 (Board on Geographic Names/Permanent Committee on Geographical Names)
- **Reference**: https://assets.publishing.service.gov.uk/media/637df1aae90e076b73e074c7/ROMANIZATION_OF_ARABIC_-_Nov_22.pdf
- **Usage**: Geographic names, official mapping
- **Status**: ✅ Integrated (48 mappings)

### UNGEGN: 1972 (United Nations Group of Experts on Geographical Names)
- **Reference**: https://unstats.un.org/unsd/geoinfo/ungegn/docs/pubs/UNGEGN%20tech%20ref%20manual_m87_combined.pdf
- **Usage**: International geographic standardization
- **Status**: ✅ Integrated (32 mappings)

### UNGEGN 5.0, 2018
- **Reference**: https://unstats.un.org/unsd/ungegn/working_groups/wg5/documents/wgrr5arabic.pdf
- **Usage**: Updated international standard
- **Status**: ℹ️ Combined with UNGEGN 1972

### ALA-LC, 2012 (American Library Association-Library of Congress)
- **Reference**: http://www.loc.gov/catdir/cpso/romanization/arabic.pdf
- **Usage**: Library cataloging, academic references
- **Status**: ✅ Integrated (58 mappings)

### DIN 31635 (Deutsches Institut für Normung)
- **Reference**: https://transliteration.eki.ee/pdf/Arabic_2.2.pdf
- **Usage**: German academic and library systems
- **Status**: ✅ Integrated (51 mappings)

## Arabic Academic Systems

### Brill Simple Arabic Transliteration System 1.0, 2010
- **Reference**: https://brill.com/fileasset/downloads_static/static_fonts_simple_arabic_transliteration.pdf
- **Usage**: Encyclopaedia of Islam, Brill academic publications
- **Status**: ✅ Integrated (34 mappings)
- **Note**: Simple 1:1 system (one Arabic letter → one roman letter). Taa marbuta (ة) context-dependent: a, ah, āh, at, āt

### DMG (Deutsche Morgenländische Gesellschaft)
- **Reference**: https://dmg-web.de/en/publications/transliteration-of-the-arabic-script/
- **Usage**: German Oriental studies standard; adopted by Hans Wehr Dictionary (German edition, 1952)
- **Status**: ✅ Integrated (46 mappings)
- **Note**: Academic precision system for reversible transliteration. Identical to Hans Wehr German edition (1952). Uses diacritics (ḥ, ḫ, ṭ, ẓ, ġ, š, ǧ, ṯ, ḏ) and special symbols (ʿ, ʾ). Aims for language-neutral, one-to-one correspondence.

### Wehr/Cowan (English Hans Wehr) - 1961
- **Reference**: https://archive.org/details/dictionaryofmode0000wehr_t0g4
- **Published**: Wehr, Hans. _A Dictionary of Modern Written Arabic_ (Arabic-English), 4th edition, ed. J. Milton Cowan (Ithaca, N.Y.: Spoken Language Services, 1994)
- **Usage**: English edition of Hans Wehr Dictionary for anglophone readers
- **Based on**: DMG system, adapted by Cowan for English readability
- **Key Differences from DMG**: Anglicized digraphs (š→sh, ǧ→j, ḫ→kh, ġ→gh, ṯ→th, ḏ→dh)
- **Status**: ✅ Integrated (42 mappings)
- **Note**: Prioritizes pronunciation accessibility over reversibility.

### ISO 233-2 Arabic Simplified
- **Reference**: https://cdn.standards.iteh.ai/samples/4118/2f03c828842c4055a5619c1bded39381/ISO-233-2-1993.pdf
- **Usage**: Simplified international standard for bibliographic use
- **Status**: ✅ Integrated (42 mappings)
- **Note**: Simplifies ISO 233:1984 for ease of typing and bibliographic processing.

### Encyclopedia of Islam Arabic (EI3/EWIC/EQ)
- **Reference**: https://brill.com/fileasset/downloads_products/27684_EI3-Instructions-for-Authors.pdf
- **Usage**: Islamic studies reference works
- **Status**: ✅ Integrated (31 mappings)
- **Note**: Standard transliteration covering Arabic, Persian, Urdu, Hindi, and Punjabi

## Phonetic Representation Systems

### Arabic IPA (OSU Egyptian Arabic)
- **Reference**: https://ielp.ehe.osu.edu/files/2025/09/IPA_Eg_Arabic.pdf
- **Usage**: Phonetic representation for Egyptian Arabic
- **Status**: ✅ Integrated (32 mappings)
- **Note**: Includes pharyngealized consonants and allophonic variations

### Arabic IPA (University of Michigan)
- **Reference**: https://sites.lsa.umich.edu/jalt/ipa-symbols/
- **Usage**: General Arabic IPA correspondences
- **Status**: ✅ Integrated (32 mappings)
- **Note**: Based on Journal of Arabic Linguistics Tradition

### Arabic IPA (Wikipedia)
- **Reference**: https://en.wikipedia.org/wiki/Help%3AIPA/Arabic
- **Usage**: Classical Modern Standard Arabic IPA
- **Status**: ✅ Integrated (38 mappings)
- **Note**: Based on Ladefoged & Maddieson, Thelwall & Sa'adeddin, Mitchell, Kaye, Al-Ani

## Persian/Farsi Standards

### ISO 233-3 Persian
- **Reference**: https://cdn.standards.iteh.ai/samples/78514/749948ae77474f7fa057a6b278281dbb/ISO-233-3-2023.pdf
- **Usage**: International technical documentation for Persian
- **Status**: ✅ Integrated (36 mappings)
- **Note**: Strict transliteration with Persian-specific characters (پ چ ژ گ)

### UNGEGN Persian (2012)
- **Reference**: https://unstats.un.org/unsd/ungegn/working_groups/wg5/documents/wgrr4persian.pdf
- **Usage**: UN approved system for geographical names
- **Status**: ✅ Integrated (38 mappings)
- **Note**: Broad transcription based on pronunciation

### BGN/PCGN Persian (1958, updated 2019)
- **Reference**: https://assets.publishing.service.gov.uk/media/5e1eeaafe5274a4f0f57553a/ROMANIZATION_OF_PERSIAN.pdf
- **Usage**: US/UK geographic names standardization
- **Adopted**: BGN 1946, PCGN 1958, updated 2019
- **Status**: ✅ Integrated (38 mappings)

### ALA-LC Persian
- **Reference**: https://www.loc.gov/catdir/cpso/romanization/persian.pdf
- **Usage**: Library cataloging, academic references
- **Status**: ✅ Integrated (32 mappings)

### Encyclopedia of Islam Persian (EI3/EWIC/EQ)
- **Reference**: https://brill.com/fileasset/downloads_products/27684_EI3-Instructions-for-Authors.pdf
- **Usage**: Islamic studies reference works
- **Status**: ✅ Integrated (36 mappings)
- **Note**: Same as EI3 Arabic with Persian-specific characters (پ چ ژ گ)

### Persian IPA (OSU)
- **Reference**: https://ielp.ehe.osu.edu/files/2025/09/IPA_Persian.pdf
- **Usage**: Phonetic representation for Persian
- **Status**: ✅ Integrated (30 mappings)

## Urdu Standards

### ALA-LC Urdu
- **Reference**: https://loc.gov/catdir/cpso/roman_urdu_pushto_sindhi.html
- **Usage**: Library cataloging, academic references
- **Status**: ✅ Integrated (53 mappings)

### UNGEGN Urdu (1972, amended 1977)
- **Reference**: https://unstats.un.org/unsd/ungegn/working_groups/wg5/documents/wgrr4urdu.pdf
- **Usage**: UN approved system for geographical names
- **Status**: ✅ Integrated (41 mappings)
- **Note**: Based on Hunterian transliteration system (Government of India official standard developed by William Wilson Hunter, 19th century, based on William Jones 1746-1794). Features aspirated consonants (bh, th), retroflex with dots (ṭ, ḍ), schwa deletion, long vowels (ā, ī, ū)

### BGN/PCGN Urdu (2018)
- **Reference**: https://assets.publishing.service.gov.uk/media/5ab4e64d40f0b67d64e21540/ROMANIZATION_OF_URDU.pdf
- **Usage**: US/UK geographic names standardization
- **Status**: ✅ Integrated (62 mappings)

### Encyclopedia of Islam Urdu/Punjabi (EI3/EWIC/EQ)
- **Reference**: https://brill.com/fileasset/downloads_products/27684_EI3-Instructions-for-Authors.pdf
- **Usage**: Islamic studies reference works
- **Status**: ✅ Integrated (51 mappings)
- **Note**: Same as EI3 Arabic with Urdu-specific characters (ٹ ڈ ڑ ے)

### Urdu IPA (CLE)
- **Reference**: https://www.cle.org.pk/Downloads/langproc/Urdu_IPA_to_Sampa.pdf
- **Usage**: Phonetic representation for Urdu
- **Status**: ✅ Integrated (70 mappings)

### Urdu IPA (Wikipedia)
- **Reference**: https://en.wikipedia.org/wiki/Help:IPA/Hindi_and_Urdu
- **Usage**: Phonetic representation for Urdu
- **Status**: ✅ Integrated (59 mappings)

## Punjabi Standards

### UNGEGN Punjabi
- **Reference**: https://unstats.un.org/unsd/ungegn/working_groups/wg5/documents/wgrr4punjabi.pdf
- **Usage**: UN approved system for geographical names
- **Status**: ✅ Integrated (38 mappings)

### Encyclopedia of Islam Punjabi (EI3/EWIC/EQ)
- **Reference**: https://brill.com/fileasset/downloads_products/27684_EI3-Instructions-for-Authors.pdf
- **Usage**: Islamic studies reference works
- **Status**: ✅ Integrated (51 mappings, shared with Urdu)
- **Note**: Uses same character set as EI3 Urdu/Hindi

### Punjabi IPA (Wikipedia)
- **Reference**: https://en.wikipedia.org/wiki/Help:IPA/Punjabi
- **Usage**: Phonetic representation for Punjabi
- **Status**: ✅ Integrated (56 mappings)

## Uyghur/Kazakh/Kyrgyz Standards

### BGN/PCGN Kazakh, 2019
- **Reference**: https://assets.publishing.service.gov.uk/media/621caa32e90e0710b73fd4ff/ROMANIZATION_KAZAKH_Feb_22_19_.pdf
- **Usage**: US/UK geographic names standardization
- **Status**: 📋 Not integrated (Cyrillic only)
- **Note**: Covers Cyrillic script, not Arabic script

### BGN/PCGN Kyrgyz, 2019
- **Reference**: https://assets.publishing.service.gov.uk/media/621caa11e90e0710c30a4706/ROMANIZATION_KYRGYZ_Feb22_9_.pdf
- **Usage**: US/UK geographic names standardization
- **Status**: 📋 Not integrated (Cyrillic only)
- **Note**: Covers Cyrillic script, not Arabic script

### Kazakh Official Latin Alphabet, 2021
- **Reference**: https://astanatimes.com/2021/02/kazakhstan-presents-new-latin-alphabet-plans-gradual-transition-through-2031/
- **Usage**: Official government Latin alphabet
- **Adoption**: April 2021, transition through 2031
- **Status**: 📋 Not integrated (Latin alphabet, not romanization)
- **Note**: 31 letters with diacritics (ä, ö, ü, ğ, ū, ş, ñ); based on Common Turkic Alphabet. Kazakhstan transitioning from Cyrillic to Latin script, abandoning historical Arabic script.

### BGN/PCGN Uyghur, 2024
- **Reference**: https://assets.publishing.service.gov.uk/media/65f317e99d99de001d03df0c/Uyghur_romanization.pdf
- **Usage**: US/UK geographic names standardization for Uyghur Arabic script
- **Status**: ✅ Integrated (40 mappings)

### Kazakh IPA (Wikipedia)
- **Reference**: https://en.wikipedia.org/wiki/Kazakh_alphabets
- **Usage**: IPA for Kazakh Arabic script
- **Status**: ✅ Integrated (33 mappings)
- **Note**: Historical correspondence between Arabic script and Latin alphabet with 35 Arabic script characters

### Kyrgyz IPA (Wikipedia)
- **Reference**: https://en.wikipedia.org/wiki/Kyrgyz_alphabets
- **Usage**: IPA for Kyrgyz Arabic script
- **Status**: ✅ Integrated (32 mappings)
- **Note**: Historical correspondence; 35 Arabic script characters with IPA mappings. Kyrgyz: 36 phonemes (14 vowels, 22 consonants)

### Uyghur IPA (Wikipedia)
- **Reference**: https://en.wikipedia.org/wiki/Uyghur_language
- **Usage**: IPA for Uyghur Arabic script
- **Status**: ✅ Integrated (33 mappings)

## Ottoman Turkish Standards

### ALA-LC Ottoman Turkish
- **Reference**: https://www.loc.gov/catdir/cpso/romanization/ottoman.pdf
- **Usage**: Library cataloging for Ottoman Turkish texts
- **Status**: ✅ Integrated (49 mappings)
- **Note**: Ottoman Turkish used Arabic script 1299-1928. Vowel diacritics deferred to Arabic/Persian tables per ALA-LC guidelines.

### DMG Turkish (Deutsche Morgenländische Gesellschaft)
- **Reference**: DMG transliteration guidelines
- **Usage**: German academic and library systems
- **Status**: ✅ Integrated (49 mappings)

### Encyclopedia of Islam Ottoman Turkish (EI3)
- **Reference**: https://brill.com/fileasset/downloads_products/27684_EI3-Instructions-for-Authors.pdf
- **Usage**: Islamic studies reference works
- **Status**: ✅ Integrated (49 mappings)

## Extended Arabic Script Standards

### Pashto Standards

#### ALA-LC Pashto
- **Reference**: https://loc.gov/catdir/cpso/romanization/pushto.pdf
- **Usage**: Library cataloging, academic references
- **Status**: ✅ Integrated (51 mappings)

#### BGN/PCGN Pashto, 1968
- **Reference**: https://assets.publishing.service.gov.uk/media/5ab4e57ee5274a1aa5933455/ROMANIZATION_OF_PASHTO.pdf
- **Usage**: US/UK geographic names standardization
- **Status**: 📋 Not integrated (ALA-LC + DIN Pashto provide coverage)

#### Pashto IPA (Wikipedia)
- **Reference**: https://en.wikipedia.org/wiki/Pashto_phonology
- **Usage**: IPA for Pashto
- **Status**: ✅ Integrated

### Kashmiri Standards

#### ALA-LC Kashmiri
- **Reference**: https://loc.gov/catdir/cpso/romanization/kashmiri.pdf
- **Usage**: Library cataloging, academic references
- **Status**: ✅ Integrated (70 mappings)

#### Kashmiri IPA (Wikipedia)
- **Reference**: https://en.wikipedia.org/wiki/Kashmiri_language#Perso-Arabic_script
- **Usage**: IPA for Kashmiri
- **Status**: ✅ Integrated (44 mappings)

### Kurdish (Sorani) Standards

#### ALA-LC Kurdish (Sorani)
- **Reference**: https://loc.gov/catdir/cpso/romanization/kurdish.pdf
- **Usage**: Library cataloging, academic references
- **Status**: ✅ Integrated (47 mappings)

#### Kurdish IPA (Wikipedia)
- **Reference**: https://en.wikipedia.org/wiki/Help:IPA/Kurdish
- **Usage**: IPA for Kurdish
- **Status**: ✅ Integrated

### Sindhi Standards

#### ALA-LC Sindhi
- **Reference**: https://loc.gov/catdir/cpso/romanization/sindhi.pdf
- **Usage**: Library cataloging, academic references
- **Status**: ✅ Integrated (49 mappings)

#### Sindhi IPA (SLA)
- **Reference**: https://learn.sindhila.edu.pk/alphabets/ipl
- **Usage**: IPA for Sindhi
- **Status**: ✅ Integrated

### Balochi Standards

#### BGN/PCGN Baluchi, 2008
- **Reference**: https://assets.publishing.service.gov.uk/media/5ab4de6ce5274a1aa593343b/ROMANIZATION_OF_BALUCHI.pdf
- **Usage**: US/UK geographic names standardization for Balochi (Eastern, Western, Southern dialects)
- **Status**: ✅ Integrated (68 mappings)
- **Note**: Based on Hunterian transliteration system (Government of India official standard); harmonized with BGN/PCGN Urdu and Persian systems

#### Balochi IPA (Wikipedia)
- **Reference**: https://en.wikipedia.org/wiki/Balochi_alphabets
- **Usage**: IPA for Balochi
- **Status**: ✅ Integrated

#### Balochi Academy Sarbaz (BAS)
- **Reference**: http://www.balochiacademy.ir/en/2022/07/01/balochi-standard-alphabets/
- **Authority**: Balochi Academy Sarbaz
- **Published**: July 2017 (accepted by BAS activists)
- **Usage**: Official Balochi standardization with diacritic-based romanization system
- **Status**: ✅ Integrated (32 mappings)
- **Note**: IPA notation set by Salim Balòc Kòhgardi. Uses diacritics: à, è, ò, š, ť, ž, ď

### Saraiki Standards

#### Saraiki IPA (Wikipedia)
- **Reference**: https://en.wikipedia.org/wiki/Saraiki_alphabet
- **Usage**: IPA for Saraiki
- **Status**: ✅ Integrated

### Balti Standards

#### Balti IPA (Wikipedia)
- **Reference**: https://en.wikipedia.org/wiki/Balti_language#Perso-Arabic_alphabet
- **Usage**: IPA for Balti Perso-Arabic alphabet
- **Status**: ✅ Integrated (45 mappings)
- **Note**: Tibetic language with unique characters including U+0768 (ݨ), U+0769 (ݩ), U+0697 (ڗ), U+075C (ݜ)

---

## Research & Undocumented Standards

### Historical & Undocumented Systems

| System | Reference | Notes |
|--------|-----------|-------|
| **Bedirxan Kurdish** | [Wikipedia](https://en.wikipedia.org/wiki/Bedirxan_script) | Historical romanization (1930s); not actively used |
| **Balti** | N/A | No widely recognized romanization standard |

---

## Arabic Standards Not Pursued

The following standards were researched but are not recommended for implementation. Source: Library and Archives Canada Inventory of Romanization Tools (2019).

| Standard | Year | Status | Reason Not Pursued | Research Date |
|----------|------|--------|-------------------|---------------|
| **ISO 233:1984** | 1984 | 📋 Not Pursued | ISO 233-2 (1993) simplified version provides equivalent coverage with easier typing | N/A |
| **BS 4280:1968** | 1968 | 🔴 Rejected | No free documentation; requires purchase (£50-200); 56 years old, likely superseded by ISO/BGN/PCGN; UK now uses BGN/PCGN or ALA-LC | 2024-10-10 |
| **I.G.N. System 1973** | 1973 | 🔴 Rejected | Documentation unavailable online; would require contacting IGN France; very niche (French geographic names); UNGEGN (Variant A) provides adequate coverage | 2024-10-10 |
| **Lebanon National** | 1963 | 📋 Not Prioritized | Country-specific; likely superseded by international standards; documentation difficult to obtain | N/A |
| **Morocco National** | 1932 | 📋 Not Prioritized | Very old (92 years); country-specific; historical interest only; documentation unavailable | N/A |
| **RJGC (Jordan)** | Unknown | 📋 Not Prioritized | Country-specific; specialized (geographic names only); limited practical use outside Jordan | N/A |
| **Survey of Egypt** | Unknown | 📋 Not Prioritized | Country-specific; specialized (cartographic); limited practical application | N/A |

**Note on I.G.N. System 1973**: This is "Variant B of the Amended Beirut System" (UNGEGN 2018 is "Variant A"). Main difference: Variant B conforms to French orthography and is preferred in Francophone countries (Morocco, Algeria, Tunisia, Lebanon).

---

## Legacy Text Mapping Files

The following text files contain extracted mappings from standards documents and are preserved for reference:

| File | Description |
|------|-------------|
| `documentation/iso2333_mappings.txt` | ISO 233-3 (2023) Persian mappings |
| `documentation/ei3_mappings.txt` | Encyclopedia of Islam mappings |
| `documentation/arabic-roman-mappings.txt` | General Arabic romanization mappings |

**Note:** All active standards have been migrated to `standards_mappings/*.py` for auto-discovery and validation.

---
