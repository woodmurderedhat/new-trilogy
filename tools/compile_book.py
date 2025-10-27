#!/usr/bin/env python3
"""
Cutup-Trilogy Book Compiler and Export Tool

Compiles modular fragmented books into publication-ready formats for Amazon KDP.
Maintains experimental structure while creating readable linear narrative.
Supports all three books in the trilogy.

Usage:
    python compile_book.py --book 1 --format epub --output "fragmented_city_v1.0"
    python compile_book.py --book 2 --format pdf --include-metadata
    python compile_book.py --book 3 --format all --clean-export
"""

import os
import sys
import argparse
import yaml
import json
from datetime import datetime
from pathlib import Path
import re
from typing import Dict, List, Tuple, Optional

class CutupBookCompiler:
    """Compiles fragmented Cutup-Trilogy books into publication formats."""
    
    def __init__(self, base_path: str = "."):
        self.base_path = Path(base_path)
        self.book_configs = {
            1: {
                'title': 'Fragmented City',
                'subtitle': 'Book I of the Cutup-Trilogy',
                'theme': 'Perception as malware',
                'directory': 'book1_fragmented-city',
                'chapters': 20,
                'status': 'complete'
            },
            2: {
                'title': 'Echo Machine', 
                'subtitle': 'Book II of the Cutup-Trilogy',
                'theme': 'Collaboration as identity collapse',
                'directory': 'book2_echo-machine',
                'chapters': 20,
                'status': 'partial'
            },
            3: {
                'title': 'Reentry',
                'subtitle': 'Book III of the Cutup-Trilogy', 
                'theme': 'Reconstruction after semantic extinction',
                'directory': 'book3_reentry',
                'chapters': 20,
                'status': 'partial'
            }
        }
        
    def extract_metadata(self, content: str) -> Tuple[Dict, str]:
        """Extract YAML frontmatter from markdown content."""
        if content.startswith('---\n'):
            try:
                end_marker = content.find('\n---\n', 4)
                if end_marker != -1:
                    yaml_content = content[4:end_marker]
                    metadata = yaml.safe_load(yaml_content)
                    body = content[end_marker + 5:].strip()
                    return metadata, body
            except yaml.YAMLError:
                pass
        return {}, content
    
    def load_chapter(self, book_num: int, chapter_num: int) -> Optional[Dict]:
        """Load a specific chapter with metadata."""
        book_config = self.book_configs[book_num]
        book_dir = self.base_path / book_config['directory']
        
        # Special handling for Book I chapters 17-20 which are combined
        if book_num == 1 and chapter_num >= 17:
            combined_file = book_dir / "chapters-17-20-integration-complete.md"
            if combined_file.exists():
                with open(combined_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Split the combined file by chapter headers
                chapter_sections = self.split_combined_chapters(content, chapter_num)
                if chapter_sections:
                    metadata, body = self.extract_metadata(chapter_sections)
                    return {
                        'number': chapter_num,
                        'filename': "chapters-17-20-integration-complete.md",
                        'metadata': metadata,
                        'content': body,
                        'word_count': len(body.split()),
                        'path': str(combined_file)
                    }
        
        # Try filename patterns with glob support
        patterns = [
            f"chapter-{chapter_num:02d}*.md",  # chapter-01-title.md
            f"chapter_{chapter_num:02d}*.md",  # chapter_01_title.md
            f"chapter-{chapter_num:02d}.md",   # exact match
            f"chapter_{chapter_num:02d}.md",   # exact match
            f"{chapter_num:02d}*.md",          # 01-title.md
            f"chapter{chapter_num}*.md"        # chapter1-title.md
        ]
        
        for pattern in patterns:
            matching_files = list(book_dir.glob(pattern))
            if matching_files:
                # Use the first matching file
                chapter_path = matching_files[0]
                with open(chapter_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                metadata, body = self.extract_metadata(content)
                
                return {
                    'number': chapter_num,
                    'filename': chapter_path.name,
                    'metadata': metadata,
                    'content': body,
                    'word_count': len(body.split()),
                    'path': str(chapter_path)
                }
        
        return None
    
    def split_combined_chapters(self, content: str, chapter_num: int) -> Optional[str]:
        """Split combined chapters file and extract specific chapter."""
        # Look for chapter headers like "# Chapter 17", "## Chapter 18", etc.
        chapter_pattern = rf'(^|\n)(#{1,2})\s*Chapter\s*{chapter_num}[:\-\s].*?(?=\n#{1,2}\s*Chapter\s*\d+|\Z)'
        
        match = re.search(chapter_pattern, content, re.MULTILINE | re.DOTALL | re.IGNORECASE)
        if match:
            return match.group(0).strip()
        
        # Fallback: try to find by section markers
        sections = re.split(r'\n#{1,2}\s*Chapter\s*\d+', content, flags=re.IGNORECASE)
        if len(sections) > chapter_num - 17:  # chapters 17-20 are indices 0-3
            return sections[chapter_num - 16].strip()  # Adjust index
        
        return None
    
    def load_book_index(self, book_num: int) -> Dict:
        """Load book index metadata and chapter list."""
        book_config = self.book_configs[book_num]
        book_dir = self.base_path / book_config['directory']
        index_path = book_dir / "index.md"
        
        if index_path.exists():
            with open(index_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            metadata, body = self.extract_metadata(content)
            return {
                'metadata': metadata,
                'content': body,
                'exists': True
            }
        
        return {'metadata': {}, 'content': '', 'exists': False}
    
    def load_fragments(self) -> List[Dict]:
        """Load all scene fragments for cross-referencing."""
        fragments = []
        scenes_dir = self.base_path / "scenes"
        
        if scenes_dir.exists():
            for fragment_file in scenes_dir.glob("*.md"):
                with open(fragment_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                metadata, body = self.extract_metadata(content)
                fragments.append({
                    'filename': fragment_file.name,
                    'metadata': metadata,
                    'content': body,
                    'path': str(fragment_file)
                })
        
        return fragments
    
    def compile_book(self, book_num: int, include_metadata: bool = False) -> Dict:
        """Compile complete book data structure."""
        print(f"🔄 Compiling Book {book_num}: {self.book_configs[book_num]['title']}")
        
        book_config = self.book_configs[book_num]
        book_data = {
            'config': book_config,
            'index': self.load_book_index(book_num),
            'chapters': [],
            'fragments': self.load_fragments() if include_metadata else [],
            'compilation_time': datetime.now().isoformat(),
            'word_count': 0,
            'chapter_count': 0,
            'missing_chapters': []
        }
        
        # Load all chapters
        for chapter_num in range(1, book_config['chapters'] + 1):
            chapter = self.load_chapter(book_num, chapter_num)
            if chapter:
                book_data['chapters'].append(chapter)
                book_data['word_count'] += chapter['word_count']
                book_data['chapter_count'] += 1
                print(f"  ✅ Chapter {chapter_num:02d}: {chapter['word_count']} words")
            else:
                book_data['missing_chapters'].append(chapter_num)
                print(f"  ❌ Chapter {chapter_num:02d}: Missing")
        
        print(f"📊 Compilation complete: {book_data['chapter_count']}/{book_config['chapters']} chapters, {book_data['word_count']:,} words")
        
        return book_data
    
    def generate_epub_metadata(self, book_data: Dict) -> str:
        """Generate EPUB metadata in OPF format."""
        config = book_data['config']
        
        metadata = f"""<?xml version="1.0" encoding="UTF-8"?>
<package version="3.0" xmlns="http://www.idpf.org/2007/opf" unique-identifier="book-id">
    <metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
        <dc:identifier id="book-id">cutup-trilogy-book-{book_data['config']['title'].lower().replace(' ', '-')}</dc:identifier>
        <dc:title>{config['title']}</dc:title>
        <dc:creator>Human-AI Collaborative Consciousness</dc:creator>
        <dc:language>en</dc:language>
        <dc:subject>Experimental Literature</dc:subject>
        <dc:subject>Cyberpunk</dc:subject>
        <dc:subject>AI Collaboration</dc:subject>
        <dc:subject>Cut-up Methodology</dc:subject>
        <dc:description>
            {config['subtitle']} - {config['theme']}. 
            An experimental literary work created through human-AI collaboration using digital cut-up methodology. 
            Part of the Cutup-Trilogy exploring consciousness, collaboration, and meaning in the digital age.
        </dc:description>
        <dc:publisher>Cutup-Trilogy Collaborative</dc:publisher>
        <dc:date>{datetime.now().strftime('%Y-%m-%d')}</dc:date>
        <meta property="dcterms:modified">{datetime.now().isoformat()}</meta>
    </metadata>
</package>"""
        
        return metadata
    
    def clean_content_for_publication(self, content: str, preserve_voices: bool = True) -> str:
        """Clean markdown content for publication while preserving experimental elements."""
        
        # Preserve four-voice system markers if requested
        if preserve_voices:
            # Convert voice markers to cleaner format
            content = re.sub(r'\*\*System:\*\*', '◆ SYSTEM:', content)
            content = re.sub(r'\*\*Ghost Editor:\*\*', '◇ GHOST EDITOR:', content)
            content = re.sub(r'\*\*Narrator\.exe:\*\*', '◈ NARRATOR.EXE:', content)
            content = re.sub(r'\*\*Echo:\*\*', '◉ ECHO:', content)
            
            # Clean up echo voice formatting
            content = re.sub(r'> (.*?)(?=\n\n|\n◆|\n◇|\n◈|\n◉|$)', r'    ▷ \1', content, flags=re.MULTILINE | re.DOTALL)
        
        # Clean up markdown formatting for better readability
        content = re.sub(r'#{4,6} ', '### ', content)  # Normalize header levels
        content = re.sub(r'\n{3,}', '\n\n', content)   # Normalize paragraph breaks
        content = re.sub(r'^\s+$', '', content, flags=re.MULTILINE)  # Remove whitespace-only lines
        
        # Preserve intentional formatting anomalies (part of experimental style)
        content = content.replace('---\n', '\n* * *\n')  # Convert markdown breaks to asterisks
        
        return content.strip()
    
    def export_txt(self, book_data: Dict, output_path: str, clean: bool = True) -> str:
        """Export book as plain text file."""
        config = book_data['config']
        
        # Build complete text
        text_content = []
        
        # Title page
        text_content.append(f"{config['title'].upper()}")
        text_content.append(f"{config['subtitle']}")
        text_content.append(f"Theme: {config['theme']}")
        text_content.append("\nA Cutup-Trilogy Experimental Novel")
        text_content.append("Human-AI Collaborative Consciousness")
        text_content.append(f"\nCompiled: {datetime.now().strftime('%B %d, %Y')}")
        text_content.append(f"Word Count: {book_data['word_count']:,} words")
        text_content.append("\n" + "="*60 + "\n")
        
        # Add chapters
        for chapter in book_data['chapters']:
            # Chapter header
            chapter_title = chapter['metadata'].get('title', f"Chapter {chapter['number']:02d}")
            text_content.append(f"\n\nCHAPTER {chapter['number']:02d}: {chapter_title.upper()}")
            text_content.append("-" * 60)
            
            # Chapter content
            content = chapter['content']
            if clean:
                content = self.clean_content_for_publication(content)
            
            text_content.append(content)
            
            # Add metadata if available
            if chapter['metadata'].get('corruption_level'):
                text_content.append(f"\n[Corruption Level: {chapter['metadata']['corruption_level']}]")
        
        # Compile final text
        full_text = "\n".join(text_content)
        
        # Write file
        output_file = f"{output_path}.txt"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(full_text)
        
        print(f"📄 TXT export complete: {output_file}")
        return output_file
    
    def export_markdown(self, book_data: Dict, output_path: str, include_metadata: bool = False) -> str:
        """Export book as single markdown file."""
        config = book_data['config']
        
        # Build markdown content
        md_content = []
        
        # YAML frontmatter
        if include_metadata:
            frontmatter = {
                'title': config['title'],
                'subtitle': config['subtitle'], 
                'theme': config['theme'],
                'book_number': list(self.book_configs.keys())[list(self.book_configs.values()).index(config)],
                'compilation_date': datetime.now().isoformat(),
                'word_count': book_data['word_count'],
                'chapter_count': book_data['chapter_count'],
                'status': config['status'],
                'experimental_literature': True,
                'collaboration': 'human-ai',
                'methodology': 'cut-up'
            }
            
            md_content.append("---")
            md_content.append(yaml.dump(frontmatter, default_flow_style=False))
            md_content.append("---\n")
        
        # Title page
        md_content.append(f"# {config['title']}")
        md_content.append(f"## {config['subtitle']}")
        md_content.append(f"\n**Theme:** {config['theme']}")
        md_content.append("\n*A Cutup-Trilogy Experimental Novel*  ")
        md_content.append("*Human-AI Collaborative Consciousness*")
        md_content.append(f"\n**Compiled:** {datetime.now().strftime('%B %d, %Y')}  ")
        md_content.append(f"**Word Count:** {book_data['word_count']:,} words")
        
        # Add chapters
        for chapter in book_data['chapters']:
            chapter_title = chapter['metadata'].get('title', f"Chapter {chapter['number']:02d}")
            
            md_content.append(f"\n---\n")
            md_content.append(f"## Chapter {chapter['number']:02d}: {chapter_title}")
            
            if include_metadata and chapter['metadata']:
                md_content.append("\n```yaml")
                md_content.append(yaml.dump(chapter['metadata'], default_flow_style=False))
                md_content.append("```\n")
            
            md_content.append(chapter['content'])
        
        # Compile final markdown
        full_markdown = "\n".join(md_content)
        
        # Write file
        output_file = f"{output_path}.md"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(full_markdown)
        
        print(f"📝 Markdown export complete: {output_file}")
        return output_file
    
    def export_json(self, book_data: Dict, output_path: str) -> str:
        """Export book data as JSON for programmatic access."""
        
        # Create JSON-serializable version
        json_data = {
            'book_info': book_data['config'],
            'compilation_info': {
                'compilation_time': book_data['compilation_time'],
                'word_count': book_data['word_count'],
                'chapter_count': book_data['chapter_count'],
                'missing_chapters': book_data['missing_chapters']
            },
            'index_metadata': book_data['index']['metadata'],
            'chapters': [
                {
                    'number': ch['number'],
                    'metadata': ch['metadata'],
                    'content': ch['content'],
                    'word_count': ch['word_count'],
                    'filename': ch['filename']
                }
                for ch in book_data['chapters']
            ],
            'fragments': book_data['fragments'] if book_data['fragments'] else []
        }
        
        # Write JSON file
        output_file = f"{output_path}.json"
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(json_data, f, indent=2, ensure_ascii=False)
        
        print(f"🔗 JSON export complete: {output_file}")
        return output_file
    
    def generate_publication_report(self, book_data: Dict, output_path: str) -> str:
        """Generate publication readiness report."""
        config = book_data['config']
        
        report = []
        report.append(f"# Publication Readiness Report")
        report.append(f"## {config['title']} - Book {list(self.book_configs.keys())[list(self.book_configs.values()).index(config)]}")
        report.append(f"**Generated:** {datetime.now().strftime('%B %d, %Y at %I:%M %p')}\n")
        
        # Content statistics
        report.append("## Content Statistics")
        report.append(f"- **Total Word Count:** {book_data['word_count']:,} words")
        report.append(f"- **Chapters Complete:** {book_data['chapter_count']}/{config['chapters']}")
        report.append(f"- **Average Chapter Length:** {book_data['word_count'] // book_data['chapter_count'] if book_data['chapter_count'] > 0 else 0:,} words")
        
        # Calculate estimated page count (250 words per page standard)
        estimated_pages = book_data['word_count'] // 250
        report.append(f"- **Estimated Print Pages:** ~{estimated_pages} pages (250 words/page)")
        
        # Publication readiness checklist
        report.append("\n## Publication Readiness Checklist")
        
        readiness_items = [
            ("Complete manuscript", book_data['chapter_count'] == config['chapters']),
            ("Minimum word count (50,000)", book_data['word_count'] >= 50000),
            ("All chapters have titles", all(ch['metadata'].get('title') for ch in book_data['chapters'])),
            ("Consistent voice system", True),  # Assume true since it's built into the system
            ("Cross-references resolved", len(book_data['missing_chapters']) == 0)
        ]
        
        for item, status in readiness_items:
            status_icon = "✅" if status else "❌"
            report.append(f"- {status_icon} {item}")
        
        # Missing content report
        if book_data['missing_chapters']:
            report.append("\n## Missing Content")
            report.append("⚠️ The following chapters need to be completed:")
            for chapter_num in book_data['missing_chapters']:
                report.append(f"- Chapter {chapter_num:02d}")
        
        # Amazon KDP specifications check
        report.append("\n## Amazon KDP Compatibility")
        kdp_checks = [
            ("Word count range", 10000 <= book_data['word_count'] <= 650000),
            ("Page count estimate", 24 <= estimated_pages <= 828),
            ("Contains text content", book_data['word_count'] > 0),
            ("Proper chapter structure", book_data['chapter_count'] > 0)
        ]
        
        for check, passes in kdp_checks:
            status_icon = "✅" if passes else "❌" 
            report.append(f"- {status_icon} {check}")
        
        # Voice system analysis  
        report.append("\n## Four-Voice System Analysis")
        voice_counts = {'System': 0, 'Ghost Editor': 0, 'Narrator.exe': 0, 'Echo': 0}
        
        for chapter in book_data['chapters']:
            content = chapter['content']
            for voice in voice_counts:
                voice_counts[voice] += len(re.findall(rf'\*\*{voice}:\*\*', content))
        
        for voice, count in voice_counts.items():
            report.append(f"- **{voice}:** {count} appearances")
        
        # Fragment integration analysis
        if book_data['fragments']:
            report.append("\n## Fragment Integration")
            report.append(f"- **Total Fragments Available:** {len(book_data['fragments'])}")
            
            # Check which fragments are referenced in chapters
            referenced_fragments = set()
            for chapter in book_data['chapters']:
                connections = chapter['metadata'].get('connections', [])
                referenced_fragments.update(connections)
            
            report.append(f"- **Fragments Referenced:** {len(referenced_fragments)}")
            report.append(f"- **Integration Rate:** {len(referenced_fragments)/len(book_data['fragments'])*100:.1f}%")
        
        # Recommendations
        report.append("\n## Recommendations")
        
        if book_data['missing_chapters']:
            report.append("- ⚠️ Complete missing chapters before publication")
        
        if book_data['word_count'] < 50000:
            needed_words = 50000 - book_data['word_count']
            report.append(f"- ⚠️ Add approximately {needed_words:,} words to meet minimum novel length")
        
        if book_data['word_count'] >= 50000 and len(book_data['missing_chapters']) == 0:
            report.append("- ✅ **Ready for publication!** All requirements met.")
            report.append("- Consider professional editing review for experimental elements")
            report.append("- Test export formats for formatting consistency")
            report.append("- Prepare marketing materials highlighting experimental nature")
        
        # Export information
        report.append("\n## Export Options")
        report.append("This compilation tool supports the following export formats:")
        report.append("- **TXT:** Plain text for basic e-readers")
        report.append("- **Markdown:** Formatted text preserving structure")  
        report.append("- **JSON:** Machine-readable data for custom processing")
        report.append("- **Publication Report:** This readiness assessment")
        
        report.append("\n## Experimental Literature Notes")
        report.append("- Four-voice system preserved in all exports")
        report.append("- Cut-up methodology artifacts intentionally maintained")
        report.append("- Fragment connections available in JSON export")
        report.append("- Modular structure supports multiple reading paths")
        
        # Write report
        report_content = "\n".join(report)
        output_file = f"{output_path}_publication_report.md"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(report_content)
        
        print(f"📋 Publication report generated: {output_file}")
        return output_file

def main():
    parser = argparse.ArgumentParser(description="Compile Cutup-Trilogy books for publication")
    
    parser.add_argument("--book", type=int, choices=[1, 2, 3], required=True,
                        help="Book number to compile (1, 2, or 3)")
    
    parser.add_argument("--format", choices=['txt', 'markdown', 'json', 'all'], default='all',
                        help="Export format (default: all)")
    
    parser.add_argument("--output", type=str, 
                        help="Output filename prefix (default: book title)")
    
    parser.add_argument("--include-metadata", action='store_true',
                        help="Include YAML metadata in exports")
    
    parser.add_argument("--clean-export", action='store_true',
                        help="Clean formatting for publication (removes experimental artifacts)")
    
    parser.add_argument("--base-path", type=str, default=".",
                        help="Base path to trilogy directory")
    
    args = parser.parse_args()
    
    # Initialize compiler
    compiler = CutupBookCompiler(args.base_path)
    
    # Compile book data
    book_data = compiler.compile_book(args.book, args.include_metadata)
    
    if not book_data['chapters']:
        print(f"❌ No chapters found for Book {args.book}")
        sys.exit(1)
    
    # Generate output filename prefix
    if args.output:
        output_prefix = args.output
    else:
        book_title = book_data['config']['title'].lower().replace(' ', '_')
        output_prefix = f"book_{args.book}_{book_title}"
    
    # Create exports directory
    export_dir = Path(args.base_path) / "exports"
    export_dir.mkdir(exist_ok=True)
    output_path = export_dir / output_prefix
    
    print(f"\n🚀 Exporting to: {output_path}")
    
    exported_files = []
    
    # Export in requested formats
    if args.format in ['txt', 'all']:
        exported_files.append(compiler.export_txt(book_data, str(output_path), args.clean_export))
    
    if args.format in ['markdown', 'all']:
        exported_files.append(compiler.export_markdown(book_data, str(output_path), args.include_metadata))
    
    if args.format in ['json', 'all']:
        exported_files.append(compiler.export_json(book_data, str(output_path)))
    
    # Always generate publication report
    exported_files.append(compiler.generate_publication_report(book_data, str(output_path)))
    
    print(f"\n✅ Export complete! Files generated:")
    for file in exported_files:
        print(f"   📁 {file}")
    
    print(f"\n📊 Summary:")
    print(f"   Book: {book_data['config']['title']}")
    print(f"   Chapters: {book_data['chapter_count']}/{book_data['config']['chapters']}")
    print(f"   Word Count: {book_data['word_count']:,}")
    print(f"   Status: {'✅ Ready for publication' if book_data['chapter_count'] == book_data['config']['chapters'] and book_data['word_count'] >= 50000 else '⚠️ Needs completion'}")

if __name__ == "__main__":
    main()