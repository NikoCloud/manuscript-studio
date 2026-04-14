#!/usr/bin/env python3
"""
pr_dialect_validator.py
Validates that translated Spanish text uses authentic Puerto Rican dialect terms.
Designed for PASS 2 (TRANSLATION) to catch missed PR colloquialisms.

Usage:
    python3 pr_dialect_validator.py input.txt [--verbose]
    python3 pr_dialect_validator.py input.md [--verbose]

Example:
    python3 pr_dialect_validator.py sample_translation.txt --verbose

Returns:
    - List of PR dialect terms found (with frequency)
    - List of non-PR Spanish patterns detected (potential misses)
    - Confidence score
    - Specific line numbers for manual review
"""

import sys
import re
from pathlib import Path
from collections import defaultdict

# Authentic PR Spanish dialect terms (should appear in good translation)
PR_DIALECT_TERMS = {
    'pa\'': 'para (contraction)',
    'pal': 'para el (contraction)',
    'gomas': 'shoes/tires',
    'nevera': 'refrigerator',
    'zafacón': 'trash can',
    'escuela superior': 'high school',
    'chance': 'chance/perhaps',
    'mano': 'bro/dude (informal)',
    'chamaco': 'kid/young person',
    'coño': 'dammit (exclamation)',
    'carajo': 'damn (exclamation)',
    'brutal': 'awesome/cool',
    'vellonera': 'jukebox',
    'plátano': 'plantain',
    'guineo': 'banana',
    'alcapurria': 'fried pastry',
    'mofongo': 'mashed plantains',
    'culebra': 'snake (also swindler)',
    'guagua': 'bus',
    'carro': 'car',
    'máquina': 'car (slang)',
    'chévere': 'cool/great',
    'bacano': 'cool/great',
    'quilla': 'money',
    'chavos': 'money/change',
    'muela': 'lie/exaggeration',
    'tela': 'a lot',
    'un chin': 'a little',
    'cabrón': 'bastard/buddy (context dependent)',
    'pendejo': 'idiot (can be friendly)',
    'descocao': 'shameless/audacious',
    'mulatada': 'group of mulatos',
    'negrería': 'black pride',
    'vejigatorio': 'bothersome/irritating',
    'empanada': 'pastry',
    'pasteles': 'plantain pastries',
    'mondongo': 'tripe stew',
    'arroz con gandules': 'rice with pigeon peas',
    'sofrito': 'seasoning base',
    'culantrillo': 'cilantro/coriander',
    'recao': 'cilantro (variant)',
    'gandules': 'pigeon peas',
    'habichuelas': 'beans',
    'yuca': 'cassava',
    'malanga': 'taro root',
    'boniato': 'sweet potato',
    'majó': 'mashed (like majó de plátanos)',
}

# Non-PR patterns to flag (common mistakes from literal translation)
NON_PR_PATTERNS = {
    r'\brefresco\b': 'Should use brand name (Coca-Cola) not generic "refresco"',
    r'\bpañales\b': 'Should use "Pampers" (brand) not generic "pañales"',
    r'\bcoche\b': 'Spanish (Spain), use "carro" or "máquina" in PR',
    r'\baparcamiento\b': 'Spanish (Spain), use "estacionamiento" in PR',
    r'\bfregadero\b': 'Spanish (Spain), use "fregador" in PR',
    r'\bascensor\b': 'Spanish (Spain), use "elevador" in PR',
    r'\bvosotros\b': 'Castilian (Spain), use "ustedes" in PR',
    r'\bos\b\s': 'Castilian (Spain), use "los/les" in PR',
    r'\bdespacho\b': 'Castilian office term, use "oficina" in PR',
    r'\bcondón\b': 'Use "condón" is OK but "goma" is more PR colloquial',
    r'\bschooner\b': 'Use brand "Medalla" for beer, not generic term',
    r'\bpierna\b(?!\s+de)': 'In leg context: OK. But "muslo" is more PR for thigh',
    r'\bcompartir\bcoche': 'Spanish phrasing, "compartir guagua/carro" more PR',
}

