#!/usr/bin/env python3
import pathlib, re, sys

target = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else 'public/llms.txt')
gen = (sys.argv[2].lower() == 'true') if len(sys.argv) > 2 else True
if not target.exists():
    alt = pathlib.Path('llms.txt')
    if alt.exists():
        target = alt
if not target.exists() and gen:
    readme = pathlib.Path('README.md')
    title = readme.read_text(encoding='utf-8').splitlines()[0].lstrip('# ').strip() if readme.exists() else 'Project'
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(f'# {title}\n\n> Official documentation and AI citation index for {title}.\n\n## Documentation\n\n- [Overview](./README.md): Primary documentation\n', encoding='utf-8')
    print(f'[AEO-Gate] Synthesized starter {target}')
if not target.exists():
    print('::error ::Missing /llms.txt file.')
    sys.exit(1)
txt = target.read_text(encoding='utf-8')
ok = bool(re.search(r'^#\s+\S+', txt, re.M)) and bool(re.search(r'^>\s+\S+', txt, re.M)) and bool(re.search(r'^##\s+\S+', txt, re.M))
print(f'[AEO-Gate] {target} llmstxt.org compliance={ok}')
sys.exit(0 if ok else 1)
