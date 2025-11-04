import argparse
import os
import random
import re

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
SCENES_DIR = os.path.join(BASE_DIR, 'scenes')
AFRIKAANS_DIR = os.path.join(BASE_DIR, 'book2_echo-machine', 'afrikaans', 'scenes')
ENGLISH_DIR = os.path.join(BASE_DIR, 'book2_echo-machine', 'english', 'scenes')
CUTUP_DIR = os.path.join(BASE_DIR, 'book2_echo-machine', 'cutup')
OUT_DIR_DEFAULT = os.path.join(BASE_DIR, 'book2_echo-machine')

# Map language codes to preferred fragment directories
LANGUAGE_DIRS = {
    'af': [AFRIKAANS_DIR],
    'en': [ENGLISH_DIR],
}

# Fallback search paths for fragments when no language is specified
DEFAULT_DIRS = [SCENES_DIR]

FRONT_MATTER_RE = re.compile(r'^---\n(.*?)\n---\n(.*)$', re.S)


def parse_front_matter(block: str) -> dict:
    metadata = {}
    for line in block.splitlines():
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        if ':' not in line:
            continue
        key, value = line.split(':', 1)
        metadata[key.strip()] = value.strip()
    return metadata


def iter_scene_files(root_paths):
    for root in root_paths:
        if not os.path.isdir(root):
            continue
        for dirpath, _, filenames in os.walk(root):
            for fn in filenames:
                if fn.lower().endswith('.md'):
                    yield os.path.join(dirpath, fn)


def load_fragments(language: str | None):
    search_dirs = LANGUAGE_DIRS.get(language, DEFAULT_DIRS)
    frags = []
    for path in iter_scene_files(search_dirs):
        with open(path, 'r', encoding='utf-8') as f:
            text = f.read()
        metadata = {}
        body = text.strip()
        match = FRONT_MATTER_RE.match(text)
        if match:
            metadata = parse_front_matter(match.group(1))
            body = match.group(2).strip()
        lang_value = metadata.get('language', '').strip("'") if metadata else ''
        if language and lang_value.lower() != language.lower():
            continue
        frags.append({
            'body': body,
            'metadata': metadata,
            'path': path
        })
    return frags


def load_cross_resistance_fragments():
    """Load both Afrikaans and English fragments for cross-resistance mixing."""
    af_frags = load_fragments('af')
    en_frags = load_fragments('en')
    return af_frags, en_frags


def match_timeline_fragments(af_frags, en_frags, timeline_week=None):
    """Match fragments from both resistances by timeline_week."""
    if timeline_week:
        af_frags = [f for f in af_frags if f['metadata'].get('timeline_week', '').strip() == str(timeline_week)]
        en_frags = [f for f in en_frags if f['metadata'].get('timeline_week', '').strip() == str(timeline_week)]
    return af_frags, en_frags


def next_output_path(language: str | None, is_cross_resistance: bool = False) -> str:
    if is_cross_resistance:
        target_dir = CUTUP_DIR
        prefix = 'resonance_'
    elif language and language in LANGUAGE_DIRS:
        target_dir = LANGUAGE_DIRS[language][0]
        prefix = f'cutup_{language}_'
    else:
        target_dir = OUT_DIR_DEFAULT
        prefix = 'generated_fragment_'
    
    os.makedirs(target_dir, exist_ok=True)
    existing_numbers = []
    for fn in os.listdir(target_dir):
        if fn.startswith(prefix) and fn.endswith('.md'):
            digits = ''.join(ch for ch in fn[len(prefix):-3] if ch.isdigit())
            if digits:
                existing_numbers.append(int(digits))
    next_num = max(existing_numbers, default=0) + 1
    return os.path.join(target_dir, f'{prefix}{next_num:03d}.md')


def make_cutup(n_sentences: int, language: str | None):
    frags = load_fragments(language)
    if not frags:
        print('Geen fragmente gevind nie.')
        return
    pieces = []
    for fragment in frags:
        body = fragment['body']
        sentences = re.split(r'(?<=[\.\?\!])\s+', body)
        pieces.extend([sentence.strip() for sentence in sentences if sentence.strip()])
    if not pieces:
        print('Geen bruikbare sin-fragmente gevind nie.')
        return
    random.shuffle(pieces)
    selection = ' '.join(pieces[:n_sentences])
    out_path = next_output_path(language, is_cross_resistance=False)
    yaml_header = (
        '---\n'
        'keywords: [cutup, echo]\n'
        'connections: []\n'
        'ai_origin: echo-thread\n'
        'version: unstable\n'
        'corruption_level: medium\n'
    )
    if language:
        yaml_header += f'language: {language}\n'
    yaml_header += '---\n\n'
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(yaml_header + selection)
    print('Geskryf:', out_path)


