#import python files
import getTestData
import kallisto
import sleuth
import bowtie2
import spades
import contigs
import blast

#import packages + libraries
import os

#test data SRR ids
SRRs = ['SRR5660030', 'SRR5660033','SRR5660044','SRR5660045']

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
getTestData.getTranscriptome(SRRs)

#change to current directory
os.chdir(current_path)

#CURRENT DIRECTORY: .../current_path

#2
kallisto.getRefTranscriptome()
kallisto.get_kallisto_index()
kallisto.run_kallisto_qaunt(SRRs)
kallisto.kallisto_sample_table(SRRs)

#3
sleuth.run_sleuth()

#4
bowtie2.run_bowtie2(SRRs)
bowtie2.getReads(SRRs)

#5
spades.run_spades(SRRs)

#6
contigs.getContigsCount()

#7
contigs.getAssemblyLen()

#8
contigs.getLongContig()
blast.run_blast()

