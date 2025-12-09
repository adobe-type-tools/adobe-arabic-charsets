# Adobe Arabic Character Sets - User Guide

**Last Updated:** 2025-10-22

## Quick Start

### I want to...

- **Design a font for Arabic** → Use [Character Set Files](#character-set-files-arabic-script)
- **Add romanization to my font** → Use [Romanization Files](#romanization-files-latin-script) + Adobe Latin 3
- **Look up how a character is romanized** → See [How to Look Up Romanization](#how-to-look-up-romanization)
- **Parse data programmatically** → See [Programmatic Access](#programmatic-access)
- **Verify against official standards** → See [arabic-roman-standards.md](arabic-roman-standards.md)

---

## Quick Reference

### Character Set Files (Arabic Script)

| File | Use For | Details |
|------|---------|---------|
| `adobe-arabic-1.txt` | Basic Arabic | [See README](../README.md#adobe-arabic-core-aar1) |
| `adobe-arabic-2.txt` | Urdu, Persian, Punjabi | [See README](../README.md#adobe-urdu--farsi--punjabi-module-aar2) |
| `adobe-arabic-3.txt` | Uyghur, Kazakh, Kyrgyz | [See README](../README.md#adobe-uyghur--kazakh--kyrgyz-module-aar3) |
| `adobe-arabic-4.txt` | Kashmiri, Saraiki, Balti | [See README](../README.md#adobe-kashmiri--saraiki--balti-module-aar4) |
| `adobe-arabic-5.txt` | Pashto, Sindhi, Kurdish, Balochi | [See README](../README.md#adobe-arabic-extended-module-aar5) |

### Romanization Files (Latin Script)

**Important:** All romanization modules require [Adobe Latin 3](https://adobe-type-tools.github.io/adobe-latin-charsets/adobe-latin-3.html)

| File | Use For | Details |
|------|---------|---------|
| `adobe-arabic-1-roman.txt` | Romanizing Arabic | [See README](../README.md#adobe-arabic-romanization-module-aar1raar1p) |
| `adobe-arabic-2-roman.txt` | Romanizing Urdu, Persian, Punjabi | [See README](../README.md#adobe-urdu--farsi--punjabi-romanization-module-aar2raar2p) |
| `adobe-arabic-3-roman.txt` | Romanizing Uyghur, Kazakh, Kyrgyz | [See README](../README.md#adobe-uyghur--kazakh--kyrgyz-romanization-module-aar3raar3p) |
| `adobe-arabic-4-roman.txt` | Romanizing Kashmiri, Saraiki, Balti | [See README](../README.md#adobe-kashmiri--saraiki--balti-romanization-module-aar4raar4p) |
| `adobe-arabic-5-roman.txt` | Romanizing extended languages | [See README](../README.md#adobe-arabic-extended-romanization-module-aar5raar5p) |

---

## How to Look Up Romanization

### "How is this Arabic character romanized?"

**Go to:** `documentation/arabic-roman-source.md`

This file contains tables showing how each character is romanized across different standards (BGN/PCGN, UNGEGN, ALA-LC, ISO, etc.)

**Example:**
- Looking for how ع (Ayn) is romanized in BGN/PCGN?
- Find the Arabic or Urdu table
- Look up Unicode `0639`
- Check the BGN/PCGN column

### Notation
- `b` = single romanization
- `k/g` = multiple options (context-dependent)
- `-` = not used in this standard

---

## Programmatic Access

### Parse Character Sets (Python)

```python
# Read character set files (tab-delimited)
with open('adobe-arabic-1.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()[1:]  # Skip header
    for line in lines:
        if line.strip() and not line.startswith('#'):
            unicode_code, char, glyph, name, notes = line.split('\t')
            print(f"{unicode_code}: {char} ({glyph})")
```

### Access Romanization Mappings (Python)

```python
# Load romanization mappings from standards_mappings/
import sys
sys.path.insert(0, '.')
from standards_mappings import get_standard_mappings, get_metadata

# Get mappings for a specific standard
mappings = get_standard_mappings('BGN/PCGN Urdu')
# Returns: {'0628': 'b', '067E': 'p', '062A': 't', ...}

# Get metadata
metadata = get_metadata('BGN/PCGN Urdu')
# Returns: {'standard_name': 'BGN/PCGN Urdu', 'table_type': 'urdu', ...}
```

---

## Common Standards

- **BGN/PCGN** - Geographic names (US/UK)
- **UNGEGN** - Geographic names (UN)
- **ALA-LC** - Library cataloging
- **ISO 233** - International standard
- **IPA** - Phonetic transcription

See `documentation/arabic-roman-standards.md` for complete list with official source URLs.

---

## Resources

- **[Interactive Browser](http://adobe-type-tools.github.io/adobe-arabic-charsets)** - Visual reference
- **[README.md](../README.md)** - Module descriptions and language support
- **[arabic-roman-source.md](arabic-roman-source.md)** - Romanization lookup tables
- **[arabic-roman-standards.md](arabic-roman-standards.md)** - Official standard documentation

---
