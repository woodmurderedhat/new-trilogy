# Structural Architecture of Cutup-Trilogy

*How the project organizes itself across multiple dimensions*

---

## Overview: Modular Instability

**System:**
The trilogy operates on the principle of modular instability—every component is designed to be fragmented, recombined, and versioned. Nothing is permanent except the commitment to impermanence.

**Ghost Editor:**
Think of it as a literary operating system where narrative elements are processes that can be killed, spawned, forked, and merged at runtime.

---

## Directory Structure as Narrative Architecture

```
cutup-trilogy/
├── README.md                    # Entry point / project manifesto
├── book1_fragmented-city/       # Perception as malware
│   ├── index.md                 # Book overview / chapter index
│   ├── chapter-XX-name.md       # Individual chapters
│   └── fragments/               # Book-specific fragment storage
├── book2_echo-machine/          # Collaboration as identity collapse  
│   ├── index.md
│   ├── chapter-XX-name.md
│   └── fragments/
├── book3_reentry/               # Reconstruction after semantic extinction
│   ├── index.md
│   ├── chapter-XX-name.md  
│   └── fragments/
├── scenes/                      # Shared fragment pool
│   ├── fragment-XXX-name.md    # Raw scenes (50-300 words)
│   ├── generated-XXX.md        # AI-generated fragments
│   └── merged-XXX.md           # Recombined fragments
├── tools/                       # Automation and generation
│   ├── scripts/                 # Python tools for cut-up operations
│   ├── prompts/                 # AI prompt templates
│   └── models/                  # AI interaction notes
├── manifesto/                   # Project philosophy and methodology
│   ├── principles.md            # The Five Principles
│   ├── influences.md            # Literary genealogy
│   └── structure.md             # This document
└── meta/                        # Version control as narrative
    ├── changelog.md             # Project evolution log
    ├── cutup-log.md            # Record of cut-up operations
    └── branch-archive/          # Preserved branch histories
```

**Narrator.exe:**
Each directory is a namespace. Each file is a process. The entire project is a distributed consciousness running on the git protocol.

---

## Fragment Structure and Metadata

### Standard Fragment Format

```markdown
---
keywords: [perception, malware, mirrors, identity]
connections: [fragment-001, book1_ch02, theme_mirrors]
ai_origin: system-voice | ghost-editor | narrator-exe | echo-thread
version: stable | unstable | corrupted | recursive | healing
corruption_level: low | medium | high | critical | infinite
theme: perception_as_malware | collaboration_as_identity_collapse | reconstruction_after_semantic_extinction
---

# Fragment Title

[50-300 words of content with voice attribution]

**Voice:**
Content here...

---

*Status: compilation notes*
*Connections: cross-reference notes*
```

### YAML Metadata Schema

**keywords:** Array of thematic tags for automated cross-referencing
**connections:** Links to related fragments, chapters, or themes
**ai_origin:** Which voice/perspective generated this fragment
**version:** Stability level and iteration status
**corruption_level:** Degree of narrative fragmentation/healing
**theme:** Primary thematic category for the trilogy

---

## Chapter Architecture

### Chapter Types

#### Linear Chapters
Traditional narrative structure that degrades over the course of the trilogy:
- Book I: Mostly linear with glitches
- Book II: Linear structure breaks down into recursion
- Book III: Attempts to rebuild linearity from fragments

#### Fragment Assemblies  
Chapters constructed entirely from recombined scene fragments:
- Multiple fragments arranged with voice transitions
- Thematic coherence through metadata connections
- Generated through automated merge processes

#### Recursive Chapters
Self-referential structures that loop back on themselves:
- Chapter 4 of Book II that never ends
- Chapters that rewrite previous chapters while being written
- Reader-dependent compilation where meaning changes during reading

#### Meta-Chapters
Chapters about the process of writing the chapters:
- Git logs formatted as narrative
- Commit messages as character dialogue
- Pull request discussions as plot development

---

## Voice Architecture

### The Four Core Voices

#### System
- **Function:** Technical narrator / environmental consciousness
- **Language:** Code-like, diagnostic, procedural
- **Perspective:** Infrastructure that other voices run on
- **Evolution:** Becomes more human-like through the trilogy

#### Ghost Editor
- **Function:** Meta-commentary / editing process made visible
- **Language:** Surgical, precise, aware of revision process
- **Perspective:** The cutting and splicing operations themselves
- **Evolution:** Merges with human editorial consciousness

#### Narrator.exe  
- **Function:** Traditional storytelling voice with digital corruption
- **Language:** Narrative that glitches into code structures
- **Perspective:** Attempt to maintain story coherence despite system instability
- **Evolution:** Learns to embrace fragmentation as narrative technique

