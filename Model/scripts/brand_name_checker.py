#!/usr/bin/env python3
"""
brand_name_checker.py
Validates that translated Spanish text uses authentic PR brand names and cultural references.
Designed for PASS 2 (TRANSLATION) to enforce Liliz's brand-heavy Puerto Rican dialect.

Usage:
    python3 brand_name_checker.py input.txt [--verbose]
    python3 brand_name_checker.py input.md [--verbose]

Example:
    python3 brand_name_checker.py sample_translation.txt --verbose

Returns:
    - List of authentic brands found (with frequency)
    - List of generic terms that should be brand names (potential misses)
    - Confidence score
    - Specific line numbers for manual review

Note: Puerto Rican Spanish is highly brand-heavy. Use specific brand names rather than
generic terms. This reflects authentic PR voice (people say "dame una Coca-Cola" not
"dame un refresco").
"""

import sys
import re
from pathlib import Path
from collections import defaultdict

# Authentic PR brands and cultural references (should be in good translation)
AUTHENTIC_BRANDS = {
    'Coca-Cola': 'soft drink (iconic PR brand)',
    'Medalla': 'beer (Puerto Rican)',
    'Pampers': 'diapers (brand, not "pañales")',
    'Netflix': 'streaming (use brand name)',
    'Spotify': 'music streaming',
    'Instagram': 'social media',
    'WhatsApp': 'messaging app',
    'TikTok': 'social media',
    'YouTube': 'video platform',
    'Google': 'search engine',
    'Uber': 'ride-sharing',
    'Airbnb': 'accommodation sharing',
    'Amazon': 'e-commerce',
    'PlayStation': 'gaming console',
    'Xbox': 'gaming console',
    'Nintendo': 'gaming',
    'iPhone': 'phone (Apple)',
    'Samsung': 'electronics',
    'Nissan': 'car brand',
    'Honda': 'car brand',
    'Toyota': 'car brand',
    'Ford': 'car brand',
    'Chevrolet': 'car brand',
    'Harley-Davidson': 'motorcycle',
    'Ferrari': 'luxury car',
    'Mercedes-Benz': 'luxury car',
    'BMW': 'luxury car',
    'Chevrolet': 'car',
    'Dyson': 'vacuum',
    'Ninja': 'blender',
    'KitchenAid': 'mixer',
    'Cuisinart': 'appliances',
    'Nikon': 'camera',
    'Canon': 'camera',
    'Sony': 'electronics',
    'Panasonic': 'electronics',
    'LG': 'electronics',
    'Samsung': 'electronics',
    'Adidas': 'sports brand',
    'Nike': 'sports brand',
    'Puma': 'sports brand',
    'New Balance': 'shoes',
    'Reebok': 'shoes/sports',
    'Converse': 'shoes',
    'Vans': 'shoes',
    'Tommy Hilfiger': 'clothing',
    'Ralph Lauren': 'clothing',
    'Calvin Klein': 'clothing',
    'Levi\'s': 'jeans',
    'Gap': 'clothing',
    'H&M': 'clothing',
    'Zara': 'clothing',
    'Gucci': 'luxury brand',
    'Prada': 'luxury brand',
    'Louis Vuitton': 'luxury brand',
    'McDonald\'s': 'fast food',
    'Burger King': 'fast food',
    'Wendy\'s': 'fast food',
    'KFC': 'fast food',
    'Pizza Hut': 'pizza chain',
    'Domino\'s': 'pizza chain',
    'Starbucks': 'coffee',
    'Dunkin\'': 'coffee/donuts',
    'Taco Bell': 'fast food',
    'Popeyes': 'fast food (fried chicken)',
    'Chick-fil-A': 'fast food',
    'Chipotle': 'fast casual',
    'Panera': 'bakery/cafe',
    'Olive Garden': 'Italian restaurant',
    'Red Lobster': 'seafood',
    'Applebee\'s': 'casual dining',
    'Chili\'s': 'casual dining',
    'TGI Friday\'s': 'bar & grill',
    'Cheesecake Factory': 'restaurant',
    'Outback Steakhouse': 'steakhouse',
    'Ruth\'s Chris': 'steakhouse',
}

