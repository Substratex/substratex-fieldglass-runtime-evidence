from pathlib import Path
import hashlib

ROOT = Path(__file__).resolve().parents[2]
checks = ROOT / "CHECKSUMS.sha256"
assert checks.exists(), "CHECKSUMS.sha256 missing"
failures=[]
for line in checks.read_text(encoding="utf-8").splitlines():
    line=line.strip()
    if not line:
        continue
    digest, rel = line.split(None, 1)
    rel = rel.lstrip("*")
    p = ROOT / rel
    if not p.exists():
        failures.append(f"missing {rel}")
        continue
    actual = hashlib.sha256(p.read_bytes()).hexdigest()
    if actual != digest:
        failures.append(f"checksum mismatch {rel}")
assert not failures, "; ".join(failures)
print("checksums: PASS")
