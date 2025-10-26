#!/usr/bin/env python3
"""
cutup.py - The Burroughs-Gysin Cut-Up Engine for Cutup-Trilogy

This script implements digital cut-up methodology, fragmenting and recombining
text according to algorithmic and random principles. It operates on the 
premise that meaning emerges from the collision of disconnected fragments.

Usage:
    python cutup.py --input scenes/ --method random --fragments 10
    python cutup.py --file fragment-001-mirror-code.md --method systematic
    python cutup.py --generate-new --theme perception_as_malware
"""

import os
import re
import random
import yaml
import argparse
from pathlib import Path
from typing import List, Dict, Any

class CutUpEngine:
    """
    The machine that cuts text until it bleeds meaning.
    Then rearranges the stains.
    """
    
    def __init__(self):
        self.fragments = []
        self.metadata = {}
        self.voices = ["System", "Ghost Editor", "Narrator.exe", "Echo"]
        
    def load_fragment(self, filepath: str) -> Dict[str, Any]:
        """Load a scene fragment with its YAML metadata."""
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Split YAML frontmatter from content
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                yaml_content = parts[1]
                text_content = parts[2].strip()
                metadata = yaml.safe_load(yaml_content)
            else:
                metadata = {}
                text_content = content
        else:
            metadata = {}
            text_content = content
            
        return {
            'filepath': filepath,
            'metadata': metadata,
            'content': text_content,
            'sentences': self.split_sentences(text_content)
        }
    
    def split_sentences(self, text: str) -> List[str]:
        """Split text into sentences, preserving the ghosts between words."""
        # Remove markdown headers and code blocks
        text = re.sub(r'^#.*$', '', text, flags=re.MULTILINE)
        text = re.sub(r'```.*?```', '', text, flags=re.DOTALL)
        text = re.sub(r'`.*?`', '', text)
        
        # Split on sentence boundaries
        sentences = re.split(r'[.!?]+', text)
        sentences = [s.strip() for s in sentences if s.strip()]
        
        return sentences
    
    def random_cut_up(self, fragments: List[Dict], num_pieces: int = 10) -> str:
        """Burroughs-style random recombination."""
        all_sentences = []
        for fragment in fragments:
            all_sentences.extend(fragment['sentences'])
        
        # Random selection and shuffling
        selected = random.sample(all_sentences, min(num_pieces, len(all_sentences)))
        random.shuffle(selected)
        
        # Assign random voices
        result = []
        for sentence in selected:
            voice = random.choice(self.voices)
            result.append(f"**{voice}:**\n{sentence}\n")
        
        return '\n'.join(result)
    
    def systematic_cut_up(self, fragments: List[Dict]) -> str:
        """Gysin-style systematic recombination using geometric patterns."""
        all_sentences = []
        for fragment in fragments:
            all_sentences.extend(fragment['sentences'])
        
        if not all_sentences:
            return "**System:** No sentences found to recombine."
        
        # Create a 3x3 grid pattern (simplified)
        grid_size = 9
        if len(all_sentences) < grid_size:
            # Repeat sentences to fill grid
            multiplied = (all_sentences * ((grid_size // len(all_sentences)) + 1))[:grid_size]
        else:
            multiplied = all_sentences[:grid_size]
        
        # Read pattern: spiral from outside in
        spiral_order = [0, 1, 2, 5, 8, 7, 6, 3, 4]
        
        result = []
        for i in spiral_order:
            if i < len(multiplied):
                voice = self.voices[i % len(self.voices)]
                result.append(f"**{voice}:**\n{multiplied[i]}\n")
        
        return '\n'.join(result)
    
    def thematic_cut_up(self, fragments: List[Dict], theme: str) -> str:
        """Select fragments based on thematic connections."""
        filtered = []
        for fragment in fragments:
            keywords = fragment['metadata'].get('keywords', [])
            if theme.lower() in [kw.lower() for kw in keywords]:
                filtered.append(fragment)
        
        if not filtered:
            # Fall back to all fragments
            filtered = fragments
            
        return self.random_cut_up(filtered, num_pieces=8)
    
    def generate_metadata(self, theme: str = None, corruption_level: str = "medium") -> Dict:
        """Generate metadata for a new fragment."""
        themes = ["perception_as_malware", "collaboration_as_identity_collapse", 
                 "reconstruction_after_semantic_extinction"]
        
        if not theme:
            theme = random.choice(themes)
        
        return {
            'keywords': [theme.split('_')[0], 'cutup', 'generated', 'recombination'],
            'connections': [],
            'ai_origin': 'cutup-engine',
            'version': 'generated',
            'corruption_level': corruption_level,
            'theme': theme
        }

def main():
    parser = argparse.ArgumentParser(description='Cut-up text generation for Cutup-Trilogy')
    parser.add_argument('--input', type=str, help='Input directory or file')
    parser.add_argument('--method', choices=['random', 'systematic', 'thematic'], 
                       default='random', help='Cut-up method')
    parser.add_argument('--fragments', type=int, default=10, 
                       help='Number of fragments to combine')
    parser.add_argument('--theme', type=str, help='Theme for thematic cut-up')
    parser.add_argument('--output', type=str, help='Output file')
    parser.add_argument('--generate-new', action='store_true', 
                       help='Generate new fragment from cut-up')
    
    args = parser.parse_args()
    
    engine = CutUpEngine()
    
    # Load fragments
    fragments = []
    if args.input:
        if os.path.isdir(args.input):
            for file in Path(args.input).glob('*.md'):
                fragments.append(engine.load_fragment(str(file)))
        else:
            fragments.append(engine.load_fragment(args.input))
    else:
        # Default to scenes directory
        scenes_dir = Path(__file__).parent.parent / 'scenes'
        for file in scenes_dir.glob('*.md'):
            fragments.append(engine.load_fragment(str(file)))
    
    # Generate cut-up
    if args.method == 'random':
        result = engine.random_cut_up(fragments, args.fragments)
    elif args.method == 'systematic':
        result = engine.systematic_cut_up(fragments)
    elif args.method == 'thematic':
        result = engine.thematic_cut_up(fragments, args.theme or 'memory')
    
    # Add metadata if generating new fragment
    if args.generate_new:
        metadata = engine.generate_metadata(args.theme)
        yaml_header = f"---\n{yaml.dump(metadata)}---\n\n"
        fragment_title = f"# Generated Fragment: Cut-Up {random.randint(100, 999)}\n\n"
        result = yaml_header + fragment_title + result
    
    # Output
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(result)
        print(f"**Ghost Editor:** Cut-up written to {args.output}")
    else:
        print("**System:** Cut-up generation complete.\n")
        print(result)

if __name__ == "__main__":
    main()