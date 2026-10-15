#!/usr/bin/env python3
"""Refresh file availability after adding project outputs; does not rerun analysis."""
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]
p=ROOT/'assets/file-manifest.json'
files=json.loads(p.read_text())
def category(path):
 return 'QC' if '/qc/' in path else 'Alignment' if '/bam/' in path else 'Variants' if '/vcf/' in path else 'Inputs' if path.startswith('data/') else 'Report & evidence'
seen={f['path'] for f in files}
for folder in ['data','results','reports']:
 for path in sorted((ROOT/folder).rglob('*')):
  if path.is_file() and not path.name.startswith('.') and path.name!='ADD_FILES_HERE.txt':
   rel=path.relative_to(ROOT).as_posix()
   if rel not in seen:
    files.append(dict(path=rel,size=0,available=False,category=category(rel)));seen.add(rel)
for f in files:
 path=ROOT/f['path'];f['available']=path.is_file();f['size']=path.stat().st_size if path.is_file() else 0
 f['preview']=path.read_text(errors='replace') if path.is_file() and path.suffix in ['.txt','.tsv','.vcf','.xml','.log'] and f['size']<2_000_000 else None
p.write_text(json.dumps(files,ensure_ascii=False,indent=2))
(ROOT/'assets/manifest.js').write_text('window.PROJECT_FILES='+json.dumps(files,ensure_ascii=False)+';\n')
print(f"Manifest refreshed: {sum(f['available'] for f in files)} included; {sum(not f['available'] for f in files)} expected files absent.")
