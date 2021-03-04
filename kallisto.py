#2. We will quantify TPM in each sample using kallisto, but first we need to build a transcriptome index for HCMV (NCBI accession EF999921).
# Use Biopython to retrieve and generate the appropriate input and then build the index with kallisto. You will need to extract the CDS features from the GenBank format.
# Write the following to your log file (replace with the number of coding sequences in the HCMV genome): The HCMV genome (EF999921) has # CDS.

import os
import pandas as pd
from Bio import Entrez
from Bio import SeqIO


#build a transcriptome index for HCMV (NCBI accession EF999921)
def getRefTranscriptome():
    hcmv_EF999921 = open('HCMV_EF999921.fasta', 'w')
    Entrez.email = "apatel72@luc.edu"
    handle = Entrez.efetch(db="nucleotide", id=["EF999921"], rettype='fasta')
    records = list(SeqIO.parse(handle, "fasta"))
    hcmv_EF999921.write('>' + str(records[0].description)+ '\n' + str(records[0].seq))
    hcmv_EF999921.close()

    hcmv_EF999921_CDS = open('HCMV_EF999921_CDS.fasta', 'w')
    handle = Entrez.efetch(db='nucleotide', id='EF999921', rettype='gb', retmode='text')
    count_CDS = 0
    for record in SeqIO.parse(handle, 'genbank'):
        for feature in record.features:
            if feature.type == "CDS":
                count_CDS = count_CDS + 1
                hcmv_EF999921_CDS.write('>' + str(feature.qualifiers['protein_id']).replace('[', '').replace(']', '').replace("'","") + '\n' + str(feature.location.extract(record).seq) + '\n')
    hcmv_EF999921_CDS.close()

    miniProject_log = open("miniProject.log", "w")
    miniProject_log.write('The HCMV genome (EF999921) has' + ' ' + str(count_CDS) + ' ' + 'CDS' + '\n')
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
    kallisto_samples.write(df.to_csv(index=False,sep='\t'))
    kallisto_samples.close()

def kallisto_table(SRA1,SRA2,SRA3,SRA4):
    list_srr = [SRA1,SRA2,SRA3,SRA4]
    kallisto_samples = open("kallisto_table.txt", 'w')
    condition_1 = '2dpi'
    condition_2 = '6dpi'
    kallisto_samples.write('sample' + '\t' + 'condition' + '\t' + 'path' + '\n')
    for srr in list_srr:
        path = "miniProject_Aditi_Patel/" + srr
        if int(srr[3:])%2==0:
            kallisto_samples.write(str(srr) + '\t' + condition_1 + '\t' + str(path) + '\n')
        else:
            kallisto_samples.write(str(srr) + '\t' + condition_2 + '\t' + str(path) + '\n')

    kallisto_samples.close()






