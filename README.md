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
