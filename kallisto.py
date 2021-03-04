#2. We will quantify TPM in each sample using kallisto, but first we need to build a transcriptome index for HCMV (NCBI accession EF999921).
# Use Biopython to retrieve and generate the appropriate input and then build the index with kallisto. You will need to extract the CDS features from the GenBank format.
# Write the following to your log file (replace with the number of coding sequences in the HCMV genome): The HCMV genome (EF999921) has # CDS.

import os
import pandas as pd
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
    kallisto_index = 'time kallisto index -i HCMV_index.idx' + ' ' + HCMV_transcriptome
    os.system(kallisto_index)


#quantify the TPM of each CDS in each transcriptome with kallisto using quantification commands
def run_kallisto_qaunt(SRA):
    kallisto_quant_SRA = 'time kallisto quant -i HCMV_index.idx -o miniProject_Aditi_Patel/' + SRA + ' ' + '-b 30 -t 2' + ' ' + 'testdata/' + SRA + '.1_1.fastq' + ' ' + 'testdata/' + SRA + '.1_2.fastq'
    os.system(kallisto_quant_SRA)

#build a table of kallisto samples, conditions, and paths and then generate tab-delimited .txt file to be used as input in sleuth
def kallisto_sample_table(SRA1,SRA2,SRA3,SRA4):
    results = {'sample': [SRA1, SRA2, SRA3, SRA4], 'condition': ["2dpi", "6dpi", "2dpi", "6dpi"], 'path': ['miniProject_Aditi_Patel/' + SRA1, 'miniProject_Aditi_Patel/' + SRA2, 'miniProject_Aditi_Patel/' + SRA3, 'miniProject_Aditi_Patel/' + SRA4]}
    df = pd.DataFrame(results)
    kallisto_samples = open("kallisto_samples.txt", 'w')
    kallisto_samples.write(df.to_string(index=False,sep='\t'))
    kallisto_samples.close()


