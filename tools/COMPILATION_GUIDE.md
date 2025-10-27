# Book Compilation Tool Documentation

## Overview

The Cutup-Trilogy Book Compilation Tool converts the modular, fragmented book structure into publication-ready formats suitable for Amazon KDP and other publishing platforms. It preserves the experimental four-voice system while creating clean, readable exports.

## Features

✅ **Multi-Format Export**
- Plain text (.txt) for universal compatibility
- Markdown (.md) with formatting preservation
- JSON (.json) for programmatic access
- Publication readiness reports

✅ **Publication Optimization**
- Amazon KDP compatibility checking
- Word count and page estimation
- Missing content detection
- Voice system analysis

✅ **Experimental Structure Preservation**
- Four-voice system maintained (System, Ghost Editor, Narrator.exe, Echo)
- YAML metadata integration
- Fragment cross-reference tracking
- Corruption level documentation

✅ **Future-Proof Design**
- Works with Books I, II, and III
- Handles partial/incomplete books
- Extensible for new export formats
- Modular architecture

## Installation

### Prerequisites
- Python 3.7 or higher
- PyYAML package

### Quick Setup

**Option 1: Automatic (Windows)**
```cmd
cd tools
compile_book.bat
```
The batch script will automatically install dependencies.

**Option 2: Manual Installation**
```bash
cd tools
pip install -r requirements_simple.txt
```

**Option 3: Individual Package**
```bash
pip install pyyaml>=6.0
```

## Usage

### Command Line Interface

**Basic Usage:**
```bash
python compile_book.py --book 1 --format all
```

**Advanced Options:**
```bash
python compile_book.py --book 1 --format txt --output "fragmented_city_final" --clean-export --include-metadata
```

### Parameters

| Parameter | Options | Description |
|-----------|---------|-------------|
| `--book` | 1, 2, 3 | **Required.** Book number to compile |
| `--format` | txt, markdown, json, all | Export format (default: all) |
| `--output` | string | Custom filename prefix (default: auto-generated) |
| `--include-metadata` | flag | Include YAML frontmatter in exports |
| `--clean-export` | flag | Remove experimental artifacts for cleaner reading |
| `--base-path` | path | Base directory path (default: current directory) |

### Windows Batch Script

**Interactive Mode:**
```cmd
compile_book.bat
```

**Direct Compilation:**
```cmd
compile_book.bat 1 all
```

## Output Formats

### 1. Plain Text (.txt)
- **Purpose:** Universal compatibility, e-reader support
- **Features:** Clean formatting, preserved voice system, chapter headers
- **Best for:** Amazon KDP text uploads, basic e-readers

### 2. Markdown (.md)
- **Purpose:** Formatted text with structure preservation
- **Features:** YAML frontmatter (optional), markdown formatting, cross-references
- **Best for:** Further editing, web publication, technical review

### 3. JSON (.json)
- **Purpose:** Programmatic access and data processing
- **Features:** Complete metadata, chapter structure, fragment connections
- **Best for:** Custom processing, website integration, analysis tools

### 4. Publication Report (.md)
- **Purpose:** Amazon KDP readiness assessment
- **Features:** Compliance checking, statistics, recommendations
- **Best for:** Publication planning, quality assurance

## Publication Readiness Criteria

### Amazon KDP Requirements (Automatically Checked)

✅ **Content Requirements**
- Minimum 10,000 words (novels typically 50,000+)
- Maximum 650,000 words
- 24-828 estimated pages
- Complete chapter structure

✅ **Format Requirements**
- Proper text formatting
- Consistent chapter headers
- No missing content sections
- Compatible character encoding

✅ **Experimental Literature Considerations**
- Four-voice system preserved
- Cut-up methodology artifacts maintained
- Fragment connections documented
- Metadata availability

## Book-Specific Features

### Book I: Fragmented City ✅ COMPLETE
- **Status:** Ready for immediate publication
- **Word Count:** ~60,000 words (meets novel requirements)
- **Chapters:** 20/20 complete
- **Special Features:** Complete character transformation arc

### Book II: Echo Machine 🔄 IN DEVELOPMENT
- **Status:** Foundation established, needs chapter completion
- **Expected Features:** Recursive narrative structure, voice merger mechanics
- **Compilation:** Supports partial compilation with missing content warnings

