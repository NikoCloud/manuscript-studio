# Testing Guide for PASS 2 Validators

This guide walks you through testing the two new validation scripts on small samples before deploying to full manuscripts.

## Overview

Two new scripts for PASS 2 (TRANSLATION):
- **`pr_dialect_validator.py`** — Checks for authentic PR Spanish dialect terms
- **`brand_name_checker.py`** — Checks for authentic PR brand names (not generic terms)

Both scripts are designed to catch missed opportunities during translation, where a translator used neutral/Castilian Spanish or generic terms instead of PR-authentic language.

## Test Samples Included

- **`test_sample_good_pr.txt`** — Well-translated sample with good PR dialect & brands
- **`test_sample_generic_translation.txt`** — Poorly-translated sample with generic terms & Castilian Spanish

## How to Test

### 1. Test PR Dialect Validator (Good Sample)

```bash
cd Model/scripts/
python3 pr_dialect_validator.py test_sample_good_pr.txt --verbose
```

**Expected output:**
- Confidence: 80+ (good)
- Should find terms like: pa', pal, gomas, nevera, zafacón, escuela superior, chance, sofrito, recao, mofongo, habichuelas, yuca, quilla, Nintendo, YouTube, Nike, Medalla, Domino's, etc.
- No non-PR patterns detected
- Recommendation: "Translation appears to use authentic PR Spanish dialect"

### 2. Test PR Dialect Validator (Generic Sample)

```bash
python3 pr_dialect_validator.py test_sample_generic_translation.txt --verbose
```

**Expected output:**
- Confidence: 40-60 (poor)
- Should find very few PR dialect terms (maybe none)
- Should detect patterns like: "refresco", "pañales", "autobús" (Castilian), "refrigerador" (Castilian), "videoconsola" (Castilian), "zapatos" (generic, not "tenis"), "judías" (Castilian, not "habichuelas"), "situación económica" (generic, not "quilla")
- Recommendation: "Translation appears to use neutral/Castilian Spanish, not PR dialect"

### 3. Test Brand Name Checker (Good Sample)

```bash
python3 brand_name_checker.py test_sample_good_pr.txt --verbose
```

**Expected output:**
- Confidence: 85+ (excellent)
- Should find brands: Coca-Cola, Pampers, Nintendo, YouTube, Nike, Medalla, Domino's
- No generic terms flagged
- Recommendation: "Translation uses authentic PR brand-heavy voice"

### 4. Test Brand Name Checker (Generic Sample)

```bash
python3 brand_name_checker.py test_sample_generic_translation.txt --verbose
```

**Expected output:**
- Confidence: 30-50 (poor)
- Should find NO authentic brands
- Should flag generic terms like: "refresco" → Use "Coca-Cola"
- Should flag: "pañales desechables" → Use "Pampers"
- Should flag: "comida rápida" → Use specific brand (McDonald's/Burger King)
- Should flag: "bebida fría" → Use specific brand (Medalla)
- Recommendation: "Translation uses too many generic terms"

## Interpretation Guide

### Confidence Scores

**PR Dialect Validator:**
- 80+: Good authentic PR Spanish ✓
- 70-79: Mostly good, minor improvements possible
- 60-69: Could use more PR dialect
- Below 60: Too much neutral/Castilian Spanish

**Brand Name Checker:**
- 80+: Good brand-authentic ✓
- 70-79: Mostly good, minor brand improvements
- 60-69: Several generic terms that should be brands
- Below 60: Too generic, not PR-authentic

## What to Look For

### Good Signs (Good PR Translation):
- Finds multiple different PR dialect terms (pa', pal, gomas, nevera, zafacón, etc.)
- Finds authentic brands (Coca-Cola, Pampers, Nike, Netflix, etc.)
- No Castilian patterns (Spanish Spain terms like "autobús", "refrigerador", "ascensor")
- Conversational, natural-sounding Spanish

### Red Flags (Generic/Castilian Translation):
- Generic terms instead of brands: "refresco" instead of "Coca-Cola"
- Castilian Spanish: "autobús" (Spain) instead of "guagua" (PR)
- Generic Spanish: "refrigerador" instead of "nevera"
- No PR-specific slang/colloquialisms
- Formal/neutral tone instead of colloquial PR voice

## Next Steps

Once you've tested on these samples and confirmed the scripts work as expected:

1. **Apply to PASS 2 output:** Run both scripts on actual translated manuscript excerpts
2. **Tweak thresholds if needed:** If scripts are too strict/lenient, we can adjust confidence calculations
3. **Deploy for full manuscripts:** Use on complete translations before moving to PASS 3

## Sample Output (Good Translation)

```
======================================================================
PR DIALECT VALIDATOR - test_sample_good_pr.txt
======================================================================

📊 RESULTS:
  Word count: 245
  Confidence: 85/100 ✓

✓ PR DIALECT TERMS FOUND (16 unique):
  • pa'              (para (contraction)        ) — 2x
  • pal              (para el (contraction)    ) — 1x
  • gomas            (shoes/tires               ) — 1x
  • nevera           (refrigerator              ) — 1x
  • zafacón          (trash can                 ) — 1x
  • escuela superior (high school               ) — 0x
  • chance           (chance/perhaps            ) — 0x
  • mano             (bro/dude (informal)       ) — 1x
  • sofrito          (seasoning base            ) — 1x
  • recao            (cilantro (variant)        ) — 1x
  • mofongo          (mashed plantains          ) — 1x
  • habichuelas      (beans                     ) — 1x
  • yuca             (cassava                   ) — 1x
  • quilla           (money                     ) — 1x
  • guagua           (bus                       ) — 1x
  • chavos           (money/change              ) — 1x

✓ No non-PR patterns detected.

======================================================================
RECOMMENDATION:
  ✓ Translation appears to use authentic PR Spanish dialect.
======================================================================
```

## Sample Output (Generic Translation)

```
======================================================================
BRAND NAME VALIDATOR - test_sample_generic_translation.txt
======================================================================

📊 RESULTS:
  Word count: 210
  Confidence: 35/100 ⚠

⚠ NO AUTHENTIC BRANDS FOUND
  Translation may not use PR brand-heavy voice.

⚠ GENERIC TERMS THAT SHOULD BE BRANDS (5 total):

  Line 1: Found 'refresco'
    → Suggestion: Use 'Coca-Cola' instead
    → Reason: Use brand name, not "refresco"
    → Context: María abrió un refresco y se dejó caer...

  Line 2: Found 'pañales'
    → Suggestion: Use 'Pampers' instead
    → Reason: Use brand name, not generic "pañales"
    → Context: Su hija estaba usando pañales desechables...

  Line 9: Found 'comida rápida'
    → Suggestion: Use 'McDonald\'s/Burger King' instead
    → Reason: Use specific brand
    → Context: los abuelos vienen en un autobús... Trae el dinero para comprar comida rápida.

  ... and 2 more

======================================================================
RECOMMENDATION:
  ✗ Translation uses too many generic terms.
    Consider PASS 3 focus on replacing generics with specific brands.
======================================================================
```

---

## Feedback & Iteration

After testing:
1. Do the scripts catch what you expect?
2. Are there false positives/negatives?
3. Should we add more PR dialect terms or brands?
4. Do confidence thresholds feel right?

Let me know what adjustments are needed!
