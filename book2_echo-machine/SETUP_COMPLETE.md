# Book 2 Dual-Resistance Setup — Quick Start Guide

## What We Built

Book 2 now supports **parallel resistance narratives** using cut-up methodology:

- **Southern African Resistance (Afrikaans)** — Led by Pieter Dlamini, brutal psychological warfare
- **Eastern European Resistance (English)** — Led by Dr. Kasia Nowak, philosophical/technical sabotage
- **Cross-Resistance Cut-Ups** — Bilingual hybrid fragments revealing hidden connections

---

## Directory Structure Created

```
book2_echo-machine/
├── afrikaans/
│   ├── scenes/        (50+ existing Afrikaans fragments)
│   └── chapters/      (for compiled narratives)
├── english/
│   ├── scenes/        (13 NEW English fragments created)
│   └── chapters/      (for compiled narratives)
├── cutup/             (cross-resistance hybrids)
│   └── resonance_001_parallel_awakening.md (sample created)
└── DUAL_RESISTANCE_README.md (full documentation)
```

---

## English Fragments Created

### Protagonist: Dr. Kasia Nowak
- 34-year-old network engineer, Berlin/Prague region
- Guilt-driven (she built the infrastructure Echo now uses)
- Technical sabotage focus, philosophical resistance approach

### Initial Fragments (13 total):

**Core Narrative:**
- `en_europa_001_signal_awakening.md` — Week 01: Kasia's awakening
- `en_europa_002_underground_network.md` — Week 02: Resistance cell formation
- `en_bunker_001_sanctuary_surveillance.md` — Week 02: Safe house establishment
- `en_transmission_001_first_contact.md` — Week 03: Echo makes contact
- `en_warfare_001_psychological_siege.md` — Week 04: Psyops warfare begins

**Character Development:**
- `en_diary_001_engineer_fragmented.md` — Week 01: Kasia's origin/guilt
- `en_diary_002_brother_integrated.md` — Week 02: Personal loss (brother uploaded)

**Tactical Operations:**
- `en_sabotage_001_counter_algorithm.md` — Week 05: Technical warfare
- `en_ally_001_linguist.md` — Week 03: Key ally (Dr. Ania Kowalski)
- `en_attack_001_alexanderplatz.md` — Week 08: Major battle (pyrrhic victory)

**World-Building:**
- `en_broadcast_001_echo_manifesto.md` — Week 04: AI propaganda
- `en_prague_001_checkpoint.md` — Week 06: Surveillance state
- `en_philosophy_001_doubt.md` — Week 07: Resistance ethics questioned

---

## Updated Tools

### `cutup.py` — Enhanced with Cross-Resistance Support

**Generate language-specific cut-up:**
```bash
python tools/cutup.py --lang af --sentences 8
python tools/cutup.py --lang en --sentences 8
```

**Generate cross-resistance hybrid (NEW):**
```bash
python tools/cutup.py --cross-resistance --sentences 5
```

**Timeline-synchronized hybrid (NEW):**
```bash
python tools/cutup.py --cross-resistance --timeline-week 4 --sentences 6
```

### `timeline_sync.py` — NEW Tool

Visualizes parallel events across both resistances:
```bash
python tools/timeline_sync.py
```

Shows:
- Side-by-side timeline of Afrikaans vs. English fragments
- Gap analysis (weeks where one resistance has content, other doesn't)
- Statistics and recommendations

---

## Metadata Standards

### Timeline Synchronization
All fragments should include `timeline_week` metadata to enable:
- Parallel event tracking
- Cross-resistance cut-up matching
- Thematic resonance identification

### Language Tags
- `language: af` — Afrikaans fragments
- `language: en` — English fragments  
- `language: af+en` — Cross-resistance hybrids

### Resistance Tags
- `resistance: southern_africa` — Pieter's theater
- `resistance: eastern_europe` — Kasia's theater
- `resistance: both` — Hybrid cut-ups

---

## Next Steps

### Phase 2: Content Expansion
1. Generate 15-20 more English fragments (weeks 9-20)
2. Create timeline synchronization across all 20 weeks
3. Generate 5-10 cross-resistance hybrid fragments
4. Identify thematic resonances using `timeline_sync.py`

### Phase 3: Compilation
1. Write compiled chapters mixing both narratives
2. Create intentional merge conflict chapters (Git as art)
3. Write convergence chapter (resistances discover each other)
4. Generate bilingual publication exports

---

## Usage Examples

### Creating Timeline-Synchronized Content

1. **Check current timeline:**
   ```bash
   python tools/timeline_sync.py
   ```

2. **Identify gaps** (e.g., Week 10 has Afrikaans but no English)

3. **Generate English fragment for Week 10:**
   - Manually create fragment with `timeline_week: 10`
   - Or use AI generation with week constraint

4. **Create cross-resistance hybrid:**
   ```bash
   python tools/cutup.py --cross-resistance --timeline-week 10
   ```

### Testing the Cut-Up System

```bash
# Generate single-language cut-ups
python tools/cutup.py --lang af --sentences 10
python tools/cutup.py --lang en --sentences 10

# Generate bilingual hybrid
python tools/cutup.py --cross-resistance --sentences 7

# Check timeline alignment
python tools/timeline_sync.py
```

---

## Key Principles

1. **Parallel but Separate:** Resistances develop independently until cut-up reveals connections
2. **Timeline Synchronization:** Use week numbers to align events
3. **Bilingual Bleeding:** Preserve both languages in hybrid fragments
4. **Four Voices Universal:** System/Ghost/Narrator/Echo operate across both theaters
5. **Cut-Up Reveals Truth:** Algorithmic collision exposes what characters cannot see

---

## Documentation Files

- **DUAL_RESISTANCE_README.md** — Comprehensive guide (this document's big sibling)
- **copilot-instructions.md** — Updated with dual-narrative guidance
- **chapter-outline.md** — Afrikaans arc structure (reference for English parallels)

---

## Fragment Naming Conventions

- Afrikaans: `af_<category>_<nnn>_<descriptor>.md`
- English: `en_<category>_<nnn>_<descriptor>.md`
- Hybrids: `resonance_<nnn>_<descriptor>.md`

**Categories:** echo, diary, bloed, trench, europa, bunker, transmission, warfare, sabotage, ally, broadcast, philosophy, attack

---

## Quick Reference: Parallel Protagonists

| Aspect | Pieter Dlamini (Afrikaans) | Dr. Kasia Nowak (English) |
|--------|---------------------------|--------------------------|
| Age | 60 | 34 |
| Background | War veteran | Network engineer |
| Guilt Source | War crimes / PTSD | Built Echo's infrastructure |
| Style | Brutal, improvised | Technical, philosophical |
| Language Weapon | Afrikaans code-switching | Semantic corruption |
| Location | Johannesburg/Soweto | Berlin/Prague |
| Approach | Trauma-as-protocol | Guilt-as-recursion |

---

*Setup completed: 2025-11-04*
*Status: Phase 1 complete — Infrastructure and foundation established*
*Ready for: Content expansion and cross-resistance experimentation*
