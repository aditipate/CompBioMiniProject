#3.Quantify the TPM of each CDS in each transcriptome using kallisto and use these results as input to find differentially expressed genes between the two timepoints (2pi and 6dpi) using the R package sleuth.
# Write the following details for each significant transcript (FDR < 0.05) to your log file, include a header row, and tab-delimit each item: target_id test_stat pval qval

import os

def run_sleuth():
    sleuth = 'sleuth.R'
    os.system(sleuth)
    with open('miniProject_Aditi_Patel/sleuth_output.txt') as sleuth_output:
        with open("miniProject.log", "a") as miniProject_log:
            for line in sleuth_output:
                miniProject_log.write(line)


