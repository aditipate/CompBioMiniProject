from Bio import SeqIO


#6.Write Python code to calculate the number of contigs with a length > 1000
def getContigsCount():
    spades_contigs = open("miniProject_Aditi_Patel/spades_output/contigs.fasta")
    contigs_min = open("miniProject_Aditi_Patel/contigs_min1000.fasta", "w")
    count = 0
    for contig in SeqIO.parse(spades_contigs,"fasta"):                                #for contig in assembly contigs
        if len(contig.seq) > 1000:                                                    #if contig length > 1000
            count = count + 1                                                         #increment count

            contigs_min.write(">" + str(contig.id) + "\n")
            contigs_min.write(str(contig.seq) + "\n")

    spades_contigs.close()

    miniProject_log = open("miniProject.log", "a")
    miniProject_log.write('There are' + ' ' + str(count) + ' ' + 'contigs > 1000 bp in the assembly' + '\n')
    miniProject_log.close()

#7.Write Python code to calculate the length of the assembly (the total number of bp in all of the contigs > 1000 bp in length)
def getAssemblyLen():
    contigs_min = open("miniProject_Aditi_Patel/contigs_min1000.fasta")
    total_bps = 0
    for contig in SeqIO.parse(contigs_min,"fasta"):                                   #for contig in contigs length > 1000 or minimum of 1000
        contig_bps = len(contig.seq)                                                  #get length or number of bps
        total_bps = total_bps + contig_bps                                            #add to total number of bps

    contigs_min.close()

    miniProject_log = open("miniProject.log", "a")
    miniProject_log.write('There are' + ' ' + str(total_bps) + ' ' + 'bp in the assembly' + '\n')
    miniProject_log.close()


#8a.Write Python code to retrieve the longest contig from your SPAdes assembly
def getLongContig():
    contigs_min = open("miniProject_Aditi_Patel/contigs_min1000.fasta")
    blast_contig = open("miniProject_Aditi_Patel/blast_contig.fasta", 'w')
    longest_id = ''
    longest_seq = ''
    for contig in SeqIO.parse(contigs_min, "fasta"):                                    #for contig in contigs length > 1000 or minimum of 1000
        if(len(contig.seq) > len(longest_seq)):                                         #if current contig length is greater than length of longest contig
            longest_id = contig.id                                                      #set current contig as longest contig, record contig id and seq
            longest_seq = contig.seq

    contigs_min.close()

    blast_contig.write(">" + str(longest_id) + "\n")
    blast_contig.write(str(longest_seq) + "\n")
    blast_contig.close()


