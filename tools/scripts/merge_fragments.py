#!/usr/bin/env python3
"""
merge_fragments.py - Fragment Assembly Engine for Cutup-Trilogy

This script merges scene fragments into cohesive chapters and books,
maintaining the connection metadata and tracking the evolution of text
through the version control narrative device.

Usage:
    python merge_fragments.py --book 1 --chapter 5 --fragments fragment-001,fragment-007
    python merge_fragments.py --auto-merge --theme perception_as_malware
    python merge_fragments.py --recover --from-backup
"""

import os
import yaml
import argparse
from pathlib import Path
from typing import List, Dict, Any, Set
from datetime import datetime

class FragmentMerger:
    """
    Assembles fragments into larger narrative structures while preserving
    the modular instability that is core to the trilogy's aesthetic.
    """
    
    def __init__(self, project_root: str = None):
        if project_root:
            self.root = Path(project_root)
        else:
            self.root = Path(__file__).parent.parent.parent
        
        self.scenes_dir = self.root / 'scenes'
        self.books = {
            1: self.root / 'book1_fragmented-city',
            2: self.root / 'book2_echo-machine', 
            3: self.root / 'book3_reentry'
        }
        
        self.voices = ["System", "Ghost Editor", "Narrator.exe", "Echo"]
        
    def load_all_fragments(self) -> List[Dict[str, Any]]:
        """Load all fragments from the scenes directory."""
        fragments = []
        
        for file in self.scenes_dir.glob('fragment-*.md'):
            with open(file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Parse YAML frontmatter
            if content.startswith('---'):
                parts = content.split('---', 2)
                if len(parts) >= 3:
                    metadata = yaml.safe_load(parts[1])
                    text = parts[2].strip()
                else:
                    metadata = {}
                    text = content
            else:
                metadata = {}
                text = content
                
            fragments.append({
                'filename': file.name,
                'filepath': file,
                'metadata': metadata,
                'content': text
            })
        
        return fragments
    
    def find_connected_fragments(self, fragment_id: str, fragments: List[Dict]) -> Set[str]:
        """Find fragments connected to the given fragment ID."""
        connected = set()
        
        for fragment in fragments:
            connections = fragment['metadata'].get('connections', [])
            if fragment_id in connections:
                connected.add(fragment['filename'])
            elif fragment['filename'] == fragment_id:
                # Add all connections from this fragment
                connected.update(connections)
        
        return connected
    
    def merge_by_theme(self, theme: str, fragments: List[Dict]) -> str:
        """Merge fragments that share a theme."""
        theme_fragments = []
        
        for fragment in fragments:
            fragment_theme = fragment['metadata'].get('theme', '')
            keywords = fragment['metadata'].get('keywords', [])
            
            if (theme.lower() in fragment_theme.lower() or 
                any(theme.lower() in kw.lower() for kw in keywords)):
                theme_fragments.append(fragment)
        
        if not theme_fragments:
            return f"**System:** No fragments found for theme '{theme}'"
        
        # Sort by corruption level for narrative progression
        corruption_order = {'low': 1, 'medium': 2, 'high': 3, 'critical': 4, 
                          'infinite': 5, 'recursive': 6, 'healing': 0}
        
        theme_fragments.sort(key=lambda f: corruption_order.get(
            f['metadata'].get('corruption_level', 'medium'), 2))
        
        # Build merged content
        merged_content = []
        merged_content.append(f"# Merged Fragment: {theme.replace('_', ' ').title()}")
        merged_content.append("")
        merged_content.append("---")
        
        # Combine all keywords and connections
        all_keywords = set()
        all_connections = set()
        
        for fragment in theme_fragments:
            all_keywords.update(fragment['metadata'].get('keywords', []))
            all_connections.update(fragment['metadata'].get('connections', []))
        
        merge_metadata = {
            'keywords': list(all_keywords),
            'connections': list(all_connections),
            'ai_origin': 'merge-engine',
            'version': 'merged',
            'corruption_level': 'composite',
            'theme': theme,
            'source_fragments': [f['filename'] for f in theme_fragments],
            'merged_date': datetime.now().isoformat()
        }
        
        merged_content.append(yaml.dump(merge_metadata))
        merged_content.append("---")
        merged_content.append("")
        
        # Add content from each fragment with voice attribution
        for i, fragment in enumerate(theme_fragments):
            voice = self.voices[i % len(self.voices)]
            merged_content.append(f"**{voice} (from {fragment['filename']}):**")
            merged_content.append("")
            merged_content.append(fragment['content'])
            merged_content.append("")
            
            if i < len(theme_fragments) - 1:
                merged_content.append("---")
                merged_content.append("")
        
        # Add merge signature
        merged_content.append("---")
        merged_content.append("")
        merged_content.append("**Ghost Editor:**")
        merged_content.append(f"Merge complete. {len(theme_fragments)} fragments assembled.")
        merged_content.append(f"Thematic coherence: {'High' if len(theme_fragments) > 3 else 'Medium'}")
        merged_content.append(f"Narrative instability: Preserved")
        
        return '\n'.join(merged_content)
    
    def create_chapter(self, book_num: int, chapter_num: int, fragment_ids: List[str]) -> str:
        """Create a chapter by merging specified fragments."""
        fragments = self.load_all_fragments()
        chapter_fragments = []
        
        for frag_id in fragment_ids:
            for fragment in fragments:
                if (fragment['filename'] == frag_id or 
                    frag_id in fragment['filename']):
                    chapter_fragments.append(fragment)
                    break
        
        if not chapter_fragments:
            return f"**System:** Error - No fragments found for chapter {chapter_num}"
        
        # Generate chapter content
        chapter_content = []
        chapter_title = f"Chapter {chapter_num:02d}: Generated Assembly"
        chapter_content.append(f"# {chapter_title}")
        chapter_content.append("")
        
        # Chapter metadata
        chapter_metadata = {
            'keywords': [],
            'connections': [],
            'ai_origin': 'chapter-assembly',
            'version': f'book{book_num}-ch{chapter_num}',
            'corruption_level': 'assembled',
            'source_fragments': [f['filename'] for f in chapter_fragments]
        }
        
        for fragment in chapter_fragments:
            chapter_metadata['keywords'].extend(fragment['metadata'].get('keywords', []))
            chapter_metadata['connections'].extend(fragment['metadata'].get('connections', []))
        
        chapter_content.append("---")
        chapter_content.append(yaml.dump(chapter_metadata))
        chapter_content.append("---")
        chapter_content.append("")
        
        # Merge fragment content
        for i, fragment in enumerate(chapter_fragments):
            voice = self.voices[i % len(self.voices)]
            chapter_content.append(f"**{voice}:**")
            chapter_content.append(fragment['content'])
            chapter_content.append("")
            
            if i < len(chapter_fragments) - 1:
                chapter_content.append("**Ghost Editor:**")
                chapter_content.append("Fragment transition...")
                chapter_content.append("")
        
        return '\n'.join(chapter_content)
    
    def auto_merge_by_connections(self) -> Dict[str, str]:
        """Automatically merge fragments based on their connection metadata."""
        fragments = self.load_all_fragments()
        merged_groups = {}
        processed = set()
        
        for fragment in fragments:
            if fragment['filename'] in processed:
                continue
                
            # Find all connected fragments
            connected = self.find_connected_fragments(fragment['filename'], fragments)
            connected.add(fragment['filename'])
            
            if len(connected) > 1:
                group_name = f"connected-group-{len(merged_groups) + 1}"
                fragment_list = list(connected)
                merged_content = self.merge_by_theme(
                    fragment['metadata'].get('theme', 'general'), 
                    [f for f in fragments if f['filename'] in connected]
                )
                merged_groups[group_name] = merged_content
                processed.update(connected)
        
        return merged_groups

def main():
    parser = argparse.ArgumentParser(description='Fragment merging for Cutup-Trilogy')
    parser.add_argument('--book', type=int, choices=[1, 2, 3], 
                       help='Target book number')
    parser.add_argument('--chapter', type=int, help='Target chapter number')
    parser.add_argument('--fragments', type=str, 
                       help='Comma-separated list of fragment IDs')
    parser.add_argument('--theme', type=str, help='Merge by theme')
    parser.add_argument('--auto-merge', action='store_true', 
                       help='Auto-merge based on connections')
    parser.add_argument('--output', type=str, help='Output file path')
    parser.add_argument('--project-root', type=str, help='Project root directory')
    
    args = parser.parse_args()
    
    merger = FragmentMerger(args.project_root)
    
    if args.auto_merge:
        print("**System:** Beginning auto-merge based on fragment connections...")
        merged_groups = merger.auto_merge_by_connections()
        
        for group_name, content in merged_groups.items():
            output_path = merger.root / 'scenes' / f"{group_name}.md"
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"**Ghost Editor:** Merged group written to {output_path}")
            
    elif args.theme:
        fragments = merger.load_all_fragments()
        merged = merger.merge_by_theme(args.theme, fragments)
        
        if args.output:
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(merged)
            print(f"**Ghost Editor:** Thematic merge written to {args.output}")
        else:
            print(merged)
            
    elif args.book and args.chapter and args.fragments:
        fragment_list = [f.strip() for f in args.fragments.split(',')]
        chapter_content = merger.create_chapter(args.book, args.chapter, fragment_list)
        
        if args.output:
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(chapter_content)
        else:
            # Default output to book directory
            book_dir = merger.books[args.book]
            output_path = book_dir / f"chapter-{args.chapter:02d}-assembled.md"
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(chapter_content)
            print(f"**Narrator.exe:** Chapter written to {output_path}")
    
    else:
        print("**System:** Please specify either --auto-merge, --theme, or --book/--chapter/--fragments")

if __name__ == "__main__":
    main()