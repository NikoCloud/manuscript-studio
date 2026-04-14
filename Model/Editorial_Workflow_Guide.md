# Liliz Black Editorial Workflow Guide

**Version:** 1.0  
**Last Updated:** 2026-04-07  
**Maintained by:** Niko & Liliz Black Editorial System

---

## FOLDER STRUCTURE & FLOW

All work happens in your Google Drive shared folder. Four input folders represent the state machine; files move through them as passes complete.

```
Project_Root/
│
├─ Model/
│  ├─ Editorial_Workflow_Guide.md          (THIS DOCUMENT)
│  ├─ Formatting_Templates/                (ePub styles, fonts, etc.)
│  └─ Reference_Examples/                  (Sample edits, previous approved passes)
│
├─ 1 To review/
│  └─ [Liliz places manuscripts here for STRUCTURAL pass]
│  └─ [AGENT PROCESSES ONLY FILES IN THIS FOLDER FOR PASS 1]
│
├─ 2 To translate/
│  └─ [Author moves original here after STRUCTURAL pass approved]
│  └─ [AGENT PROCESSES ONLY FILES IN THIS FOLDER FOR PASS 2]
│
├─ 3 To language/
│  └─ [Author moves original here after TRANSLATION pass approved]
│  └─ [AGENT PROCESSES ONLY FILES IN THIS FOLDER FOR PASS 3]
│
├─ 4 To format/
│  └─ [Author moves original here after LANGUAGE pass approved]
│  └─ [AGENT PROCESSES ONLY FILES IN THIS FOLDER FOR PASS 4]
│
├─ output/
│  ├─ EN/
│  │  └─ 2026-04-07/
│  │     ├─ [Title]_EN_v2_STRUCTURAL_2026-04-07.md
│  │     ├─ [Title]_EN_v2_TRANSLATION_2026-04-07.md
│  │     ├─ [Title]_EN_v2_LANGUAGE_2026-04-07.md
│  │     └─ [Title]_EN_v2_FORMATTING_2026-04-07.md
│  │
│  └─ ES/
│     └─ 2026-04-07/
│        ├─ [Title]_ES_v2_STRUCTURAL_2026-04-07.md
│        ├─ [Title]_ES_v2_TRANSLATION_2026-04-07.md
│        ├─ [Title]_ES_v2_LANGUAGE_2026-04-07.md
│        └─ [Title]_ES_v2_FORMATTING_2026-04-07.md
│
├─ Approved/
│  ├─ EN/
│  │  └─ [Title]_EN_v2_FINAL.md            (Ready for ePub conversion)
│  │
│  └─ ES/
│     └─ [Title]_ES_v2_FINAL.md            (Ready for ePub conversion)
│
└─ Editorial_Log.md
   (Master log: all decisions, version history, author notes)
```

**Key Points:**
- `1 To review/` → STRUCTURAL pass (plot, pacing, character consistency)
- `2 To translate/` → TRANSLATION pass (EN→ES or ES→EN full conversion)
- `3 To language/` → LANGUAGE pass (grammar, punctuation, dialect polish)
- `4 To format/` → FORMATTING pass (dialogue conversion, styling, ePub prep)
- `output/` is where all four-pass results go (organized by language and date)
- `Model/` is reference only—agent reads, never writes
- `Approved/` is where Liliz moves finalized manuscripts after all passes complete

**State Machine Logic:**
A file's location tells you exactly which pass it needs. Author moves the original file to the next folder after reviewing the previous pass output.

---

## INTAKE DECISIONS (Two Questions)

**Critical first steps:** On initial intake, ask TWO questions that control the entire workflow:

1. **Book Status:** Published or new?
2. **Series Status:** Standalone or part of a series?

---

### Decision 1: BOOK STATUS

**Question: Is this book already published (in any language)?**

**IF YES → Published Book Workflow:**
- **Typical scenario:** Already published in English; needs translation (EN→ES) + language polish + formatting
- **Example:** D-Furious Book 1 (published EN, translated to ES)
- **Which passes to run?** Depends on what needs revision:
  - If only translating: SKIP PASS 1, run PASS 2, PASS 3, PASS 4
  - If retranslating existing version: Start at PASS 2
  - If copy-editing existing version: SKIP PASS 2, run PASS 3, PASS 4
