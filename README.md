# Computational Biology Mini Project 

## Project Background 
Human herpesvirus 5 is also known as Human cytomegalovirus and is typically abbreviated as HCMV.
From Wikipedia: Although they may be found throughout the body, HCMV infections are frequently associated with the
salivary glands. HCMV infection is typically unnoticed in healthy people, but can be life-threatening for the
immunocompromised, such as HIV-infected persons, organ transplant recipients, or newborn infants. Congenital
cytomegalovirus infection can lead to significant morbidity and even death. After infection, HCMV remains latent within
the body throughout life and can be reactivated at any time. Eventually, it may cause mucoepidermoid carcinoma and
possibly other malignancies such as prostate cancer

![alt text](https://assets.teenvogue.com/photos/5633c437315908291450e9af/1:1/w_350%2Ch_350%2Cc_limit/herpes.jpg)

The Comp Bio Mini Project aims to compare the HCMV transcriptomes from 2 patient donors 2- and 6-days post-infection (dpi) and to observe the genetic diversity of the HMVC by comparing the patient samples to other publicly available strains inorder to find the ones that are the most similar.  

A Python wrapper was developed to automate the execution of various Bioinformatics software tools. 

## Software Requirements: 
* Linux/Unix
* Python3
    * os
    * Pandas
    * Biopython
        * Entrez
        * SeqIO
* Kallisto
* Bowtie2
* SPades
* BLAST+

## Run The Wrapper: 

<h5> Clone Repository: </h5> 

`git clone https://github.com/aditipate/CompBioMiniProject`

<h5> Move Into Project Directory: </h5>

`cd CompBioMiniProject/`

<h5> Run Wrapper: </h5>

`python3 compbio_wrapper.py`

## Folders and Scripts: 

**testdata:** folder containing test data </br>

**compbio_wrapper.py:** python wrapper, calls other python scripts, creates various output files, writes significant output results to miniProject.log </br> 

**getTestData.py:** retrieves transcriptomes from two patient donors from SRA and convert to paired-end fastq files </br>
***Note:*** *getTestData.py is not called in the python wrapper due to lengthy runtime of full length transcriptomes. However, a testdata folder containing shortened paired-end fastq files has been provided in the repository which the wrapper will use to run the pipeline* </br>

**kallisto.py:** builds a transcriptome index for HCMV (NCBI accession EF999921), quantifies TPM in each sample using Kallisto, creates kallisto output table </br>

**sleuth.R:** reads in kallisto output table to create a sleuth object, performs the likelihood ratio test for differential expression between conditions </br>

**sleuth.py** writes significant sleuth output to miniProject.log </br>

**bowtie2.py:** creates an index for HCMV (NCBI accession EF999921), saves the reads that map to the HCMV index for use in assembly </br>

**spades.py:** uses reads from Bowtie2 mapping to produce 1 assembly via SPAdes </br>

**contigs.py:** from SPades assembly calculates the number of contigs with a length > 1000, calculates the length of the assembly, finds longest contig </br>

**blast.py:**  uses longest contig as blast+ input to query the nr nucleotide database limited to members of the Betaherpesvirinae subfamily

## Output: 

**miniProject.log:** contains significant results from running the pipeline including # CDS in the HCMV genome, significant (FDR < 0.05) sleuth results, the number of reads in each transcriptome before and after the Bowtie2 mapping, the number of contigs with a length > 1000, the length of the assembly, and the top 10 BLAST hits </br>

**miniProject_Aditi_Patel:** contains any significant files generated from running software tools

