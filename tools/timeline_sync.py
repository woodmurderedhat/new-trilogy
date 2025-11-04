#!/usr/bin/env python3
"""
Timeline Synchronization Tool for Book II Dual-Resistance Narrative

Analyzes fragments across both Afrikaans and English resistances,
showing parallel events organized by timeline_week metadata.
"""

import os
import re
from collections import defaultdict
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
AFRIKAANS_DIR = BASE_DIR / 'book2_echo-machine' / 'afrikaans' / 'scenes'
ENGLISH_DIR = BASE_DIR / 'book2_echo-machine' / 'english' / 'scenes'

FRONT_MATTER_RE = re.compile(r'^---\n(.*?)\n---\n', re.S)


def parse_front_matter(text: str) -> dict:
    """Extract YAML metadata from fragment."""
    match = FRONT_MATTER_RE.match(text)
    if not match:
        return {}
    
    metadata = {}
    for line in match.group(1).splitlines():
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        if ':' not in line:
            continue
        key, value = line.split(':', 1)
        metadata[key.strip()] = value.strip()
    return metadata


def extract_title(text: str) -> str:
    """Extract title from markdown content."""
    # Remove front matter
    text = FRONT_MATTER_RE.sub('', text)
    # Find first heading
    match = re.search(r'^#\s+(.+)$', text, re.MULTILINE)
    if match:
        return match.group(1).strip()
    return "Untitled"


def load_fragments(directory: Path):
    """Load all fragments from directory with metadata."""
    fragments = []
    if not directory.exists():
        return fragments
    
    for filepath in directory.glob('*.md'):
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                text = f.read()
            
            metadata = parse_front_matter(text)
            title = extract_title(text)
            
            fragments.append({
                'filename': filepath.name,
                'title': title,
                'metadata': metadata,
                'path': filepath
            })
        except Exception as e:
            print(f"Warning: Could not parse {filepath.name}: {e}")
    
    return fragments


def organize_by_timeline(fragments):
    """Organize fragments by timeline_week."""
    timeline = defaultdict(list)
    no_timeline = []
    
    for frag in fragments:
        week = frag['metadata'].get('timeline_week', '').strip()
        if week and week.isdigit():
            timeline[int(week)].append(frag)
        else:
            no_timeline.append(frag)
    
    return timeline, no_timeline


