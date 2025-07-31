SELECT gene, COUNT(*) as num_variants -- counting all variants per gene
FROM variants -- Calling variant table
GROUP BY gene; -- grouping by genes
