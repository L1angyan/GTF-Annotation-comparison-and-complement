# GTF-Annotation-comparison-and-complement

#Using stringtie to generate a new annotation file in GTF format through transcriptome assembly.

#The scripts is uesd to complement extra transcripts not annotated in reference annotation

#Here, I get a re-annotation file in GTF format. I want to add the new transcripts to my reference annotation. 

#However, the stringtie --merge or cuffmerge would chage the prefix of genes.

## USAGE

gffcompare -G -r ~/rice_ref/Oryza_sativa.IRGSP-1.0.48.gtf -o compare rice_merge_update.gtf

#Using gffcompare to find transcripts different from that in reference annotation

python3 parse_compare.py compare.annotation.gtf rice_merge_update.gtf > extra.gtf

#compare.annotation.gtf is the output of gffcompare, the rice_merge_update.gtf is our re-annotation file.

#Output the new transcripts to the extra.gtf

cat extra.gtf >> ~/rice_ref/Oryza_sativa.IRGSP-1.0.48.gtf

#Now we get the complemented annotation file ~/rice_ref/Oryza_sativa.IRGSP-1.0.48.gtf.