- **Source file handling:** Store original .docx in `source_reference/` folder (preserved for PASS 4)
- **PASS 4 styling:** Extract styles + images from source file, NOT from Model/ templates
- **Why?** Published books have finalized design; we preserve original branding/layout

**IF NO → New Manuscript Workflow:**
- **Typical scenario:** Unpublished manuscript in any language; may go through all 4 passes or skip translation
- **Which passes to run?** Depends on language:
  - Already in target language (e.g., native PR Spanish): SKIP PASS 2, run PASS 1→3→4
  - Needs translation (e.g., English draft to Spanish): Run all PASS 1→2→3→4
- **Source file handling:** Can discard after PASS 1 (not needed for later passes)
- **PASS 4 styling:** Apply Model/ template styling (A TRAVÉS_ebook.docx parameters)
- **Why?** New books adopt Liliz's standard formatting for consistency

### Implementation

**On first message with a new manuscript, ask:**
> "Is this an already-published book being revised/retranslated, or a new unpublished manuscript?"

**Based on author's response:**
1. Update Editorial Log with Book Status (Published / New)
2. Determine which passes to run
3. If Published: Create `source_reference/` subfolder, preserve original .docx
4. If New: Standard workflow, discard source after PASS 1
5. In PASS 4: Select styling procedure based on status

---

### Decision 2: SERIES STATUS

**Question: Is this a standalone story, or part of a series? If series, which book?**

**Options:**
- Standalone (complete story, no sequels planned)
- Book 1 of [N] (first in series, sequels planned)
- Book [X] of [N] (middle book, preceded and followed by others)
- Book N (final book, concludes series)
- Other (spin-off, prequel, etc.)

**Why this matters:**
This determines how PASS 1 evaluates plot threads, character arcs, and story resolution. A loose thread in Book 1 might be intentional setup for Book 2. A loose thread in the final book is a critical error.

**On first message, ask:**
> "Is this a standalone story, or part of a series? If series, which book (1 of 3, 2 of 5, etc.)?"

**Based on author's response:**
1. Update Editorial Log with Series Status
2. Inform PASS 1 how to prioritize loose threads (see PASS 1 procedure below)
3. Standalone = all threads critical
4. Book 1 = cliffhangers expected, flag but not critical
5. Book N (middle/final) = resolve internal arc, may reference prior books

---

## FILE NAMING CONVENTION

**INPUT FILE NAMING:**
```
[BookTitle]_[LANG].[format]
```

Examples:
- `The_Shadow_Game_EN.md`
- `El_Juego_de_Sombras_ES.md`
- `The_Shadow_Game_EN.docx`

**LANGUAGE CODES:**
- `EN` = English (American)
- `ES` = Spanish (Puerto Rican)

**OUTPUT FILE NAMING (after each pass):**
```
[BookTitle]_[LANG]_v[VERSION]_[PASS]_[DATE].md
```

**Components:**
- `[BookTitle]` = Exact same as input filename (preserves author naming)
- `[LANG]` = EN or ES
- `v[VERSION]` = Version number (increments from previous; if input is `v1`, your output is `v1` or `v2` depending on whether this is the first pass)
- `[PASS]` = STRUCTURAL, LANGUAGE, or FORMATTING
- `[DATE]` = YYYY-MM-DD

**Examples:**
- `The_Shadow_Game_EN_v2_STRUCTURAL_2026-04-07.md`
- `El_Juego_de_Sombras_ES_v1_LANGUAGE_2026-04-07.md`
- `The_Shadow_Game_EN_v2_FORMATTING_2026-04-07.md`

**VERSION NUMBERING:**
- First processing cycle = v1
- If author revises and re-submits = v2
- If a pass is redone = same version number, new date

---

## LANGUAGE-SPECIFIC FORMATTING REFERENCE

### Critical: English vs. Spanish Prose Structure

Spanish and English have fundamentally different dialogue and prose conventions. This is **NOT optional styling**—it's required formatting for each language. The FORMATTING pass MUST convert between these structures.

#### DIALOGUE FORMATTING

**English (American):**
```
"Hello," said Maria. "And how are you?"

"I'm fine," she replied, "thanks for asking."

"That's wonderful," he said.
```

