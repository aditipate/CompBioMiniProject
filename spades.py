#5.Using the Bowtie2 output reads, assemble all four transcriptomes together to produce 1 assembly via SPAdes.
# Write the SPAdes command used to the log file.

import os

#run spades to assemble output reads (rate limiting step)
def run_spades(SRRs):
    spades = 'spades -k 55,77,99,127 -t 2 --only-assembler --pe1-1 ' + 'miniProject_Aditi_Patel/' + SRRs[0] + '.1.fastq --pe1-2 ' + 'miniProject_Aditi_Patel/' + SRRs[0] + '.2.fastq --pe2-1 '+ 'miniProject_Aditi_Patel/' + SRRs[1] + '.1.fastq --pe2-2 ' + 'miniProject_Aditi_Patel/' + SRRs[1] + '.2.fastq --pe3-1 ' + 'miniProject_Aditi_Patel/' + SRRs[2] + '.1.fastq --pe3-2 ' + 'miniProject_Aditi_Patel/' + SRRs[2] +'.2.fastq --pe4-1 ' + 'miniProject_Aditi_Patel/' + SRRs[3] + '.1.fastq --pe4-2 ' + 'miniProject_Aditi_Patel/' + SRRs[3] + '.2.fastq -o miniProject_Aditi_Patel/spades_output/'
    os.system(spades)
    miniProject_log = open("miniProject.log", "a")
    miniProject_log.write(spades + '\n')
    miniProject_log.close()

