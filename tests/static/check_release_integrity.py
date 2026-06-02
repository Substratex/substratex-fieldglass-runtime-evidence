from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
INDEX = ROOT / "index.html"
text = INDEX.read_text(encoding="utf-8", errors="replace")
required = [
    "V270_PUBLIC_RELEASE_PROVENANCE_LICENSE_LOCK",
    "Fieldglass® Runtime Evidence Observatory",
    "SubstrateX® Runtime Evidence Infrastructure",
    "SubstrateX Public Research and Accountability License v1.0",
    "__fieldglassStampPublicReleaseProvenanceV270",
    "no_provenance_removal_notice",
    "Recursive Science® → SubstrateX® → Fieldglass® → RuntimeEvidence.com → EvidenceCommons®",
]
missing = [x for x in required if x not in text]
assert not missing, f"Missing release markers: {missing}"
print("release integrity: PASS")
