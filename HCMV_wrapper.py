import getTestData
import kallisto

import os
from Bio import Entrez
from Bio import SeqIO

SRA1 = 'SRR5660030'
SRA2 = 'SRR5660033'
SRA3 = 'SRR5660044'
SRA4 = 'SRR5660045'

#create project results folder
current_path = os.getcwd()
results = "/miniProject_Aditi_Patel"
os.mkdir(current_path + results)

#create and change to testdata folder directory
current_path = os.getcwd()
testdata = "/testdata"
os.mkdir(current_path + testdata)
os.chdir(current_path + testdata)

#CURRENT DIRECTORY: .../current_path/testdata
#1
getTestData.getTranscriptome(SRA1)
getTestData.getTranscriptome(SRA2)
getTestData.getTranscriptome(SRA3)
getTestData.getTranscriptome(SRA4)

#change to current directory
os.chdir(current_path)

#CURRENT DIRECTORY: .../current_path
#2
kallisto.getRefTransciptome()

kallisto.get_kallisto_index()

kallisto.run_kallisto_qaunt(SRA1)
kallisto.run_kallisto_qaunt(SRA2)
kallisto.run_kallisto_qaunt(SRA3)
kallisto.run_kallisto_qaunt(SRA4)

kallisto.kallisto_sample_table(SRA1,SRA2,SRA3,SRA4)
