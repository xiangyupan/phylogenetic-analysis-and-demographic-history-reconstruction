# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 17:15:31 2018

@author: Pan Xiangyu
"""
import sys
if len(sys.argv) < 3:
    print('Usage: python3.5 '+sys.argv[0]+'[input cds.edit][input species name] [output fasta]')
    exit(1)
infile1 = open(sys.argv[1])
infile2 = sys.argv[2]
outfile=open(sys.argv[3],'w')
seq = ""
for line in infile1:
    line = line.strip().split("\t")
    print(line[0]+"\t"+str(len(line[1])))
    seq += line[1]
long = len(seq)
outfile.write('>'+infile2+"\n"+seq)
print(long)