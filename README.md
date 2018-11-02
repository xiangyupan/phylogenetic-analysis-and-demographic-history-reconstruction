## Phylogenetic-analysis-and-demographic-history-reconstruction

1.build database   

`lastdb -uNEAR -cR11 cattle.db cattle.fa`

2.pairwise alignment   
`lastal -P20 -m100 -E0.05 22.db Choloepus_hoffmanni.choHof1.dna.toplevel.fa | last-split -m1 >sloth.22.maf`   

3.filter    
`maf-swap Cervus_albirostris.maf |last-split |maf-swap |last-split |maf-sort > Cervus_albirostris.last.maf`    

4.rename    
`perl maf.rename.species.S.pl Cervus_albirostris.last.maf Cattle(targetName) Cervus_albirostris(queryName) Cervus_albirostris.last.maf.final.maf > Cervus_albirostris.last.maf.stat`    

5.multiz   
`python3.5 MergeMAFFile.py -i chr1.list -p $PATH/chr1`  

6.filter_no_ref
`mafFilter -speciesFilter=filename chr1.raw.maf > chr1.filter.maf`    
##filename is a list name with the species name which we want to filter without it

7.pick 4dTV sites from maf   
`perl Identify_4D_Sites.pl UCD1.2.gff  cattle.4dtv.tmp`    
`perl gff_maker.pl cattle.4dtv.tmp > cattle.4dtv.gff`    
`perl 01.convertMaf2List.pl chr1.filter.maf`     
`perl 02.lst2gene.pl cattle.maf.lst`       
`perl cat_genes.pl`    
`python3.5 deal_cds_to_line.py rename.cds rename.cds.edit`    

