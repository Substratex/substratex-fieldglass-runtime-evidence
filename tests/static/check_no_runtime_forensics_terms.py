from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
old_upper = 'Runtime ' + 'Forensics'
old_lower = 'runtime ' + 'forensics'
violations=[]
for p in ROOT.rglob('*'):
    if p.is_file() and p.suffix.lower() in {'.md','.txt','.json','.html','.cff','.yml','.yaml'}:
        s = p.read_text(encoding='utf-8', errors='ignore')
        if old_upper in s or old_lower in s:
            violations.append(str(p.relative_to(ROOT)))
assert not violations, 'Old Runtime Forensics terms remain: ' + ', '.join(violations)
print('terminology lock: PASS')
