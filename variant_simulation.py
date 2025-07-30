import pandas as pd
import random
import gzip
import re

# ----------------------
# Configuration
# ----------------------

NUM_VARIANTS = 1000 # Change for bigger test datasets
GTF_file = "./GTF/genecode.v45.annotation.gtf.gz"

SAMPLES = [f"S{i}" for i in range(1,501)] # 500 samples
CHROMOSOMES = [str(i) for i in range(1,23)] + ["X", "Y"]
VARIANT_TYPES = ["SNV", "INDEL", "CNV", "SV"]
IMPACT_LEVELS = ["high", "moderate", "low", "modifier"]

# ----------------------
# Step 1: Extract gene symbols from GTF
# ----------------------
def extract_gene_symbols_from_gtf(gtf_path):
    gene_names = set()
    open_func = gzip.open if gtf_path.endswith(".gz") else open

    with open_func(gtf_path, "rt") as f:
        for line in f:
            if line.startswith("#"):
                continue
            fields = line.strip().split("\t")
            if fields[2] != "gene":
                continue
            attr_field = fields[8]
            match = re.search(r'gene_name "([^"]+)"', attr_field)
            if match:
                gene_names.add(match.group(1))
    return sorted(gene_names)


# Get gene symbols from GTF
GENES = extract_gene_symbols_from_gtf(GTF_FILE)
print(f"Loaded {len(GENES)} gene names from GTF.")


# --------------------------
# Step 2: Variant Simulation
# --------------------------
def generate_variant():
    return {
        "sample_id": random.choice(SAMPLES),
        "gene": random.choice(GENES),
        "chromosome": "chr" + random.choice(CHROMOSOMES),
        "variant_type": random.choice(VARIANT_TYPES),
        "impact": random.choices(
            IMPACT_LEVELS,
            weights=[0.1, 0.3, 0.5, 0.1],  # skewed toward low/moderate
            k=1
        )[0],
    }

variants = [generate_variant() for _ in range(NUM_VARIANTS)]
df = pd.DataFrame(variants)



# --------------------------
# Step 3: Output
# --------------------------
df.to_csv("variants_simulated.csv", index=False)
print("Simulated variant data writen to variants_simulated.csv")
