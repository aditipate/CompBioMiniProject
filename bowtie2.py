#4. Using Bowtie2, create an index for HCMV (NCBI accession EF999921).
#Next, save the reads that map to the HCMV index for use in assembly.
# Write to your log file the number of reads in each transcriptome before and after the Bowtie2 mapping.
#For instance, if I was looking at the Donor 1 (2dpi) sample, I would write to the log (numbers here are arbitrary):
#Donor 1 (2dpi) had 230000 read pairs before Bowtie2 filtering and 100000 read pairs after.

import os

def run_bowtie2(SRRs):
    bowtie2_index = "bowtie2-build HCMV_EF999921.fasta HCMV"
    for SRR in SRRs:
        bowtie2 = 'bowtie2 --quiet --no-unal --al-conc ' + SRR + '.fastq -x HCMV -1 ' + 'testdata/' + SRR + '.1_1.fastq -2 ' + 'testdata/' + SRR + '.1_2.fastq -S ' + SRR + '_map.sam'
        os.system(bowtie2_index)
        os.system(bowtie2)

#find the number of reads in each transcriptome before and after the Bowtie2 mapping
def getReads(SRRs):
    for i in range(0,len(SRRs)-1):
        if i == 0:
            donor = "Donor 1 (2dpi)"
        elif i == 1:
            donor = "Donor 1 (6dpi)"
        elif i == 2:
            donor = "Donor 3 (2dpi)"
        elif i ==3:
            donor = "Donor 3 (6dpi)"

        beforeBow_1 = open('testdata/' + str(SRRs[i])+'.1_1.fastq').readlines()
        beforeBow_2 = open('testdata/' + str(SRRs[i])+'.1_2.fastq').readlines()
        before_reads = (len(beforeBow_1) + len(beforeBow_2))/8

        afterBow_1 = open(str(SRRs[i])+'.1.fastq').readlines()
        afterBow_2 = open(str(SRRs[i])+'.2.fastq').readlines()
        after_reads = (len(afterBow_1) + len(afterBow_2))/8

        miniProject_log = open("miniProject.log", "a")
        miniProject_log.write(donor + "had " + str(before_reads) + " read pairs before Bowtie2 filtering and " + str(after_reads) + " read pairs after." + "\n")
        miniProject_log.close()












