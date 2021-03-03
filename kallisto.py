#2. We will quantify TPM in each sample using kallisto, but first we need to build a transcriptome index for HCMV (NCBI accession EF999921).
# Use Biopython to retrieve and generate the appropriate input and then build the index with kallisto. You will need to extract the CDS features from the GenBank format.
# Write the following to your log file (replace with the number of coding sequences in the HCMV genome): The HCMV genome (EF999921) has # CDS.

import os
from Bio import Entrez
from Bio import SeqIO

#build a transcriptome index for HCMV (NCBI accession EF999921)
def getRefTransciptome():
    Entrez.email = "apatel72@luc.edu"                                                            #YOUR_NAME@EMAIL.COM
    handle = Entrez.efetch(db="nucleotide", id=["EF999921"],rettype='gb', retmode="text")
    record = SeqIO.read(handle, "genbank")
    record.features = [feat for feat in record.features if feat.type == "CDS"]
    number_CDS = len(record.features)
    SeqIO.write(record, "HCMV_transcriptome.fasta", "fasta")

    miniProject_log = open("miniProject.log", "w")
    miniProject_log.write('The HCMV genome (EF999921) has' + ' ' + str(number_CDS) + ' ' + 'CDS' + '\n')
    miniProject_log.close()



#build the index of the reference transciptome with kallisto using indexing command
def get_kallisto_index():
    HCMV_transcriptome = "HCMV_transcriptome.fasta"
    kallisto_index = 'time kallisto index -i miniProject_Aditi_Patel/HCMV_index.idx' + ' ' + HCMV_transcriptome
    os.system(kallisto_index)


#Quantify the TPM of each CDS in each transcriptome with kallisto using quantification commands
def run_kallisto_qaunt(SRA):
    kallisto_quant_SRA = 'time kallisto quant -i miniProject_Aditi_Patel/HCMV_index.idx -o miniProject_Aditi_Patel/' + SRA + ' ' + '-b 30 -t 2' + 'testdata/' + SRA + '.1_1.fastq' + 'testdata/' + SRA + '.1_2.fastq'
    os.system(kallisto_quant_SRA)

