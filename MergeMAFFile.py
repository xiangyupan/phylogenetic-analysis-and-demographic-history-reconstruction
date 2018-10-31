# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""
Created on Tue Aug 15 17:43:10 2017
@Mail: minnglee@163.com
@Author: Ming Li
"""

import sys
import os
import argparse
import time
import re

def GetCommandLine():
    CommandLine = 'python3 {0}'.format(' '.join(sys.argv))
    return(CommandLine)
LogFile = None
def log(LogInfo):
    '''
    Output the LogInfo to log file
    '''
    global LogFile
    if sys.platform == 'linux':
        CurrentFolder = os.getcwd()
        LogFileName = re.split('/|\\\\',sys.argv[0].strip())
        LogFileName = LogFileName[-1].split('.')
        LogFileName = '{0}/{1}.log'.format(CurrentFolder,LogFileName[0])
        if LogFile: LogFile.write(LogInfo+'\n')
        else:
            LogFile = open(LogFileName,'w')
            LogFile.write(LogInfo+'\n')
    else:
        print(LogInfo)
def LoadMAFFileList():
    '''
    goat    AfricanBuffalo  /stor9000/apps/users/NWSUAF/2015060145/genomic_align/last_align/LastResultChr/1/AfricanBuffalo.1.final.maf
    goat    Argali  /stor9000/apps/users/NWSUAF/2015060145/genomic_align/last_align/LastResultChr/1/Argali.1.final.maf
    goat    BarbarySheep    /stor9000/apps/users/NWSUAF/2015060145/genomic_align/last_align/LastResultChr/1/BarbarySheep.1.final.maf
    '''
    List = []
    for line in args.input:
        line = line.strip().split()
        List.append(line[2])
    return List
def GetErrorInfo(file):
    File = open(file)
    for line in File:
        if re.search('error|ERROR|Error|command not found', line):
            print('error in {0}'.format(file))
            sys.exit()
    File.close()
def ReturnMaxFileName(Len):
    MaxFileName = 0
    while Len != 2:
        MaxFileName += Len//2+1
        Len = Len//2+1
    return MaxFileName
def MergeMAFFile():
    MAFFileList = LoadMAFFileList()
    ListLen = len(MAFFileList)
    NewList = []
    for i in range(ListLen//2):
        File1 = MAFFileList[i]
        File2 = MAFFileList[ListLen-1-i]
        Len = len(NewList)
        NewList.append(Len)
        os.system('echo "multiz {0} {1} 0 all > {3}{2}.maf" > {3}{2}.sh'.format(File1,File2,Len,args.path))
        os.system('chmod 755 {0}{1}.sh'.format(args.path,Len))
        os.system('jsub -q jynodequeue -R "rusage[res=1]span[hosts=1]" -M 100000000 -n 1 -o {1}{0}.o -e {1}{0}.e -J {0} {1}{0}.sh'.format(Len,args.path))
    if ListLen%2 != 0:
        os.system('cp {0} {2}{1}.maf'.format(MAFFileList[ListLen//2],Len+1,args.path))
        os.system('touch {0}{1}.o'.format(args.path,Len+1))
        os.system('touch {0}{1}.e'.format(args.path,Len+1))
        os.system('touch {0}{1}.sh'.format(args.path,Len+1))
        NewList.append(Len+1)
    MAFFileList = NewList
        
    LastFileName = len(MAFFileList)
    NewList = []
    while len(MAFFileList) >1 :
        ListLen = len(MAFFileList)
        for FileName in MAFFileList:
            if os.path.isfile('{0}{1}.e'.format(args.path,FileName)):
                GetErrorInfo('{0}{1}.e'.format(args.path,FileName))
                NewList.append(FileName)
        while len(NewList) >= 2:
            os.system('echo "multiz {3}{0}.maf {3}{1}.maf 0 all > {3}{2}.maf" > {3}{2}.sh'.format(NewList[0],NewList[1],LastFileName,args.path))
            os.system('chmod 755 {0}{1}.sh'.format(args.path,LastFileName))
            os.system('jsub -q jynodequeue -R "rusage[res=1]span[hosts=1]" -M 100000000 -n 1 -o {1}{0}.o -e {1}{0}.e -J {0} {1}{0}.sh'.format(LastFileName,args.path))
            os.system('rm {0}{1}.e'.format(args.path,NewList[0]))
            os.system('rm {0}{1}.e'.format(args.path,NewList[1]))
            MAFFileList.append(LastFileName)
            MAFFileList.remove(NewList.pop(0))
            MAFFileList.remove(NewList.pop(0))
            LastFileName += 1
        NewList = []
def main():
    print('Running...')
    log('The start time: {0}'.format(time.ctime()))
    log('The command line is:\n{0}'.format(GetCommandLine()))
    MergeMAFFile()
    log('The end time: {0}'.format(time.ctime()))
    print('Done!')
#############################Argument
parser = argparse.ArgumentParser(description=print(__doc__),formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('-i','--Input',metavar='File',dest='input',help='Input file',type=open,required=True)
parser.add_argument('-p','--path',metavar='Str',dest='path',help='MAF file path',type=str,default='./')
#parser.add_argument('-o','--Output',metavar='File',dest='output',help='Output file',type=argparse.FileType('w'),required=True)
args = parser.parse_args()
###########################
if __name__ == '__main__':
    main()
