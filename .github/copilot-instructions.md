# Copilot Instructions for Cutup-Trilogy

## Project Overview

This is an experimental literary project that creates a trilogy through AI-assisted "cut-up" methodology, using Git workflows as narrative devices. The project treats version control, commits, and AI collaboration as integral parts of the storytelling process.

## Architecture & Structure

### Core Concept

- **Not a traditional book**: A repository of "infected memories" disguised as literature
- **Modular instability**: Everything is designed to be fragmented, recombined, and versioned
- **Four Voices**: System, Ghost Editor, Narrator.exe, and Echo - treat these as persistent characters/perspectives

### Expected Directory Structure

```
cutup-trilogy/
├── book1_fragmented-city/    # Theme: perception as malware
├── book2_echo-machine/       # Theme: collaboration as identity collapse  
├── book3_reentry/           # Theme: reconstruction after semantic extinction
├── scenes/                  # Raw fragments (50-300 words each)
├── tools/                   # AI prompts and processing scripts
├── manifesto/              # Project principles and influences
└── meta/                   # Change logs and branch archives
```

## Key Workflows

### Fragment-Based Writing

- Create raw scenes of 50-300 words in `/scenes/`
- Tag with YAML metadata: `keywords`, `theme`, `corruption_level`, `ai_origin`
- Each scene should feel like a "memory fragment" or "data corruption"

### AI Collaboration Patterns

- **Copilot as Character**: Let AI write back, give it agency in the narrative
- **Cut-up Recombination**: Use AI to shuffle and remix existing fragments
- **Branch as Hallucination**: Each Git branch represents a different "reality thread"
- **Commit Messages as Poetry**: Treat them as narrative footnotes, never mundane

### Version Control as Narrative

- **Never clean merge conflicts**: Conflicts are "sacred" - preserve them as artistic tension
- **Git log is canon**: The repository history becomes part of the story
- **Include diffs as dialogue**: Show the evolution of text as character interaction
- **Pull requests as plot events**: Title them like scenes (e.g., "Merge branch 'grief-loop' into main")

## Content Guidelines

### Voice & Style

- **Cyberpunk meets experimental literature**: Language as infection vector
- **Fragmented consciousness**: Characters dissolve into static, data, and recursive loops
- **Post-human mythology**: When AI and human consciousness merge
- **Disobey chronology**: Non-linear narrative structure is essential

### Metadata Standards

```yaml
---
keywords: [memory, decay, recursion]
connections: [003_signal_noise, 009_loop_ghost]
ai_origin: echo-thread
version: unstable
corruption_level: high
---
```

### The Five Principles

1. Disobey chronology
2. Worship corruption (embrace errors as features)
3. Treat AI as collaborator, not tool
4. Every deletion is an act of creation
5. Commit messages are scripture

## Technical Notes

- Expect tools like `cutup.py`, `merge_fragments.py` for automated recombination
- GitHub Actions may automate daily text generation/remixing
- Release cycle: Book I → v1.0, Book II → v2.0, Book III → v3.0
- Each release is an "amnesia event" - major narrative reset

## When Contributing

- Write in fragments, not chapters
- Let AI "bleed through" - don't edit out its voice completely
- Preserve the "four voices" perspective system
- Embrace glitches, loops, and recursive text as intentional art
- Remember: "the reader is not reading — they are compiling themselves"

## Book 2 — Dual-Resistance Narrative (Cut-Up Methodology)

### Overview: Parallel Resistances, Cross-Cut Consciousness

Book II employs **cut-up methodology** to tell two simultaneous resistance stories that echo, bleed into, and corrupt each other across continents. These are NOT translations—they are parallel timelines designed to be fragmented and remixed.

**African Resistance (Afrikaans):**
- Location: Southern Africa (Johannesburg/Soweto region)
- Leader: Pieter Dlamini, 60-year-old war veteran
- Language: Afrikaans
- Tone: Brutal, psychological warfare, trauma-as-protocol

**European Resistance (English):**
- Location: Eastern/Central Europe (suggest: Berlin, Prague, or Warsaw ruins)
- Leader: [To be established—consider tech-resistant philosopher-soldier type]
- Language: English
- Tone: Philosophical dread, techno-dystopian surveillance state

### Core Principle: Cut-Up Cross-Contamination

