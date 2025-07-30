import pandas as pd
import gzip
import re

# Set your GTF file path here
gtf_file = "gencode.vXX.annotation.gtf"  # or .gtf.gz if compressed

# Initialize set for unique gene names
gene_names = set()

# Open file (support both plain or gzipped GTF)
open_func = gzip.open if gtf_file.endswith(".gz") else open
with open_func(gtf_file, "rt") as f:
    for line in f:
        if line.startswith("#"):
            continue
        fields = line.strip().split("\t")
        feature_type = fields[2]
        if feature_type == "gene":
            attr_field = fields[8]
            match = re.search(r'gene_name "([^"]+)"', attr_field)
            if match:
                gene_names.add(match.group(1))

# Convert to sorted list and save
gene_list = sorted(gene_names)
pd.DataFrame({"gene_symbol": gene_list}).to_csv("gene_list.csv", index=False)
print(f"✅ Extracted {len(gene_list)} unique gene symbols to gene_list.csv")