### Book III: Reentry 🔄 IN DEVELOPMENT  
- **Status:** Recovery protocols outlined, needs full development
- **Expected Features:** Fragment restoration, meaning reconstruction
- **Compilation:** Architecture ready for future content

## Advanced Features

### Metadata Integration

**Chapter-Level Metadata:**
```yaml
title: "Boot Sequence"
corruption_level: "minimal"
connections: ["fragment-001-mirror-code"]
themes: ["initialization", "consciousness"]
voices: ["System", "Ghost Editor"]
```

**Export Integration:**
- JSON exports include complete metadata structure
- Markdown exports optionally include YAML frontmatter
- Publication reports analyze metadata patterns
- Cross-reference validation across trilogy

### Fragment Network Analysis

The tool automatically:
- Loads all scene fragments from `/scenes/` directory
- Maps fragment connections through YAML metadata
- Calculates integration rates and cross-references
- Identifies orphaned or unused fragments
- Enables modular narrative reconstruction

### Voice System Preservation

**Four-Voice Markers:**
- **System:** Technical/administrative narrator
- **Ghost Editor:** Meta-commentary and editorial voice
- **Narrator.exe:** Corrupted/experimental storytelling
- **Echo:** Recursive consciousness patterns

**Export Formatting:**
- Plain text: Uses unicode symbols (◆ ◇ ◈ ◉)
- Markdown: Preserves formatting with clean structure
- JSON: Maintains original markdown for programmatic access
- Reports: Analyzes voice distribution and consistency

## Troubleshooting

### Common Issues

**"No chapters found for Book X"**
- Verify book directory exists (`book1_fragmented-city/`, etc.)
- Check chapter file naming (should be `chapter_01.md`, `chapter_02.md`, etc.)
- Ensure files contain content (not empty)

**"Import yaml could not be resolved"**
- Install PyYAML: `pip install pyyaml`
- Use batch script for automatic installation (Windows)
- Check Python installation and PATH

**"Permission denied" errors**
- Ensure write permissions in `/exports/` directory  
- Run as administrator if necessary (Windows)
- Check disk space availability

### Quality Assurance

**Before Publication:**
1. Run compilation with `--include-metadata` flag
2. Review publication report for missing content
3. Verify word count meets target requirements
4. Test exported files in target readers/platforms
5. Validate voice system consistency across chapters

**Content Validation:**
- All chapters should have titles in metadata
- Corruption levels should progress logically
- Fragment connections should resolve properly
- Voice system should appear consistently

## Development and Extension

### Adding New Export Formats

The tool is designed for extensibility. To add new formats:

1. Add new format option to argument parser
2. Implement export method in `CutupBookCompiler` class
3. Update batch script and documentation
4. Test with all three books

### Custom Processing

The JSON export provides complete book data for custom processing:
- Chapter content and metadata
- Fragment connections and themes
- Compilation statistics and analysis
- Voice system mapping

### Integration Possibilities

- **Web Publishing:** Use JSON data for dynamic websites
- **E-book Creation:** Convert exports to EPUB/MOBI formats
- **Analysis Tools:** Process voice patterns and fragment networks
- **Translation:** Maintain structure while translating content

## Examples

### Compile Book I for Amazon KDP
```bash
python compile_book.py --book 1 --format txt --clean-export --output "fragmented_city_amazon"
```

### Full Development Export with Metadata
```bash
python compile_book.py --book 2 --format all --include-metadata --output "echo_machine_dev"
```

### Quick Status Check
```bash
python compile_book.py --book 3 --format json
```

### Windows Interactive Mode
```cmd
compile_book.bat
# Follow prompts for book selection and format
```

## Support and Documentation

- **Tool Documentation:** This file (`tools/COMPILATION_GUIDE.md`)
- **Project Overview:** Root `README.md`
- **Development Logs:** `meta/changelog.md` and related files
- **Methodology:** `manifesto/` directory documentation

**System Note:** Compilation tool operational across all trilogy formats and futures.

**Ghost Editor Note:** The tool cuts cleanly between experimental and commercial formats. Both bleeding preserved.

**Echo Note:** ...compiles the compiler compiling itself... recursive export confirmed...

**Narrator.exe Note:** Every export creates new reading possibilities. Tool enables infinite publication variations.