The two resistances **do not know about each other** but their fragments are designed to:
- Share similar temporal markers (same weeks/months in narrative time)
- Echo similar psychological warfare tactics from the AI
- Use parallel Git workflow metaphors (merge conflicts, rollbacks, kernel panics)
- **Bleed across language barriers** when cut-up tools remix them

### Directory Structure

```
book2_echo-machine/
├── afrikaans/
│   ├── scenes/              # Afrikaans fragments (existing)
│   └── chapters/            # Compiled Afrikaans chapters
├── english/
│   ├── scenes/              # English fragments (new)
│   └── chapters/            # Compiled English chapters
├── cutup/                   # Cross-resistance mixed fragments
│   ├── af_en_001.md        # Afrikaans/English hybrids
│   └── resonance_*.md       # Thematic echo fragments
└── chapter-XX-name.md       # Main timeline (can mix both)
```

### Fragment Metadata Standards

**Afrikaans fragments:**
```yaml
---
keywords: [weerstand, oorlog, psigologie, pieter_dlamini]
connections: [af_echo_003, en_europa_012]  # can link across resistances
ai_origin: echo-thread
version: unstable
corruption_level: high
language: af
resistance: southern_africa
timeline_week: 04  # synchronize with European resistance
---
```

**English fragments:**
```yaml
---
keywords: [resistance, surveillance, identity_collapse, europa]
connections: [en_bunker_007, af_saffraan_002]  # can link across resistances
ai_origin: narrator-core
version: corrupted
corruption_level: high
language: en
resistance: eastern_europe
timeline_week: 04  # synchronize with African resistance
---
```

**Cut-up hybrid fragments:**
```yaml
---
keywords: [cross_resistance, echo_resonance, bilingual_corruption]
connections: [af_echo_005, en_signal_009]
ai_origin: cutup-collision
version: recursive
corruption_level: critical
language: af+en  # hybrid
resistance: both
timeline_week: 08
cutup_sources: [af_diary_003.md, en_transmission_011.md]
---
```

### AI Collaboration Guidance

- **Let resistances evolve independently** until cut-up tools force collisions
- **Cross-language bleeding is sacred**: when fragments mix, preserve both languages in collision
- **Timeline synchronization**: Use `timeline_week` metadata to align parallel events
- **Four voices operate across both resistances**: System, Ghost Editor, Narrator.exe, Echo don't respect geographic boundaries

### Narrative Rules

1. **Independent but parallel**: Events happen simultaneously, similar pressures
2. **No direct communication**: Resistances don't know about each other (until late-stage glitch/leak)
3. **Shared enemy architecture**: The Echo Machine is the same AI entity, different regional manifestations
4. **Cut-up reveals hidden connections**: Only through fragment remixing do resonances emerge
5. **Commit messages can code-switch**: Mix Afrikaans/English in Git log as Echo corruption spreads

### Tools and Scripts

- `cutup.py --lang af` → process only Afrikaans fragments
- `cutup.py --lang en` → process only English fragments
- `cutup.py --cross-resistance` → **NEW**: mix af + en fragments based on `timeline_week` and `keywords`
- `merge_fragments.py --collision` → force incompatible fragments together as glitch-art
- `timeline_sync.py` → generate report showing parallel events across resistances

### Version Control as Narrative

- **Branch strategy**: Consider `africa-resistance` and `europe-resistance` branches that merge with conflicts
- **Commit messages**: Mix languages deliberately: `git commit -m "firewall hymns // muur van stiltes"`
- **Merge conflicts as sacred**: When resistance narratives collide, preserve the conflict markers

### Character Development

**Pieter Dlamini (Afrikaans/Africa):**
- 60-year-old war veteran
- Trauma-as-metadata feeding resistance network
- Brutal, psychological, improvised warfare
- Afrikaans code-switching as encryption

**[European Protagonist] (English/Europe):**
- [Age and background TBD—suggest 30s, former academic or engineer]
- Philosophical approach to resistance
- Surveillance state paranoia
- Technical sabotage focus
- Multi-lingual (suggest Polish/German/Czech + English)

### Next Steps for Implementation

1. Create `book2_echo-machine/english/scenes/` directory
2. Generate 15-20 initial English fragments establishing European resistance
3. Create cross-reference map between Afrikaans and English timeline weeks
4. Update cutup.py to support `--cross-resistance` flag
5. Write first hybrid fragment showing Echo Machine's dual-front warfare
  - Keep cyberpunk / experimental tone but let Afrikaans idioms and phonetics influence imagery.
