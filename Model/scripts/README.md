# Editorial Workflow Scripts

Automation tools for Liliz Black's 4-pass editorial workflow. These scripts reduce token usage and automate repetitive processing tasks.

## Scripts

### `image_extractor.py`
**Purpose:** Extract all images from a source .docx and inject them into an output .docx.

**Used in:** PASS 4 (FORMATTING) for PUBLISHED BOOKS only.

**Why:** Published books have finalized artwork that must be preserved. Rather than manually re-inserting images, this script automates extraction and re-embedding.

**Usage:**
```bash
python3 image_extractor.py source.docx output.docx
```

**Example:**
```bash
python3 image_extractor.py "D-Furious_original_EN.docx" "D-Furious_ES_v1_FORMATTING_2026-04-08.docx"
```

**What it does:**
- Unpacks both .docx files (which are ZIP archives)
- Copies all image files from source's `word/media/` folder to output's `word/media/`
- Updates image relationships in `word/_rels/document.xml.rels` to maintain integrity
- Repacks the output .docx with images embedded

**Output:** Modified output.docx with all images from source injected and properly linked.

---

### `style_extractor.py`
**Purpose:** Extract typography, spacing, and formatting from a source .docx and apply to an output .docx.

**Used in:** PASS 4 (FORMATTING) for PUBLISHED BOOKS only.

**Why:** Published books have established design parameters (fonts, margins, line spacing). This script preserves the author's original design rather than overriding with model templates.

**Usage:**
```bash
python3 style_extractor.py source.docx output.docx
```

**Example:**
```bash
python3 style_extractor.py "D-Furious_original_EN.docx" "D-Furious_ES_v1_FORMATTING_2026-04-08.docx"
```

**What it extracts & applies:**
- Font specifications (typeface, size, weight)
- Paragraph defaults (indentation, spacing, justification)
- Line spacing and first-line indent settings
- Heading styles (Heading 1, 2, 3, etc.)
- Page size and margin settings
- Color theme

**Output:** Modified output.docx with all original styling applied while preserving the markdown-converted content.

---

## Workflow Integration

### For NEW Books (from Model templates):
PASS 4 does NOT use these scripts. Instead, apply Model/ template styling (A TRAVÉS_ebook.docx parameters).

### For PUBLISHED Books (preserve original design):
1. Store original .docx in `source_reference/` folder
2. In PASS 4, after dialogue conversion and formatting:
   - Run `image_extractor.py` to recover images
   - Run `style_extractor.py` to recover typography & spacing
3. Output the combined result

---

## Token Cost Savings

These scripts save significant API costs by:
- Automating image/style extraction (would otherwise require manual re-work or model tokens)
- Running in local Python (0 API cost) instead of delegating to Claude
- For a 50K-word book with images, saves ~$5-15 in API costs per pass

---

## Error Handling

Both scripts:
- Check file existence before running
- Clean up temporary directories on error
- Print progress indicators (✓) for successful operations
- Print error messages with context
- Return exit code 0 (success) or 1 (failure)

---

## Notes

- Both scripts are idempotent (safe to run multiple times)
- Temp directories are auto-cleaned after execution
- Scripts use standard Python libraries only (no external dependencies)
- Compatible with Python 3.6+
