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

<h5> Clone Repository </h5> 

`git clone https://github.com/aditipate/CompBioMiniProject`

<h5> Move From Current Directory To Project Directory </h5>

`cd CompBioMiniProject/`

<h5> Run Wrapper </h5>

`python3 compbio_wrapper.py`
