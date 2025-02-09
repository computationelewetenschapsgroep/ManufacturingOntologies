from rdflib import Graph
from pathlib import Path
import sys

parser = Graph()
triple_store = Graph()

dir = Path(sys.argv[1])
json_ld_files = list(dir.glob("**/*.json"))

for file in json_ld_files:
    print(f"Reading in {file}")
    parser.parse(file, format="json-ld")

    print(f"Read {len(parser)} triples")

    print(f"PreUpdate: Number of triples in triple_store: {len(triple_store)}")

    for s,p,o in parser:
        triple_store.add((s,p,o))

    print(f"PostUpdate: Number of triples in triple_store: {len(triple_store)}")

triple_store.serialize("isa-95-wot.ttl")