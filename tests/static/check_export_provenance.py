from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
INDEX = ROOT / "index.html"
text = INDEX.read_text(encoding="utf-8", errors="replace")
required = [
    "license",
    "citation",
    "origin",
    "lineage",
    "claim_boundary",
    "no_provenance_removal_notice",
    "generated_by",
    "Fieldglass® Runtime Evidence Observatory",
    "SubstrateX Public Research and Accountability License v1.0",
    "__fieldglassStampPublicReleaseProvenanceV313",
    "public_release_provenance_v313",
    "chronos_instrument_layer",
    "noesis_instrument_layer",
]
missing = [x for x in required if x not in text]
assert not missing, f"Missing export provenance markers: {missing}"
print("export provenance: PASS")