def print_timeline_report(af_fragments, en_fragments):
    """Print synchronized timeline showing parallel events."""
    af_timeline, af_no_timeline = organize_by_timeline(af_fragments)
    en_timeline, en_no_timeline = organize_by_timeline(en_fragments)
    
    all_weeks = sorted(set(list(af_timeline.keys()) + list(en_timeline.keys())))
    
    print("=" * 100)
    print("BOOK II: ECHO MACHINE — DUAL-RESISTANCE TIMELINE SYNCHRONIZATION")
    print("=" * 100)
    print()
    
    for week in all_weeks:
        print(f"{'─' * 100}")
        print(f"WEEK {week:02d}")
        print(f"{'─' * 100}")
        
        af_frags = af_timeline.get(week, [])
        en_frags = en_timeline.get(week, [])
        
        # Print side by side
        print(f"\n{'SOUTHERN AFRICA (Afrikaans)':<50} {'EASTERN EUROPE (English)':<50}")
        print(f"{'─' * 50} {'─' * 50}")
        
        max_len = max(len(af_frags), len(en_frags))
        
        for i in range(max_len):
            af_entry = ""
            en_entry = ""
            
            if i < len(af_frags):
                frag = af_frags[i]
                keywords = frag['metadata'].get('keywords', '[]')
                af_entry = f"• {frag['title'][:45]}\n  {frag['filename']}\n  {keywords[:45]}"
            
            if i < len(en_frags):
                frag = en_frags[i]
                keywords = frag['metadata'].get('keywords', '[]')
                en_entry = f"• {frag['title'][:45]}\n  {frag['filename']}\n  {keywords[:45]}"
            
            # Print entries side by side
            af_lines = af_entry.split('\n') if af_entry else ['']
            en_lines = en_entry.split('\n') if en_entry else ['']
            max_lines = max(len(af_lines), len(en_lines))
            
            for j in range(max_lines):
                af_line = af_lines[j] if j < len(af_lines) else ''
                en_line = en_lines[j] if j < len(en_lines) else ''
                print(f"{af_line:<50} {en_line:<50}")
            print()
        
        # Summary for this week
        print(f"Week {week} Summary: {len(af_frags)} Afrikaans fragments, {len(en_frags)} English fragments")
        print()
    
    print(f"{'═' * 100}")
    print("FRAGMENTS WITHOUT TIMELINE METADATA")
    print(f"{'═' * 100}")
    
    if af_no_timeline:
        print(f"\nAfrikaans ({len(af_no_timeline)}):")
        for frag in af_no_timeline[:10]:  # Show first 10
            print(f"  • {frag['filename']}: {frag['title']}")
    
    if en_no_timeline:
        print(f"\nEnglish ({len(en_no_timeline)}):")
        for frag in en_no_timeline[:10]:  # Show first 10
            print(f"  • {frag['filename']}: {frag['title']}")
    
    print()
    print(f"{'═' * 100}")
    print("STATISTICS")
    print(f"{'═' * 100}")
    print(f"Total Afrikaans fragments: {len(af_fragments)}")
    print(f"Total English fragments: {len(en_fragments)}")
    print(f"Weeks with Afrikaans content: {len(af_timeline)}")
    print(f"Weeks with English content: {len(en_timeline)}")
    print(f"Synchronized weeks (both): {len(set(af_timeline.keys()) & set(en_timeline.keys()))}")
    print(f"Timeline coverage: Weeks {min(all_weeks) if all_weeks else 'N/A'} - {max(all_weeks) if all_weeks else 'N/A'}")
    print()


def print_gap_analysis(af_fragments, en_fragments):
    """Identify timeline gaps where one resistance has content but not the other."""
    af_timeline, _ = organize_by_timeline(af_fragments)
    en_timeline, _ = organize_by_timeline(en_fragments)
    
    af_weeks = set(af_timeline.keys())
    en_weeks = set(en_timeline.keys())
    
    af_only = sorted(af_weeks - en_weeks)
    en_only = sorted(en_weeks - af_weeks)
    
    if af_only or en_only:
        print(f"{'═' * 100}")
        print("GAP ANALYSIS — Opportunities for Cross-Resistance Content")
        print(f"{'═' * 100}")
        
        if af_only:
            print(f"\nWeeks with Afrikaans but NO English: {af_only}")
            print("  → Generate English fragments for these weeks to synchronize timelines")
        
        if en_only:
            print(f"\nWeeks with English but NO Afrikaans: {en_only}")
            print("  → Generate Afrikaans fragments for these weeks to synchronize timelines")
        print()


def main():
    print("Loading fragments...\n")
    
    af_fragments = load_fragments(AFRIKAANS_DIR)
    en_fragments = load_fragments(ENGLISH_DIR)
    
    if not af_fragments and not en_fragments:
        print("Error: No fragments found in either directory")
        print(f"  Afrikaans: {AFRIKAANS_DIR}")
        print(f"  English: {ENGLISH_DIR}")
        return
    
    print_timeline_report(af_fragments, en_fragments)
    print_gap_analysis(af_fragments, en_fragments)
    
    print("=" * 100)
    print("NEXT STEPS")
    print("=" * 100)
    print("1. Generate fragments for gap weeks using: python tools/cutup.py --lang [af|en]")
    print("2. Create cross-resistance hybrids: python tools/cutup.py --cross-resistance --timeline-week [N]")
    print("3. Review synchronized weeks for thematic resonances")
    print()


if __name__ == '__main__':
    main()
