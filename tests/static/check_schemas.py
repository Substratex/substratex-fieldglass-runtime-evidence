import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
for p in (ROOT/'schemas').glob('*.json'):
    json.loads(p.read_text(encoding='utf-8'))
print('schemas valid json: PASS')
