#5. Using the Bowtie2 output reads, assemble all four transcriptomes together to produce 1 assembly via SPAdes.
# Write the SPAdes command used to the log file.

import os


def spades(SRRs):
    run_spades = 'spades -k 55,77,99,127 -t 2 --only-assembler --pe1-1 ' + SRRs[0] + '.1.fastq --pe1-2 '+ SRRs[0] + '.2.fastq --pe2-1 '+ SRRs[1] + '.1.fastq --pe2-2 ' + SRRs[1] + '.2.fastq --pe3-1 ' + SRRs[2] + '.1.fastq --pe3-2 ' + SRRs[2] +'.2.fastq --pe4-1 ' + SRRs[3] + '.1.fastq --pe4-2 ' + SRRs[3] + '.2.fastq -o spades_output/'
    os.system(run_spades)
    miniProject_log = open("miniProject.log", "w")
    miniProject_log.write( run_spades + '\n')
    miniProject_log.close()


