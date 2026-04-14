#!/usr/bin/env python3
"""
image_extractor.py
Extract all images from a source .docx file and inject them into an output .docx file.
Preserves original image relationships and maintains document integrity.

Usage:
    python3 image_extractor.py source.docx output.docx

Example:
    python3 image_extractor.py "D-Furious_original.docx" "D-Furious_formatted.docx"

This is used in PASS 4 (FORMATTING) for PUBLISHED BOOKS to preserve original artwork.
"""

import zipfile
import os
import shutil
import sys
from pathlib import Path
import xml.etree.ElementTree as ET

def extract_images(source_docx, output_docx):
    """
    Extract images from source .docx and inject them into output .docx.

    Args:
        source_docx: Path to source .docx file with original images
        output_docx: Path to output .docx file to receive images
    """

    if not os.path.exists(source_docx):
        print(f"ERROR: Source file not found: {source_docx}")
        return False

    if not os.path.exists(output_docx):
        print(f"ERROR: Output file not found: {output_docx}")
        return False

    try:
        # Create temp directories for unpacking
        source_temp = "temp_source_images"
        output_temp = "temp_output_images"

        # Unpack source .docx
        with zipfile.ZipFile(source_docx, 'r') as z:
            z.extractall(source_temp)

        # Unpack output .docx
        with zipfile.ZipFile(output_docx, 'r') as z:
            z.extractall(output_temp)

        # Copy media folder from source to output
        source_media = os.path.join(source_temp, 'word', 'media')
        output_media = os.path.join(output_temp, 'word', 'media')

        if os.path.exists(source_media):
            if os.path.exists(output_media):
                shutil.rmtree(output_media)
            shutil.copytree(source_media, output_media)
            print(f"✓ Copied image files from source media folder")
        else:
            print("  (No images found in source document)")

        # Copy document relationships (which reference the images)
        source_rels = os.path.join(source_temp, 'word', '_rels', 'document.xml.rels')
        output_rels = os.path.join(output_temp, 'word', '_rels', 'document.xml.rels')

        if os.path.exists(source_rels) and os.path.exists(output_rels):
            # Parse both relationship files
            source_tree = ET.parse(source_rels)
            output_tree = ET.parse(output_rels)

            source_root = source_tree.getroot()
            output_root = output_tree.getroot()

            # Extract image relationships from source
            ns = {'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'}
            source_image_rels = source_root.findall(".//r:Relationship[@Type='http://schemas.openxmlformats.org/officeDocument/2006/relationships/image']", ns)

            # Find highest existing rId in output
            max_rid = 0
            for rel in output_root.findall(".//r:Relationship", ns):
                rid = rel.get('Id', '')
                if rid.startswith('rId'):
                    try:
                        num = int(rid[3:])
                        max_rid = max(max_rid, num)
                    except ValueError:
                        pass

            # Copy image relationships with new IDs to avoid conflicts
            for i, rel in enumerate(source_image_rels, start=max_rid+1):
                new_rel = ET.Element('{http://schemas.openxmlformats.org/package/2006/relationships}Relationship')
                new_rel.set('Id', f'rId{i}')
                new_rel.set('Type', 'http://schemas.openxmlformats.org/officeDocument/2006/relationships/image')
                new_rel.set('Target', rel.get('Target', ''))
                output_root.append(new_rel)

            # Save updated relationships
            output_tree.write(output_rels, encoding='utf-8', xml_declaration=True)
            print(f"✓ Updated image relationships in output document")

        # Repack output .docx
        with zipfile.ZipFile(output_docx, 'w', zipfile.ZIP_DEFLATED) as z:
            for root, dirs, files in os.walk(output_temp):
                for file in files:
                    filepath = os.path.join(root, file)
                    arcname = os.path.relpath(filepath, output_temp)
                    z.write(filepath, arcname)

        print(f"✓ Successfully created output: {output_docx}")

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
        print("Usage: python3 image_extractor.py source.docx output.docx")
        sys.exit(1)

    source = sys.argv[1]
    output = sys.argv[2]

    success = extract_images(source, output)
    sys.exit(0 if success else 1)