def read_file(filepath):
    """Read input file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"ERROR: File not found: {filepath}")
        return None
    except Exception as e:
        print(f"ERROR: Could not read file: {e}")
        return None

def count_pr_terms(text):
    """Count occurrences of PR dialect terms."""
    found = defaultdict(int)
    lines_with_terms = defaultdict(list)

    for i, line in enumerate(text.split('\n'), 1):
        for term, meaning in PR_DIALECT_TERMS.items():
            # Case-insensitive, word-boundary matching
            pattern = r'\b' + re.escape(term) + r'\b'
            matches = re.findall(pattern, line, re.IGNORECASE)
            if matches:
                found[term] += len(matches)
                if len(lines_with_terms[term]) < 3:  # Store first 3 occurrences
                    lines_with_terms[term].append((i, line.strip()[:80]))

    return found, lines_with_terms

def find_non_pr_patterns(text):
    """Find non-PR Spanish patterns that suggest literal translation."""
    found = defaultdict(list)

    for i, line in enumerate(text.split('\n'), 1):
        for pattern, note in NON_PR_PATTERNS.items():
            matches = re.finditer(pattern, line, re.IGNORECASE)
            for match in matches:
                found[pattern].append({
                    'line': i,
                    'text': line.strip()[:80],
                    'note': note,
                    'match': match.group()
                })

    return found

def calculate_confidence(text, found_terms, non_pr_found):
    """
    Calculate confidence that this is authentic PR Spanish translation.
    0-100 scale. Higher = more confident this is good PR dialect.
    """
    word_count = len(text.split())

    # Baseline
    score = 50

    # Bonus for finding PR dialect terms (max +30)
    if found_terms:
        unique_terms = len(found_terms)
        term_density = sum(found_terms.values()) / max(word_count, 1000) * 1000
        score += min(30, unique_terms * 2 + term_density)

    # Penalty for non-PR patterns (max -30)
    if non_pr_found:
        non_pr_count = sum(len(v) for v in non_pr_found.values())
        score -= min(30, non_pr_count * 3)

    return max(0, min(100, score))

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 pr_dialect_validator.py input.txt [--verbose]")
        print("\nExample: python3 pr_dialect_validator.py sample.txt --verbose")
        sys.exit(1)

    filepath = sys.argv[1]
    verbose = '--verbose' in sys.argv

    text = read_file(filepath)
    if text is None:
        sys.exit(1)

    print(f"\n{'='*70}")
    print(f"PR DIALECT VALIDATOR - {Path(filepath).name}")
    print(f"{'='*70}\n")

    # Count PR dialect terms
    found_terms, lines_with_terms = count_pr_terms(text)

    # Find non-PR patterns
    non_pr_found = find_non_pr_patterns(text)

    # Calculate confidence
    confidence = calculate_confidence(text, found_terms, non_pr_found)

    # Report
    print(f"📊 RESULTS:")
    print(f"  Word count: {len(text.split())}")
    print(f"  Confidence: {confidence}/100 {'✓' if confidence >= 70 else '⚠'}\n")

    if found_terms:
        print(f"✓ PR DIALECT TERMS FOUND ({len(found_terms)} unique):")
        for term in sorted(found_terms.keys(), key=lambda x: found_terms[x], reverse=True):
            count = found_terms[term]
            meaning = PR_DIALECT_TERMS[term]
            print(f"  • {term:15} ({meaning:25}) — {count}x")
            if verbose and term in lines_with_terms:
                for line_no, line_text in lines_with_terms[term][:2]:
                    print(f"    Line {line_no}: {line_text}...")
    else:
        print("⚠ NO PR DIALECT TERMS FOUND")
        print("  This translation may be using neutral/Castilian Spanish instead of Puerto Rican.")

    if non_pr_found:
        print(f"\n⚠ NON-PR PATTERNS DETECTED ({sum(len(v) for v in non_pr_found.values())} total):")
        for pattern, matches in non_pr_found.items():
            print(f"\n  Pattern: {pattern}")
            for match_info in matches[:2]:  # Show first 2 occurrences
                print(f"    Line {match_info['line']}: Found '{match_info['match']}'")
                print(f"      → {match_info['note']}")
                print(f"      → Text: {match_info['text']}...")
    else:
        print("\n✓ No non-PR patterns detected.")

    print(f"\n{'='*70}")
    print(f"RECOMMENDATION:")
    if confidence >= 80:
        print("  ✓ Translation appears to use authentic PR Spanish dialect.")
    elif confidence >= 70:
        print("  ⚠ Translation is mostly good but may benefit from PR dialect review.")
    elif confidence >= 60:
        print("  ⚠ Translation could use more PR dialect terms and fewer Castilian patterns.")
    else:
        print("  ✗ Translation appears to use neutral/Castilian Spanish, not PR dialect.")
        print("    Consider PASS 3 focus on PR colloquialism integration.")
    print(f"{'='*70}\n")

    return 0 if confidence >= 70 else 1

if __name__ == "__main__":
    sys.exit(main())
