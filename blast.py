#.8 Use the longest contig as blast+ input to query the nr nucleotide database limited to members of the Betaherpesvirinae subfamily.
#You will need to make a local database of just sequences from the Betaherpesvirinae subfamily.
#Identify the top 10 hits

import os
import csv

def parse_blast(filename,headers):
    x=[]
    blast_results = open(filename,'r')
    rows = csv.DictReader(blast_results,headers,delimiter=',')
    for row in rows:
        x.append(row)
    blast_results.close()
    return x

def run_blast():
    betaherpes_genome = 'betaherpes.fasta'
    blast_output = "blast_output.csv"
    make_db = "makeblastdb -in " + betaherpes_genome + " -out betaherpes -title betaherpes -dbtype nucl"
    os.system(make_db)
    blast_contig = "blast_contig.fasta"
    blast = 'blast+ -query ' + blast_contig + ' -db betaherpes -out ' + blast_output + ' -outfmt "10 sacc pident length qstart qend sstart send bitscore evalue stitle"'
    os.system(blast)

    headers = ['sacc', 'pident', 'length', 'qstart', 'qend', 'sstart', 'send', 'bitscore', 'evalue', 'stitle']
    x = parse_blast(blast_output, headers)
    top_hits = x[:10]


    miniProject_log = open("miniProject.log", "a")
    spaced_headers = '\t'.join(headers)
    miniProject_log.write(spaced_headers + '\n')
    for hit in top_hits:
        hit_values = list(hit.values())
        hit_values = [str(i) for i in hit_values]
        hit_values = "\t".join(hit_values)
        miniProject_log.write(hit_values + '\n')
    miniProject_log.close()


