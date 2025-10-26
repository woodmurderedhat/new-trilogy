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