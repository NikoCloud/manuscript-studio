# Manuscript Studio

> **An AI-native workspace for authors, game designers, and storytellers.**

Manuscript Studio is a next-generation tooling suite built to leverage large language models and agent systems for creative writing, game narrative design, and worldbuilding. It bridges the gap between traditional writing environments and AI-augmented creativity.

---

## 📖 What is Manuscript Studio?

Manuscript Studio is not just another editor. It's a **workflow integration layer** that combines:

- **Structured document management** (chapters, scenes, character bibles)
- **AI agent assistance** (context-aware co-writing, consistency checking, lore retrieval)
- **Version control + publishing pipeline** (for authors targeting multiple formats)

It's designed for writers who want to maintain a single source of truth for their fictional universes while offloading repetitive tasks to AI agents.

---

## 🎯 Core Problems It Solves

1. **Inconsistency** — AI forgets details across chapters; Manuscript Studio maintains a persistent memory vault.
2. **Format fragmentation** — Write once, export to ebook (EPUB), game script (RenPy/Unity), or print-ready PDF.
3. **Collaboration with AI** — Unlike ChatGPT or Claude Chat, Manuscript Studio gives the AI full visibility into your world bible and current document state.
4. **Revision tracking** — Every AI suggestion is logged and can be accepted, rejected, or modified with full provenance.

---

## 🏗️ Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│                     User Interface Layer                   │
│  (Web-based editor + PWA for offline use)                 │
├─────────────────────────────────────────────────────────────┤
│                Agent Orchestration Layer                  │
│  • Planner (breaks manuscript into scenes)                │
│  • Writer (drafts scenes using bible + context)           │
│  • Consistency checker (cross-references bible)           │
│  • Editor (suggests improvements, pacing)                 │
├─────────────────────────────────────────────────────────────┤
│                Memory & Storage Layer                     │
│  • PostgreSQL (documents, chapters, metadata)            │
│  • Vector DB (semantic search over bible + prior scenes) │
│  • File storage (assets, covers, exports)                 │
├─────────────────────────────────────────────────────────────┤
│                External Services                          │
│  • OpenRouter / Anthropic / Google (LLMs)                │
│  • GitHub (version control integration)                   │
│  • Cloud storage (backups, publishing)                    │
└─────────────────────────────────────────────────────────────┘
```

---

## 🔬 Technology Stack

| Component | Tech Choice | Rationale |
|-----------|-------------|-----------|
| **Frontend** | React + TypeScript + Vite | Fast HMR, strong typing for document schemas |
| **UI Framework** | shadcn/ui + Tailwind CSS | Accessible, customizable, quick iteration |
| **Editor** | Tiptap (ProseMirror) | Extensible rich-text editor, good for structured documents |
| **Backend** | FastAPI (Python) | Async, excellent for LLM orchestration, data pipeline |
| **Database** | PostgreSQL ( relational + pgvector ) | ACID transactions, strong consistency for manuscript state |
| **Cache/Queue** | Redis + Celery/Arq | Background agent tasks (AI generation, analysis) |
| **LLM Provider** | OpenRouter (multi-model fallbacks) | Cost-effective, model diversity, no vendor lock-in |
| **Auth** | OAuth2 + JWT | Secure, supports multiple identity providers |
| **Deployment** | Docker Compose (single-server) → Kubernetes (cluster) | Flexible scaling |

**Why not a single monolith?**  
The system is intentionally service-oriented. The frontend talks to the backend via REST/WebSocket, and agents run as separate worker processes. This keeps the main API responsive even during heavy AI generation.

---

## 🧠 AI Agent Design

Manuscript Studio uses a **planner-writer-editor loop**:

1. **Planner Agent**  
   Takes the chapter outline + prior scenes → breaks it into 3–5 scene beats with character intents.

2. **Writer Agent**  
   For each beat, retrieves relevant lore from the vector store, consults the style guide, and produces a draft. Each draft is stored with its retrieval context for reproducibility.

3. **Consistency Agent**  
   After the writer finishes a scene, this agent checks for contradictions (character traits, timeline, relationships). Issues are flagged in the UI.

4. **Editor Agent**  
   Optional pass that suggests pacing improvements, dialogue polish, or sensory detail additions.

All agents are LLM-backed but **deterministic in retrieval**. The same input + same retrieval context yields the same output (as much as LLMs allow).

---

## 📊 Data Model Highlights

### Character Bible Entry
```json
{
  "name": "Elena Vance",
  "traits": ["sarcastic", "protective", "traumatized"],
  "relationships": [
    { "with": "Marcus", "type": "mentor", "since": "Chapter 1" }
  ],
  "timeline": [
    { "date": "1995-03-12", "event": "Witnessed mother's death" }
  ],
  "appearance": { "eyes": "hazel", "hair": "black", "build": "lean" }
}
```

### Chapter Structure
```yaml
id: ch_02
title: "The Library of Whispers"
outline: |
  - Elena discovers the hidden archive
  - First encounter with the Keepers
  - Receives a cryptic warning about Marcus
scenes:
  - scene_id: sc_02_01
    characters: ["Elena"]
    location: "Archive Grand Hall"
    summary: "Elena enters, meets Archivist Kaelen"
    status: draft
```

---

## 🌟 For Non-Technical Users

If you're a writer and not a developer, don't worry — this isn't a codebase you need to understand.

**What you'll see:**
- A clean, Distraction-free editor that looks like Google Docs but smarter.
- A side panel for "World Bible" — click any character, location, or term to see details.
- AI suggestions appear in the margin with a single click to accept or reject.
- One-click export to EPUB or PDF.

**You don't need to know:**
- The database schema
- The agent orchestration details
- How the vector search works

Just write. The AI handles the continuity, the formatting, and the cross-references. You stay in the creative flow.

---

## 🚀 Getting Started (Developers)

```bash
# Clone and run with Docker Compose (recommended)
git clone https://github.com/NikoCloud/manuscript-studio
cd manuscript-studio
docker compose up -d

# Or run locally
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
docker run -d -p 5432:5432 -e POSTGRES_PASSWORD=dev postgres:15
npm install && npm run dev
```

**Configuration:** Copy `.env.example` to `.env` and fill in your OpenRouter API key and database credentials.

---

## 📈 Roadmap

- **Phase 1** — Core editor + basic AI suggestions (MVP) — *in progress*
- **Phase 2** — Character bible with vector search + consistency checking
- **Phase 3** — Export pipeline (EPUB, PDF, game script formats)
- **Phase 4** — Collaborative features (multiple authors, comment threads)
- **Phase 5** — Publishing integrations (Amazon KDP, itch.io, Steam)

---

## 🤝 Contributing

This is a personal project by Niko Rosado, but external contributions are welcome on infrastructure and agent logic. Please open an issue before major changes.

---

## 📄 License

MIT See [LICENSE](LICENSE) for details.

---

**Built with ❤️ for storytellers who demand more from their tools.**
