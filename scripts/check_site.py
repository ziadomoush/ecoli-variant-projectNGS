#!/usr/bin/env python3
"""Check internal resources, route targets and manifest entries without a web server."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import unquote,urlsplit
import json,re,sys
ROOT=Path(__file__).resolve().parents[1]
class Inspect(HTMLParser):
 def __init__(self):super().__init__();self.refs=[];self.routes=set();self.ids=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if 'data-page' in a:self.routes.add(a['data-page'])
  if 'id' in a:self.ids.append(a['id'])
  for k in ['src','href','data-image']:
   if a.get(k):self.refs.append((k,a[k]))
p=Inspect();p.feed((ROOT/'index.html').read_text());errors=[]
for attr,ref in p.refs:
 if ref.startswith('#'):
  route=unquote(ref[1:])
  if route and route not in p.routes and route not in p.ids:errors.append('Unknown route '+ref)
 elif not urlsplit(ref).scheme and not (ROOT/unquote(urlsplit(ref).path)).is_file():errors.append('Missing resource '+ref)
for f in json.loads((ROOT/'assets/file-manifest.json').read_text()):
 if f['available'] and not (ROOT/f['path']).is_file():errors.append('Incorrect manifest availability '+f['path'])
 if (ROOT/f['path']).is_file() and f['size']!=(ROOT/f['path']).stat().st_size:errors.append('Incorrect size '+f['path'])
if len(p.ids)!=len(set(p.ids)):errors.append('Duplicate HTML id')
for name in ['site.css','site.js','project-data.js','manifest.js']:
 if not (ROOT/'assets'/name).is_file():errors.append('Missing app asset '+name)
if errors:print('\n'.join(errors));sys.exit(1)
print(f'PASS: {len(p.routes)} views, {len(p.refs)} local/external references, unique IDs and all included file mappings.')
