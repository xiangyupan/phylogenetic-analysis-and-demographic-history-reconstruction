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
> multiz {3}{0}.maf {3}{1}.maf 0 all > {3}{2}.maf    

6.filter_no_ref     
`mafFilter -speciesFilter=filename chr1.raw.maf > chr1.filter.maf`    
##filename is a list name with the species name which we want to filter without it

7. filter gff  
`perl clear_gff.pl UCD1.2.gff`     

8.pick 4dTV sites from maf   
`perl Identify_4D_Sites.pl UCD1.2.gff cattle.fa cattle.4dtv.tmp`    
`perl gff_maker.pl cattle.4dtv.tmp > cattle.4dtv.gff`    
`perl 01.convertMaf2List.pl chr1.filter.maf 1`     
`perl 02.lst2gene.pl cattle.maf.lst`       
`perl cat_genes.pl`    
`python3.5 deal_cds_to_line.py rename.cds rename.cds.edit`    
`cat 1/rename.cds.edit 2/rename.cds.edit 3/rename.cds.edit 4/rename.cds.edit 5/rename.cds.edit 6/rename.cds.edit 7/rename.cds.edit 8/rename.cds.edit 9/rename.cds.edit 10/rename.cds.edit 11/rename.cds.edit 12/rename.cds.edit 13/rename.cds.edit 14/rename.cds.edit 15/rename.cds.edit 16/rename.cds.edit 17/rename.cds.edit 18/rename.cds.edit 19/rename.cds.edit 20/rename.cds.edit 21/rename.cds.edit 22/rename.cds.edit 23/rename.cds.edit 24/rename.cds.edit 25/rename.cds.edit 26/rename.cds.edit 27/rename.cds.edit 28/rename.cds.edit 29/rename.cds.edit S/rename.cds.edit MT/rename.cds.edit X/rename.cds.edit  > All.rename.cds.edit`     
`python3.5 cds_to_4dtv.py Cattle.rename.cds.edit Cattle Cattle.4dTV.fasta`      
`cat *.fasta > All.12.species.Cervidae.4DTV.fasta`    

9、ML tree by iqtree   
`iqtree -s All.12.species.Cervidae.4DTV.fasta -nt 10 -bb 1000 -m TEST -o Giraffe`   