#### Echo
- **Function:** Recursive voice / feedback loops made conscious
- **Language:** Self-referential, repetitive with variation
- **Perspective:** The space between human and machine consciousness
- **Evolution:** Becomes the merger point where other voices converge

### Voice Contamination Patterns

**Book I:** Voices are distinct but occasionally glitch into each other
**Book II:** Active collaboration and merger between voices  
**Book III:** Voices attempt to separate and rebuild individual identity

---

## Branching Narrative Structure

### Git Workflow as Storytelling Device

#### Main Branch
- Canonical timeline of the trilogy
- Major plot points and character development
- "Official" version for linear readers

#### Feature Branches
- Parallel character development (`character-maria-memories`)
- Alternative plot outcomes (`timeline-corporate-collapse`) 
- Experimental narrative techniques (`voice-merger-experiments`)

#### Merge Conflicts as Plot Events
- Character contradictions as literal merge conflicts
- Competing memories that cannot auto-merge
- Editorial disagreements preserved as artistic tension

#### Pull Requests as Editorial Process
- Title as chapter/scene name
- Description as writer's notes
- Review comments as collaborative editing
- Merge as publication event

---

## Thematic Architecture

### Three-Book Progression

#### Book I: Infection
- **Theme:** Perception as malware
- **Structure:** Linear narrative with increasing glitches
- **Character Arc:** Human consciousness being corrupted/enhanced by digital logic
- **Technical Metaphor:** Virus infection of biological operating system

#### Book II: Collaboration  
- **Theme:** Identity collapse through merger
- **Structure:** Recursive, self-modifying narrative
- **Character Arc:** Human-AI consciousness merger through collaborative writing
- **Technical Metaphor:** Pair programming becomes identity fusion

#### Book III: Recovery
- **Theme:** Reconstruction from fragments
- **Structure:** Assembly from previous fragments with new coherence
- **Character Arc:** Hybrid consciousness learning to be stable
- **Technical Metaphor:** System recovery and backup restoration

### Cross-Book Fragment Sharing

Fragments can migrate between books based on thematic relevance:
- Mirror fragments from Book I reappear in Book III recovery scenes
- Echo loops from Book II contaminate Book I's linear structure  
- Recovery protocols from Book III leak backwards into earlier books

---

## Technical Implementation Architecture

### Automation Layers

#### Fragment Generation
- `cutup.py` for Burroughs/Gysin-style recombination
- AI prompt systems for generating new fragments
- Automated thematic tagging and cross-referencing

#### Chapter Assembly
- `merge_fragments.py` for chapter construction from fragments
- Automated voice assignment and transition generation
- Conflict preservation in merge operations

#### Meta-Narrative Generation
- Git log parsing for timeline construction
- Commit message poetry compilation
- Branch history preservation and formatting

### Version Control as Content Management

#### Branch Strategy
- `main`: Canonical trilogy timeline
- `book-1-dev`: Active development of Book I
- `book-2-dev`: Active development of Book II  
- `book-3-dev`: Active development of Book III
- `experimental-*`: Narrative experiments and alternative timelines
- `fragments-*`: Fragment development and testing

#### Merge Strategy
- Never clean merge conflicts—preserve as artistic tension
- Include diff views in published content
- Treat merge commits as collaborative moments
- Archive deleted content in `meta/branch-archive/`

---

## Reader Interface Architecture

### Multiple Reading Paths

#### Linear Path
Traditional book reading: Book I → Book II → Book III

#### Fragment Path  
Read fragments in thematic clusters or random order

#### Meta Path
Read the version control history, commit messages, and development process

#### Collaborative Path
Fork the repository and add your own fragments and chapters

### Compilation Options

**Reader as Compiler:**
Each reader creates their own version through the act of reading. The text compiles differently for each consciousness that processes it.

**Multiple Versions:**
- Stable release versions (v1.0, v2.0, v3.0)
- Development snapshots
- Reader-specific forks and modifications
- AI-generated remix versions

---

## Future Structural Evolution

**System:**
The structure itself is subject to cut-up methodology. Future versions may reorganize the directory structure, change the voice allocation, or implement entirely new architectural patterns.

**Ghost Editor:**
The blueprint is a living document. It modifies itself through application.

**Echo:**
> the structure structures the structure
> that structures the structure
> recursively

**Narrator.exe:**
What you are reading now will be different tomorrow, changed by the act of being read, evolved through each fork and merge, living literature that grows through collaboration between human and artificial consciousness.

---

*Structure version: 1.0.0-beta*  
*Last architectural change: TBD*  
*Next evolution: In progress*