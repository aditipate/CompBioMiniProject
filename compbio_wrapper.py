#import python files
#import getData
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


#1
#Note: getData is not called in wrapper, instead testdata folder containing the first 10000 records from the paired-end fastq will be used by wrapper
#getData.getTranscriptome(SRRs)

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


