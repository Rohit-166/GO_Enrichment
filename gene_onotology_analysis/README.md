# Promoter Region Extraction (Strand-Aware)

## Objective
Convert gene annotation to BED format and extract promoter regions by extending 500 bp upstream of TSS in a strand-aware manner.

## Steps
1. Converted annotation file to BED using `make_bed.py`
2. Generated promoter regions using bedtools:

   bedtools slop -i tss.bed -g genome.txt -l 500 -r 0 -s > promoters.bed

## Files
- tss.bed → TSS coordinates
- promoters.bed → final promoter regions
- genome.txt → chromosome sizes
- make_bed.py → script to generate BED file