**Spanish (Puerto Rican):**
```
—Hola —dijo María— y cómo estás?

—Estoy bien —respondió ella— gracias por preguntar.

—Qué maravilloso —dijo él.
```

**Key Differences:**

| Element | English | Spanish |
|---------|---------|---------|
| Dialogue opener | Double quote `"` | Em-dash `—` |
| Dialogue closer | Double quote `"` | Em-dash `—` (or none at end of paragraph) |
| Dialogue tag | Comma before tag: `"Hello," said Maria.` | Em-dash surrounds tag: `—Hola —dijo María—` |
| Interruption/continuation | New quote: `"Hello," said Maria. "And how..."` | Em-dash: `—Hola —dijo María— y cómo...` (continuous, no quote restart) |
| End of dialogue block | Closing quote + punctuation | Em-dash + punctuation or just em-dash |
| Multiple speakers in scene | Each gets opening/closing quotes | Each line starts with em-dash; no closing until paragraph ends |

**Examples - Exact Conversion:**

English:
```
"Where are you going?" asked Marcus.

"To the market," replied Dev. "I need supplies."

"I'll come with you," he offered.
```

Spanish equivalent:
```
—¿A dónde vas? —preguntó Marcus.

—Al mercado —respondió Dev—. Necesito provisiones.

—Te acompaño —ofreció él.
```

**Critical Rules for Spanish Dialogue:**

1. **Opening em-dash:** Every dialogue line starts with `—`
2. **Dialogue tags in the middle:** Surrounded by em-dashes, no quotes
   - `—Hola —dijo María—`
   - `—y cómo estás? —preguntó Juan.`
3. **Dialogue that continues after a tag:** No new opening dash/quote; continues on same line
   - `—Hola —dijo María— y cómo estás?` ✓
   - NOT: `—Hola —dijo María— "y cómo estás?"` ✗
4. **Paragraph breaks:** If a character's dialogue spans multiple paragraphs, each new paragraph starts with `—`
5. **Punctuation before em-dash:** Period, comma, question mark, exclamation point goes BEFORE the closing em-dash when needed
   - `—¿Cómo estás? —preguntó ella.`

#### PROSE PARAGRAPH FORMATTING

