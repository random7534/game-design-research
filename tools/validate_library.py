"""Validate source traceability, local links and the public/private boundary.

This checks document invariants, not game quality or player experience.
Uses only Python's standard library. Exits nonzero on invalid content.
"""
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

def validate(root):
    root = Path(root).resolve()
    errors = []
    sources = json.loads((root / 'skills/game-design-development/references/sources.json').read_text(encoding='utf-8'))
    candidates = json.loads((root / 'research/candidates.json').read_text(encoding='utf-8'))
    source_ids = set()
    for item in sources['sources']:
        sid = item.get('id')
        if not sid or sid in source_ids:
            errors.append(f'duplicate or missing source id: {sid}')
        source_ids.add(sid)
        for key in ('title','url','accessed_on','coverage','source_claim','limits','date_basis'):
            if not item.get(key):
                errors.append(f'{sid}: missing {key}')
        url = urlsplit(item.get('url',''))
        if url.scheme != 'https' or not url.netloc:
            errors.append(f'{sid}: invalid public source URL')
        if re.search(r'(?:xsec_token|access_token|api_key|auth_token)=',url.query,re.I):
            errors.append(f'{sid}: access parameter in public URL')
    primary = sum(s.get('type') != 'community_self_report' for s in sources['sources'])
    community = len(sources['sources']) - primary
    if primary != sources['primary_source_count'] or community != sources['community_record_count']:
        errors.append('source counts do not match registry')

    candidate_ids = set()
    for item in candidates['candidates']:
        cid = item.get('id')
        if not cid or cid in candidate_ids:
            errors.append(f'duplicate or missing candidate id: {cid}')
        candidate_ids.add(cid)
        if not item.get('source_ids') or set(item['source_ids']) - source_ids:
            errors.append(f'{cid}: unknown or missing source references')
        if item.get('status') not in ('proposed','experimented','deprecated'):
            errors.append(f'{cid}: personal endorsement does not belong in public registry')
        if item.get('status') == 'experimented' and not item.get('experiment_evidence'):
            errors.append(f'{cid}: experimented claim needs evidence')
        for key in ('claim','conditions','limits','validation'):
            if not item.get(key):
                errors.append(f'{cid}: missing {key}')

    files = [p for p in root.rglob('*') if p.is_file() and '.git' not in p.relative_to(root).parts]
    text_files = [p for p in files if p.suffix in ('.md','.json','.yaml','.yml')]
    link_count = 0
    for path in text_files:
        rel = path.relative_to(root)
        try:
            content = path.read_text(encoding='utf-8')
        except UnicodeDecodeError:
            errors.append(f'{rel}: not UTF-8')
            continue
        if '\ufffd' in content:
            errors.append(f'{rel}: replacement characters')
        if re.search(r'[A-Za-z]:[\\/](?:Users|学习资料|项目)[\\/]',content):
            errors.append(f'{rel}: local personal or workspace path in public content')
        if re.search(r'(?:xsec_token|access_token|api_key|auth_token)=[^\s)]+',content,re.I):
            errors.append(f'{rel}: possible access token')
        if re.search(r'(?:ghp_|github_pat_|sk-proj-)[A-Za-z0-9_]{16,}',content):
            errors.append(f'{rel}: credential-like value')
        if path.suffix == '.md':
            for target in re.findall(r'\[[^\]\n]*\]\(([^)\n]+)\)',content):
                target = target.strip('<>')
                if target.startswith(('http:','https:','mailto:','#')):
                    continue
                dest = (path.parent / unquote(target.split('#')[0])).resolve()
                link_count += 1
                if not dest.is_relative_to(root):
                    errors.append(f'{rel}: link leaves public root: {target}')
                elif not dest.exists():
                    errors.append(f'{rel}: broken local link: {target}')
            for sid in re.findall(r'\[((?:D\d\d|G\d\d|R\d\d|PROD-\d\d|XHS-[A-Z0-9]+))\]',content):
                if sid not in source_ids:
                    errors.append(f'{rel}: unknown cited source: {sid}')
    return {'ok': not errors,'primary_sources':primary,'community_records':community,
            'candidates':len(candidate_ids),'text_files':len(text_files),'local_links':link_count,'errors':errors}

if __name__ == '__main__':
    try:
        report = validate(sys.argv[1] if len(sys.argv)>1 else Path(__file__).resolve().parents[1])
    except (OSError, ValueError, KeyError, TypeError) as exc:
        report = {'ok':False,'errors':[str(exc)]}
    print(json.dumps(report,ensure_ascii=True,indent=2))
    sys.exit(0 if report['ok'] else 1)
