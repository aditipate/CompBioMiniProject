#1.We would like to compare HCMV transcriptomes 2- and 6-days post-infection (dpi).
#First, retrieve the following transcriptomes from two patient donors from SRA and convert to paired-end fastq files.
#You can use wget (by constructing the path based on the SRR numbers for each of these samples).

import os

#create and change to testdata folder directory
current_path = os.getcwd()
testdata = "/testdata"
os.mkdir(current_path + testdata)
os.chdir(current_path + testdata)

#CURRENT DIRECTORY: .../current_path/testdata

#get Donor HMCV transcriptome
def getTranscriptome(SRRs):
    for SRR in SRRs:
        SRR_data_address = 'https://sra-downloadb.be-md.ncbi.nlm.nih.gov/sos2/sra-pub-run-11/'+ SRR + '/'+ SRR + '.1'
        wget_SRR = 'wget' + ' ' + SRR_data_address
        fastq_dump_SRR = 'fastq-dump -I --split-files' + ' ' + SRR + '.1'
        os.system(wget_SRR)                                                      #retrieve small subset of input reads or testdata using wget command
        os.system(fastq_dump_SRR)                                                #uncompress data and convert to paired-end fastq files using fastq-dump command


#change to current directory
os.chdir(current_path)

#CURRENT DIRECTORY: .../current_path