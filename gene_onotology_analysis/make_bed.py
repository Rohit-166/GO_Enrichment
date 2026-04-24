import gzip

with gzip.open("human_gene_annotation.tsv.gz", "rt") as f, open("tss.bed", "w") as out:
    next(f)  

    for line in f:
        parts = line.strip().split("\t")

        chrom = parts[4]                      
        strand = parts[5]                     
        gene = parts[6]                     
        tss = int(parts[7])                  

        if chrom == "MT":
            chrom = "chrM"
        else:
            chrom = "chr" + chrom

        # fix strand
        strand = "+" if strand == "1" else "-"

        start = tss
        end = tss + 1

        name = f"{chrom}@{start}-{end}|{gene}"

        out.write(f"{chrom}\t{start}\t{end}\t{name}\t.\t{strand}\n")