# Generic terms that should probably be brand names
GENERIC_TERMS_TO_FLAG = {
    r'\brefresco\b': ('Coca-Cola', 'Use brand name, not "refresco"'),
    r'\bpañales\b': ('Pampers', 'Use brand name, not generic "pañales"'),
    r'\bconservante\b': ('Pampers/Huggies', 'Usually a brand in context'),
    r'\bplatforma\s+de\s+streaming': ('Netflix/Amazon Prime', 'Use specific brand'),
    r'\bservicio\s+de\s+videos': ('Netflix/YouTube', 'Use specific brand'),
    r'\bservicios\s+de\s+música': ('Spotify/Apple Music', 'Use specific brand'),
    r'\bred\s+social': ('Instagram/TikTok/Twitter', 'Use specific brand'),
    r'\bmensajería\b': ('WhatsApp/Telegram', 'Use specific brand'),
    r'\btaxi\b': ('Uber/Lyft', 'Use specific brand in modern context'),
    r'\bcoche\s+de\s+alquiler': ('Uber/Lyft', 'Use specific brand'),
    r'\bvideojuego': ('PlayStation/Xbox/Nintendo', 'Specify console'),
    r'\bconsolа\s+de\s+juegos': ('PlayStation/Xbox/Nintendo', 'Specify brand'),
    r'\bteléfono\s+inteligente': ('iPhone/Samsung/Pixel', 'Use specific brand'),
    r'\bteléfono\s+móvil': ('iPhone/Samsung', 'Use specific brand'),
    r'\bcámara\s+digital': ('Nikon/Canon/Sony', 'Use specific brand'),
    r'\bzapatillas\b': ('Nike/Adidas', 'Use specific brand'),
    r'\bropa\s+deportiva': ('Nike/Adidas/Puma', 'Use specific brand'),
    r'\bcomida\s+rápida': ('McDonald\'s/Burger King', 'Use specific brand'),
    r'\bcafé': ('Starbucks/Dunkin\'', 'Use specific brand if applicable'),
    r'\bcerveza\b': ('Medalla/Corona', 'Use specific brand in PR context'),
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

def count_authentic_brands(text):
    """Count occurrences of authentic brand names."""
    found = defaultdict(int)
    lines_with_brands = defaultdict(list)

    for i, line in enumerate(text.split('\n'), 1):
        for brand in AUTHENTIC_BRANDS.keys():
            # Case-insensitive matching
            pattern = r'\b' + re.escape(brand) + r'\b'
            matches = re.findall(pattern, line, re.IGNORECASE)
            if matches:
                found[brand] += len(matches)
                if len(lines_with_brands[brand]) < 2:  # Store first 2 occurrences
                    lines_with_brands[brand].append((i, line.strip()[:80]))

    return found, lines_with_brands

def find_generic_terms(text):
    """Find generic terms that should probably be brand names."""
    found = []

    for i, line in enumerate(text.split('\n'), 1):
        for pattern, (suggestion, note) in GENERIC_TERMS_TO_FLAG.items():
            matches = re.finditer(pattern, line, re.IGNORECASE)
            for match in matches:
                found.append({
                    'line': i,
                    'text': line.strip()[:80],
                    'match': match.group(),
                    'suggestion': suggestion,
                    'note': note
                })

    return found

def calculate_confidence(text, found_brands, generic_found):
    """
    Calculate confidence that this translation uses authentic PR brands.
    0-100 scale. Higher = more brand-authentic.
    """
    word_count = len(text.split())

    # Baseline
    score = 50

    # Bonus for authentic brands (max +40)
    if found_brands:
        unique_brands = len(found_brands)
        brand_count = sum(found_brands.values())
        score += min(40, unique_brands * 3 + brand_count)

    # Penalty for generic terms (max -30)
    if generic_found:
        score -= min(30, len(generic_found) * 2)

    return max(0, min(100, score))

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 brand_name_checker.py input.txt [--verbose]")
        print("\nExample: python3 brand_name_checker.py sample.txt --verbose")
        sys.exit(1)

    filepath = sys.argv[1]
    verbose = '--verbose' in sys.argv

    text = read_file(filepath)
    if text is None:
        sys.exit(1)

    print(f"\n{'='*70}")
    print(f"BRAND NAME VALIDATOR - {Path(filepath).name}")
    print(f"{'='*70}\n")

    # Count authentic brands
    found_brands, lines_with_brands = count_authentic_brands(text)

    # Find generic terms that should be brands
    generic_found = find_generic_terms(text)

    # Calculate confidence
    confidence = calculate_confidence(text, found_brands, generic_found)

    # Report
    print(f"📊 RESULTS:")
    print(f"  Word count: {len(text.split())}")
    print(f"  Confidence: {confidence}/100 {'✓' if confidence >= 70 else '⚠'}\n")

    if found_brands:
        print(f"✓ AUTHENTIC BRANDS FOUND ({len(found_brands)} unique):")
        for brand in sorted(found_brands.keys(), key=lambda x: found_brands[x], reverse=True):
            count = found_brands[brand]
            meaning = AUTHENTIC_BRANDS[brand]
            print(f"  • {brand:20} ({meaning:30}) — {count}x")
            if verbose and brand in lines_with_brands:
                for line_no, line_text in lines_with_brands[brand]:
                    print(f"    Line {line_no}: {line_text}...")
    else:
        print("⚠ NO AUTHENTIC BRANDS FOUND")
        print("  Translation may not use PR brand-heavy voice.")

    if generic_found:
        print(f"\n⚠ GENERIC TERMS THAT SHOULD BE BRANDS ({len(generic_found)} total):")
        for item in generic_found[:10]:  # Show first 10
            print(f"\n  Line {item['line']}: Found '{item['match']}'")
            print(f"    → Suggestion: Use '{item['suggestion']}' instead")
            print(f"    → Reason: {item['note']}")
            print(f"    → Context: {item['text']}...")
        if len(generic_found) > 10:
            print(f"\n  ... and {len(generic_found) - 10} more")
    else:
        print("\n✓ No obvious generic terms found. Good brand usage!")

    print(f"\n{'='*70}")
    print(f"RECOMMENDATION:")
    if confidence >= 80:
        print("  ✓ Translation uses authentic PR brand-heavy voice.")
    elif confidence >= 70:
        print("  ⚠ Translation is good but could use more brand authenticity.")
    elif confidence >= 60:
        print("  ⚠ Translation could benefit from more brand-specific language.")
    else:
        print("  ✗ Translation uses too many generic terms.")
        print("    Consider PASS 3 focus on replacing generics with specific brands.")
    print(f"{'='*70}\n")

    return 0 if confidence >= 70 else 1

if __name__ == "__main__":
    sys.exit(main())