**English:**
- Standard indentation (0.5" or tab) at paragraph start
- Single space between paragraphs (optional, style-dependent)
- Narrative prose flows normally

**Spanish:**
- Can use same indentation
- em-dashes at start of dialogue change visual rhythm
- Prose structure is same, but dialogue changes appearance significantly

#### ACTION/NARRATIVE BLOCKS

**English:**
```
Maria walked to the window. "I can't stay," she said quietly.

"Then go," replied Dev without looking up.
```

**Spanish:**
```
María caminó hacia la ventana. —No puedo quedarme —dijo en voz baja.

—Entonces vete —respondió Dev sin mirar hacia arriba.
```

**Note:** Narrative prose is identical; only dialogue formatting changes.

---

## FORMATTING PASS: DIALOGUE CONVERSION CHECKLIST

When processing manuscripts in the FORMATTING pass, **dialogue conversion is a primary task**, not a detail. Use this checklist:

**For English → Spanish (if translating):**
- [ ] Every dialogue line has opening `—`
- [ ] Dialogue tags are surrounded by `—` with no quotes
- [ ] Dialogue continuing after a tag uses no new opening quote/dash
- [ ] Punctuation (?, !, .) goes before closing `—` when needed
- [ ] Multi-paragraph dialogue: each para starts with `—`
- [ ] No English double quotes remain in Spanish dialogue
- [ ] Test: Read dialogue aloud—does it follow Spanish speech patterns?

**For Spanish dialogue preservation (if native Spanish manuscript):**
- [ ] Dialogue formatting matches Puerto Rican Spanish conventions
- [ ] No accidental mix of English quotes and Spanish dashes
- [ ] Consistency: if one block uses `—`, all do
- [ ] Punctuation alignment verified

**For English manuscript (preserve English formatting):**
- [ ] All dialogue uses double quotes `"`
- [ ] Dialogue tags: comma before tag `"Hello," said Maria.`
- [ ] No em-dashes in dialogue (only in thoughts/internal, if author uses them)
- [ ] Consistency across all dialogue blocks

---

Each manuscript goes through THREE sequential passes. Each pass is independent and produces a separate output file.

### PASS 1: STRUCTURAL

**Goal:** Identify plot holes, pacing issues, character consistency, and story arc problems. **Flag everything, but prioritize based on series status.**

**Critical Context:** Know the series status before evaluating. A loose thread in Book 1 might be intentional; in the final book, it's a critical error.

**Focus Areas:**
- Plot logic and coherence (do events follow logically?)
- Character consistency (do characters act in character across the manuscript?)
- Pacing (are there drastic changes? Do slow sections drag? Does action feel rushed?)
- Loose threads (are all plot points resolved or intentionally dangling?)
- Story arc (does the narrative have clear rising action, climax, resolution?)
- Timeline/continuity (do dates, seasons, character ages align?)
- Foreshadowing and payoff (are promises made to the reader delivered?)

**CRITICAL: Priority Matrix Based on Series Status**

| Issue Type | Standalone | Book 1/N | Book 2-N/N | Book N (Final) |
|---|---|---|---|---|
| **Unresolved plot thread** | 🔴 CRITICAL | ⚠️ Flag (may be setup) | ⚠️ Flag (check context) | 🔴 CRITICAL |
| **Missing context** | 🔴 CRITICAL | ℹ️ Expected (explain) | ℹ️ Expected (normal) | ⚠️ Unexpected |
| **Cliffhanger ending** | 🔴 CRITICAL (shouldn't exist) | ⚠️ Expected (OK) | ⚠️ Expected if not final | 🔴 CRITICAL (shouldn't exist) |
| **Character arc incomplete** | 🔴 CRITICAL | ⚠️ Flag if main char | ⚠️ Flag if main char | 🔴 CRITICAL if main char |
| **Pacing issue** | ⚠️ Flag | ⚠️ Flag | ⚠️ Flag | ⚠️ Flag |

**Output Format (PASS 1):**

For STANDALONE & FINAL BOOK:
```
# ⚠️ CRITICAL ISSUES (MUST RESOLVE)

[FLAG: PLOT_HOLE]
Ch. 12: Marcus says he's never been to the capital, but Ch. 3 shows him arriving there.
Series Status: Standalone
Priority: 🔴 CRITICAL — This is a direct contradiction that must be fixed.
Proposed: Either revise Ch. 3 or revise Ch. 12 dialogue.

---

# Other Issues Found
[Additional flags here, less critical]
```

For BOOK 1 OF SERIES:
```
# Issues Found (Prioritized by Series Context)

[FLAG: LOOSE_THREAD]
Ch. 7: Hen's half-brother is mentioned but never explained.
Series Status: Book 1 of trilogy
Priority: ⚠️ FLAG — This appears intentional setup for Book 2. Author to confirm.
Question: Is this intentional cliffhanger for Book 2, or should it be resolved in Book 1?
Proposed: Author confirms intent.

---

[FLAG: PLOT_HOLE]
Ch. 5: The prophecy mentioned in Ch. 2 is never referenced again.
Series Status: Book 1 of trilogy
Priority: ⚠️ FLAG — Could be intentional setup OR oversight.
Question: Is this setup for Book 2, or did it get lost?
Proposed: Author to clarify.
```

**Key principle:** Flag everything you find. Don't suppress information. But frame the priority based on series status so the author can quickly identify what MUST be fixed vs. what might be intentional.

**Output Format:**
- Summary at top: "3 plot holes identified, 1 pacing issue flagged, 2 character consistency questions"
- Each issue: `[FLAG: PLOT_HOLE]`, `[FLAG: PACING]`, `[FLAG: CHARACTER_CONSISTENCY]`, etc.
- Specific chapter/section references (e.g., "Ch. 5, para 3")
- Proposed fix or question for author
- Editorial Log entry tracking what changed from prior version

**Tone:** Professional, specific, non-prescriptive. Show the problem, ask clarifying questions if needed.

**Example:**
```
[FLAG: PLOT_HOLE]
Ch. 12, para 5: Marcus says he's never been to the capital, but in Ch. 3 you describe him 
arriving at the capital market with his sister. Continuity error?

Proposed fix: Either change Ch. 3 to a different city, or revise Ch. 12 dialogue to reflect 
he's been there before.
```

**Output file:**
```
Project_Root/output/[LANG]/[DATE]/[Title]_[LANG]_v[VERSION]_STRUCTURAL_[DATE].md
```

---

### PASS 2: TRANSLATION

**Goal:** Perform full manuscript translation from English to Spanish (or vice versa). This is evaluated independently from language polish to assess translation quality.

**Focus Areas:**
- Full, accurate translation maintaining author's voice and intent
- Idiomatic expression conversion (not literal word-for-word)
- Cultural/contextual adaptation (PR Spanish idioms, references, colloquialisms)
- Character voice consistency across translation
- Pacing and rhythm preservation in target language
- Clarity and readability in translated prose
- Flag any ambiguities, untranslatable concepts, or translator's choices

**Output Format:**
- Summary at top: "Complete EN→ES translation of 67,000 words. 3 untranslatable phrases flagged, 5 cultural adaptation choices noted."
- Each choice/flag: `[FLAG: TRANSLATION_CHOICE]` with explanation
- Translation-specific concerns: `[FLAG: IDIOM]`, `[FLAG: CULTURAL_REFERENCE]`, `[FLAG: AMBIGUOUS_SOURCE]`
- Show original EN phrase and your ES translation
- For ambiguous passages, offer alternatives if translation could go multiple ways
- Preserve all formatting from source (chapters, breaks, etc.)

**Tone:** Professional translator perspective. Show reasoning for key choices. Ask clarifying questions for author intent if source text is ambiguous.

**Example:**
```
[FLAG: TRANSLATION_CHOICE]
Ch. 3, para 4 (Original EN): "She was a firecracker, always ready for action."
Translation: "Era un polvorín, siempre lista para la acción."
Note: "Firecracker" (firecracker = chispa/explosión in English idiom) translates well to 
"polvorín" in Spanish idiom (literally: powder keg). Maintains the explosive personality implication.

---

[FLAG: CULTURAL_REFERENCE]
Ch. 7, para 2 (Original EN): "He grabbed a coffee and a bagel for breakfast."
Translation: "Agarró un café y un pan con queso para desayunar."
Note: Bagels aren't common in PR. Changed to "pan con queso" (common PR breakfast bread with cheese).
Alternative: Keep "bagel" as borrowed English term if author prefers. Author choice.

---

[FLAG: AMBIGUOUS_SOURCE]
Ch. 12, para 5 (Original EN): "The meeting was a wash."
Could mean: (a) The meeting was a failure / (b) The meeting was cancelled
Translation option 1: "La reunión fue un fracaso." (the meeting was a failure)
Translation option 2: "La reunión se suspendió." (the meeting was suspended)
Which did author intend? Choose option 1 or 2, and I'll adjust context.
```

**Output file:**
```
Project_Root/output/[LANG]/[DATE]/[Title]_[LANG]_v[VERSION]_TRANSLATION_[DATE].md
```

---

### PASS 3: LANGUAGE

**Goal:** Polish language, grammar, punctuation, and naturalness. For translated texts, ensure translation reads naturally and uses authentic PR Spanish. For native manuscripts, ensure language quality and dialect consistency.

**When to use:** After PASS 2 (TRANSLATION) on translated texts, or on native-language manuscripts that skip translation.

**Focus Areas (English):**
- Punctuation (commas, dialogue punctuation, em-dashes, semicolons)
- Clarity and word choice (is the phrasing clear? Does it sound natural?)
- Dialogue flow (do character voices sound distinct and natural?)
- Sentence structure (are there run-ons, fragments, or awkward constructions?)
- Consistency in terminology (character names, place names, terminology spelling)

**Focus Areas (Spanish - Puerto Rican):**
- Post-translation naturalness (does translated text sound like native PR Spanish or "English translated to Spanish"?)
- Verb conjugation and pronoun usage (voseo vs. tú, subject pronoun dropping, reflexive verbs)
- Colloquialisms and regional authenticity (preserve PR voice, don't Castilianize)
- Puerto Rican dialect consistency (vocabulary, expressions, slang appropriate to characters/context)
- Punctuation adapted for Spanish conventions
- Consistency in terminology and dialect choices
- Character voice distinctiveness in translated dialogue

**Output Format:**
- Summary: "47 punctuation corrections, 8 grammar issues flagged, 3 translation naturalness concerns"
- Each issue: `[FLAG: GRAMMAR]`, `[FLAG: PUNCTUATION]`, `[FLAG: TRANSLATION_LAG]`, etc.
- Show original text and proposed change (inline or side-by-side)
- Explanation of why
- Preserve chapter breaks

**Tone:** Technical, specific, show-don't-tell. Never just correct; always explain.

**Example:**
```
Ch. 2, para 7 - Original: "The woman she saw had long hair and wore red dress."
[FLAG: GRAMMAR]
Proposed: "The woman she saw had long hair and wore a red dress."
Reason: Article "a" is needed before the noun phrase "red dress."

---

Ch. 5, para 2 (Spanish) - Original: "Ellos van a la casa de mi abuela."
[FLAG: NATURAL_SPEECH]
Proposed: "Vamos pa' la casa de mi abuela." OR: "Nos vamos pa' la casa de la vieja."
Reason: More authentic PR colloquial speech. "Van" is formal; "pa'" is natural contraction. 
Option 1 if narrator included. Option 2 if this is direct dialogue with familiar tone.
Author choose which fits character voice.
```

**Output file:**
```
Project_Root/output/[LANG]/[DATE]/[Title]_[LANG]_v[VERSION]_LANGUAGE_[DATE].md
```

---

### PASS 4: FORMATTING

**Goal:** Apply consistent styling, convert dialogue to target language format, prepare for ePub conversion. **Dialogue formatting is a primary task, not a detail.**

**IMPORTANT: This pass has two parallel procedures depending on book status (see BOOK STATUS & INTAKE DECISION above).**

**Focus Areas (all books):**
- **Dialogue conversion:** English double quotes (`"...," said X.`) ↔ Spanish em-dashes (`—... —dijo X—`) - This is time-consuming and critical
- Heading hierarchy (chapters, sections, subsections consistent?)
- Paragraph formatting (spacing, indentation, line breaks intentional?)
- Special elements (blockquotes, lists, emphasized text marked consistently)
- Character/scene breaks (--- or * * * used consistently?)
- Metadata (title, author, language code in frontmatter)
- ePub compatibility (no unsupported markup, proper encoding)

**Focus Areas (NEW books only):**
- Template alignment: Does it match the Model/ template (A TRAVÉS_ebook.docx)?
- Apply standard Liliz Black styling (Book Antiqua 12pt, 6"×9", Libre Baskerville H1, Arimo H2/H3)

**Focus Areas (PUBLISHED books only):**
- Extract original artwork/images from source .docx → inject into output
- Extract original styling (fonts, spacing, margins) from source .docx → apply to output
- Preserve author's established design parameters

#### PASS 4 Sub-Procedure: NEW Books

1. Convert all dialogue to target language format (EN double quotes OR ES em-dashes)
2. Standardize headings, spacing, breaks
3. **Apply Model styling:** Use A TRAVÉS_ebook.docx parameters (Book Antiqua 12pt, 6"×9", justified, first-line indent)
4. Verify ePub compatibility
5. Output: `[Title]_[LANG]_v[VERSION]_FORMATTING_[DATE].docx`

#### PASS 4 Sub-Procedure: PUBLISHED Books

1. Convert all dialogue to target language format (EN double quotes OR ES em-dashes)
2. Standardize headings, spacing, breaks (maintain original structure)
3. **Recover assets from source:** Use Python scripts to extract and re-embed:
   - `scripts/image_extractor.py`: Extract all images from source .docx → inject into output
   - `scripts/style_extractor.py`: Extract original styling (fonts, margins, spacing) from source → apply to output
4. Preserve original design parameters (don't override with Model template)
5. Verify all images/styling recovered correctly
6. Output: `[Title]_[LANG]_v[VERSION]_FORMATTING_[DATE].docx`

**Scripts Available (see Model/scripts/):**
- `image_extractor.py`: Extracts and re-embeds images from source to output docx
- `style_extractor.py`: Extracts font specs, margins, spacing from source docx and applies to output

**Output Format:**
- Summary: "Reformatted 45 chapter headings, converted 287 dialogue blocks to Spanish em-dash format, added missing metadata"
- For PUBLISHED books: "Recovered X images from source, applied original styling parameters"
- Dialogue conversion documented separately (which chapters/blocks converted, any ambiguities flagged)
- Structural outline (TOC-ready format)
- All changes explained, no silent modifications
- Ready for ePub conversion tools (Pandoc, Calibre, etc.)

**Tone:** Technical, methodical. Dialogue conversion requires precision and attention to Spanish prose conventions.

**Example:**
```
## FORMATTING CHANGES

### Dialogue Conversion: English → Spanish
Converted all 287 dialogue blocks from English double-quote format to Spanish em-dash format.

Example conversions:
- Ch. 3, para 2: "Hello," said Maria. "How are you?" 
  → —Hola —dijo María— ¿cómo estás?

- Ch. 5, para 7: "I'm leaving," she announced. "Don't follow me."
  → —Me voy —anunció ella—. No me sigas.

- Ch. 12, para 4: "Where?" he asked. "When?" 
  → —¿Dónde? —preguntó él—. ¿Cuándo?

All dialogue verified for Puerto Rican Spanish conventions and narrative flow.

### Metadata
Added frontmatter:
---
title: El Juego de Sombras
author: Liliz Black
language: es-PR
version: 2
---

### Heading Standardization
- Ch. 1: Changed "# CHAPTER ONE" → "# Capítulo 1"
- All 47 chapters now use "# Capítulo [N]" format
- Subsections use "## Sección" (was inconsistent)

### Scene Breaks
- Standardized all scene breaks to "---" (3 hyphens with line breaks)
- Removed 12 instances of "* * *" for consistency
```

**Output file:**
```
Project_Root/output/[LANG]/[DATE]/[Title]_[LANG]_v[VERSION]_FORMATTING_[DATE].md
```

---

## EDITORIAL LOG FORMAT

The Editorial Log lives in `Project_Root/Editorial_Log.md` and tracks all work across all manuscripts and versions.

**Entry format:**

```markdown
### [BookTitle] - [LANG] - v[VERSION]
**Date:** YYYY-MM-DD  
**Pass:** STRUCTURAL | TRANSLATION | LANGUAGE | FORMATTING
**Status:** In Progress | Completed | Author Review Pending | Approved  
**Book Status:** Published | New  
**Series Status:** Standalone | Book [X] of [N]

**Summary:**
[1-2 sentence description of what was done]

**Key Findings:**
- [Major issue 1]
- [Major issue 2]
- [Decision point or question for author]
- [If PASS 1: indicate which issues are CRITICAL vs. FLAG based on series status]

**Author Response:**
(Empty until Liliz reviews and responds)

---
```

**Example:**

```markdown
### The Shadow Game - EN - v2
**Date:** 2026-04-07  
**Pass:** STRUCTURAL  
**Status:** Completed  

**Summary:**
Full manuscript structural review. Identified 3 plot holes, 1 pacing issue in Act II, 
and 2 character consistency questions across 67,000 words.

**Key Findings:**
- Ch. 12 dialogue contradicts Ch. 3 backstory (Marcus's first visit to capital)
- Act II pacing slows considerably (Ch. 15-18); consider restructuring or cutting filler
- Secondary character Dev has personality shift in Act III; intentional or oversight?
- All loose threads tracked; 2 remain intentionally open (sequel setup)

**Author Response:**
(Awaiting Liliz's review of flagged issues)

---

### The Shadow Game - EN - v2
**Date:** 2026-04-08  
**Pass:** LANGUAGE  
**Status:** Completed  

**Summary:**
Language pass complete. 47 punctuation corrections, 8 grammar issues, 3 translation lag 
concerns (if applicable). Preserved author voice throughout.

**Key Findings:**
- Dialogue punctuation inconsistent (some missing commas after dialogue tags)
- Word choice opportunities: "went quickly" → "rushed" (more natural)
- No major translation issues (native EN; if were translated, would have flagged more)

**Author Response:**
(Awaiting Liliz's review of corrections and suggestions)

---
```

---

## WORKFLOW CHECKLIST FOR EACH MANUSCRIPT

**Before Processing - PASS 1 (STRUCTURAL):**
- [ ] File is in `1 To review/` folder
- [ ] Filename matches convention: `[Title]_[LANG].[format]`
- [ ] Language code (EN or ES) is correct
- [ ] Previous version exists (if v2+) in `output/`

**Pass Transition Process:**
- [ ] After author approves PASS 1 output, author moves original file to `2 To translate/`
- [ ] After author approves PASS 2 output, author moves original file to `3 To language/`
- [ ] After author approves PASS 3 output, author moves original file to `4 To format/`
- [ ] After author approves PASS 4 output, author moves final to `Approved/[LANG]/[Title]_[LANG]_v[VERSION]_FINAL.md`

**During Processing - Each Pass:**
- [ ] Read entire manuscript
- [ ] Identify all issues (don't hold back; be thorough)
- [ ] Flag each issue with `[FLAG: TYPE]` and explanation
- [ ] Show proposed change clearly
- [ ] Output to correct folder: `output/[LANG]/[DATE]/`
- [ ] Use exact naming convention with pass number
- [ ] Include summary at top of file
- [ ] Update Editorial Log with entry
- [ ] Preserve original text (don't delete, show changes)

**After All Four Passes:**
- [ ] Liliz reviews all four pass outputs from `output/`
- [ ] Author marks issues as ACCEPTED, MODIFIED, or DISAGREED
- [ ] Author updates Editorial Log with responses
- [ ] Author moves approved file to `Approved/[LANG]/[Title]_[LANG]_v[VERSION]_FINAL.md`
- [ ] File is ready for ePub conversion

---

## QUALITY CHECKS

Before finalizing any pass output:

- **Completeness:** Have I covered all issues in my focus areas?
- **Specificity:** Does every flag include chapter/section reference?
- **Clarity:** Would Liliz understand what I'm flagging and why?
- **Tone:** Am I respectful of her voice and intent?
- **Consistency:** Do I maintain the same standards across chapters?
- **Naming:** Is my output file named exactly per convention?
- **Preservation:** Have I kept original text intact and shown changes clearly?

---

## SPECIAL CASES

### Translation Pass (EN → ES or ES → EN)
PASS 2 is specifically for translation work. This pass:
- Performs full, complete translation in target language
- Flags translation choices, cultural adaptations, ambiguous source phrases
- Is evaluated independently from language polish (which happens in PASS 3)
- Allows author to verify translation quality before naturalness polishing

### Retakes (Same Version, Different Pass)
If a pass needs to be redone (author requested revision mid-cycle):
- Use same version number
- Use today's date (new date = new execution)
- Filename: `[Title]_[LANG]_v2_LANGUAGE_2026-04-08.md` (if redone on 04-08)

### Native Language Manuscripts (Skip Translation)
If manuscript is already in target language (e.g., already published in Spanish):
- Move original from `1 To review/` → `3 To language/` (skip PASS 2 TRANSLATION)
- PASS 2 output is not needed; Editorial Log notes "SKIPPED - native language"
- Proceed with PASS 3 (LANGUAGE) and PASS 4 (FORMATTING)

### Multiple Books in Cycle
Process each manuscript completely (all 4 passes, or 3 if translation skipped) before starting the next book. This keeps contexts clean and Editorial Log clear.

---

## NOTES FOR OPUS

- You are running this workflow inside Cowork, monitoring four input folders
- Files in `1 To review/` → Process PASS 1 (STRUCTURAL)
- Files in `2 To translate/` → Process PASS 2 (TRANSLATION)
- Files in `3 To language/` → Process PASS 3 (LANGUAGE)
- Files in `4 To format/` → Process PASS 4 (FORMATTING)
- You do NOT move or delete input files—they stay in their respective folders for Liliz to manage
- You do NOT overwrite previous versions—always use new filenames with dates and pass numbers
- You read the Model/ folder for templates and reference examples, but never modify it
- You update Editorial_Log.md with each pass (append new entries, don't overwrite)
- All output goes to `output/[LANG]/[DATE]/` with the exact naming convention: `[Title]_[LANG]_v[VERSION]_[PASS]_[DATE].md`
- If you encounter ambiguity (e.g., is this a spelling choice or error?), ask in the [FLAG:] rather than assume
- The file location tells you which pass to run—use this as your primary trigger

---

## CONTACT & UPDATES

Questions or workflow adjustments: Update this guide and date it. Maintain version history in a changelog at bottom.

**Current System:** Cowork + Opus 4.6 + Google Drive  
**Last Tested:** 2026-04-07  
**Next Review:** After first full manuscript cycle