def make_cross_resistance_cutup(n_sentences_per_lang: int = 5, timeline_week: int | None = None):
    """Create hybrid fragments mixing Afrikaans and English resistance narratives."""
    af_frags, en_frags = load_cross_resistance_fragments()
    
    if not af_frags or not en_frags:
        print('Error: Need both Afrikaans and English fragments for cross-resistance cutup')
        return
    
    if timeline_week:
        af_frags, en_frags = match_timeline_fragments(af_frags, en_frags, timeline_week)
        if not af_frags or not en_frags:
            print(f'Warning: No matching fragments for timeline_week {timeline_week}')
            # Fall back to all fragments
            af_frags, en_frags = load_cross_resistance_fragments()
    
    # Extract sentences from both languages
    af_pieces = []
    en_pieces = []
    af_sources = []
    en_sources = []
    
    for frag in af_frags:
        body = frag['body']
        sentences = re.split(r'(?<=[\.\?\!])\s+', body)
        af_pieces.extend([s.strip() for s in sentences if s.strip()])
        af_sources.append(os.path.basename(frag['path']))
    
    for frag in en_frags:
        body = frag['body']
        sentences = re.split(r'(?<=[\.\?\!])\s+', body)
        en_pieces.extend([s.strip() for s in sentences if s.strip()])
        en_sources.append(os.path.basename(frag['path']))
    
    # Shuffle and select from each language
    random.shuffle(af_pieces)
    random.shuffle(en_pieces)
    
    af_selection = af_pieces[:n_sentences_per_lang]
    en_selection = en_pieces[:n_sentences_per_lang]
    
    # Interleave sentences for bilingual corruption effect
    mixed_pieces = []
    for af_sent, en_sent in zip(af_selection, en_selection):
        mixed_pieces.append(af_sent)
        mixed_pieces.append(en_sent)
    
    # Add remaining sentences if one list is longer
    if len(af_selection) > len(en_selection):
        mixed_pieces.extend(af_selection[len(en_selection):])
    elif len(en_selection) > len(af_selection):
        mixed_pieces.extend(en_selection[len(af_selection):])
    
    selection = '\n\n'.join(mixed_pieces)
    
    out_path = next_output_path(None, is_cross_resistance=True)
    
    yaml_header = (
        '---\n'
        'keywords: [cross_resistance, echo_resonance, bilingual_corruption]\n'
        f'connections: [{", ".join(set(af_sources[:3] + en_sources[:3]))}]\n'
        'ai_origin: cutup-collision\n'
        'version: recursive\n'
        'corruption_level: critical\n'
        'language: af+en\n'
        'resistance: both\n'
    )
    if timeline_week:
        yaml_header += f'timeline_week: {timeline_week:02d}\n'
    
    yaml_header += f'cutup_sources: [{", ".join(set(af_sources[:2] + en_sources[:2]))}]\n'
    yaml_header += '---\n\n'
    yaml_header += '# Cross-Resistance Resonance Fragment\n\n'
    yaml_header += '**Echo:** [Bilingual corruption — language bleeding across continents]\n\n'
    
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(yaml_header + selection)
    
    print('Cross-resistance cutup written:', out_path)
    print(f'Mixed {len(af_selection)} Afrikaans + {len(en_selection)} English fragments')
    if timeline_week:
        print(f'Timeline: Week {timeline_week}')


def main():
    parser = argparse.ArgumentParser(description='Cut-up generator vir Echo Machine.')
    parser.add_argument('--sentences', type=int, default=6, help='Aantal sinne om te gebruik')
    parser.add_argument('--lang', type=str, default=None, help='Taalfilter: af (Afrikaans) of en (English)')
    parser.add_argument('--cross-resistance', action='store_true', 
                        help='Create cross-resistance fragment mixing Afrikaans and English')
    parser.add_argument('--timeline-week', type=int, default=None,
                        help='Filter fragments by timeline_week for synchronized mixing')
    args = parser.parse_args()
    
    if args.cross_resistance:
        make_cross_resistance_cutup(
            n_sentences_per_lang=args.sentences,
            timeline_week=args.timeline_week
        )
    else:
        make_cutup(args.sentences, args.lang)


if __name__ == '__main__':
    main()
