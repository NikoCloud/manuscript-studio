#!/usr/bin/env python3
"""
style_extractor.py
Extract styling parameters from a source .docx file and apply them to an output .docx file.
Preserves original fonts, spacing, margins, and formatting from published books.

Usage:
    python3 style_extractor.py source.docx output.docx

Example:
    python3 style_extractor.py "D-Furious_original.docx" "D-Furious_formatted.docx"

This is used in PASS 4 (FORMATTING) for PUBLISHED BOOKS to maintain original design.
Extracts: fonts, paragraph spacing, margins, line spacing, indentation, heading styles.
"""

import zipfile
import os
import shutil
import sys
from pathlib import Path
import xml.etree.ElementTree as ET

def extract_and_apply_styles(source_docx, output_docx):
    """
    Extract styles from source .docx and apply to output .docx.

    Args:
        source_docx: Path to source .docx with original styling
        output_docx: Path to output .docx to receive styling
    """

    if not os.path.exists(source_docx):
        print(f"ERROR: Source file not found: {source_docx}")
        return False

    if not os.path.exists(output_docx):
        print(f"ERROR: Output file not found: {output_docx}")
        return False

    try:
        source_temp = "temp_source_styles"
        output_temp = "temp_output_styles"

        # Unpack both files
        with zipfile.ZipFile(source_docx, 'r') as z:
            z.extractall(source_temp)

        with zipfile.ZipFile(output_docx, 'r') as z:
            z.extractall(output_temp)

        # Extract styles.xml from source
        source_styles = os.path.join(source_temp, 'word', 'styles.xml')
        output_styles = os.path.join(output_temp, 'word', 'styles.xml')

        if os.path.exists(source_styles):
            # Parse source styles
            source_tree = ET.parse(source_styles)
            source_root = source_tree.getroot()

            # Parse output styles
            output_tree = ET.parse(output_styles)
            output_root = output_tree.getroot()

            # Define namespace
            ns = {
                'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main',
                'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'
            }

            # Register namespaces
            for prefix, uri in ns.items():
                ET.register_namespace(prefix, uri)

            # Copy docDefaults (default paragraph/character formatting)
            source_defaults = source_root.find('.//w:docDefaults', ns)
            output_defaults = output_root.find('.//w:docDefaults', ns)

            if source_defaults is not None and output_defaults is not None:
                output_root.remove(output_defaults)
                output_root.insert(0, source_defaults)
                print("✓ Applied default paragraph/character styles")

            # Copy style definitions (preserves heading styles, fonts, spacing)
            source_styles_elem = source_root.find('.//w:styles', ns)
            output_styles_elem = output_root.find('.//w:styles', ns)

            if source_styles_elem is not None and output_styles_elem is not None:
                # Get all style elements from source
                for style in source_root.findall('.//w:style', ns):
                    style_id = style.get('{' + ns['w'] + '}styleId')
                    # Check if this style exists in output
                    existing = output_root.find(f".//w:style[@w:styleId='{style_id}']", ns)
                    if existing is not None:
                        output_root.remove(existing)
                    output_root.append(style)

                print("✓ Applied style definitions (fonts, heading styles, paragraph formatting)")

            # Extract and apply document default properties
            source_sect = source_root.find('.//w:sectPr', ns)
            output_sect = output_root.find('.//w:sectPr', ns)

            if source_sect is not None:
                # Copy page size, margins from source
                for child in source_sect:
                    tag = child.tag.split('}')[-1] if '}' in child.tag else child.tag
                    if tag in ['pgSz', 'pgMar', 'pgBorders']:
                        existing = output_sect.find(child.tag)
                        if existing is not None:
                            output_sect.remove(existing)
                        output_sect.append(child)

                print("✓ Applied page size and margin settings")

            # Save updated styles.xml
            output_tree.write(output_styles, encoding='utf-8', xml_declaration=True)

        # Extract theme/colors from source (optional)
        source_theme = os.path.join(source_temp, 'word', 'theme', 'theme1.xml')
        output_theme = os.path.join(output_temp, 'word', 'theme', 'theme1.xml')

        if os.path.exists(source_theme):
            shutil.copy(source_theme, output_theme)
            print("✓ Applied color theme from source")

        # Repack output .docx
        with zipfile.ZipFile(output_docx, 'w', zipfile.ZIP_DEFLATED) as z:
            for root, dirs, files in os.walk(output_temp):
                for file in files:
                    filepath = os.path.join(root, file)
                    arcname = os.path.relpath(filepath, output_temp)
                    z.write(filepath, arcname)

        print(f"✓ Successfully applied source styling to: {output_docx}")

        # Cleanup
        shutil.rmtree(source_temp)
        shutil.rmtree(output_temp)

        return True

    except Exception as e:
        print(f"ERROR: {e}")
        # Cleanup on error
        if os.path.exists(source_temp):
            shutil.rmtree(source_temp)
        if os.path.exists(output_temp):
            shutil.rmtree(output_temp)
        return False

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 style_extractor.py source.docx output.docx")
        sys.exit(1)

    source = sys.argv[1]
    output = sys.argv[2]

    success = extract_and_apply_styles(source, output)
    sys.exit(0 if success else 1)
