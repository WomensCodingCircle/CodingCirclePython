# A little bit of molecular biology
# Codons are non-overlapping triplets of nucleotides. 
# ATG CCC CTG GTA ... - this corresponds to four codons; spaces added for emphasis

# The start codon is 'ATG'

# Stop codons can be 'TGA' , 'TAA', or 'TAG', but they must be 'in frame' with the start codon. The first stop codon usually determines the end of the gene. 
# In other words:
# 'ATGCCTGA...' - here TGA is not a stop codon, because the T is part of CCT
# 'ATGCCTTGA...' - here TGA is a stop codon because it is in frame (i.e. a multiple of 3 nucleic acids from ATG)

# The gene is start codon to stop codon, inclusive 
# Example"
# dna - GGCATGAAAGTCAGGGCAGAGCCATCTATTTGAGCTTAC
# gene - ATGAAAGTCAGGGCAGAGCCATCTATTTGA



#dna ='GGCATGAAAGTCAGGGCAGAGCCATCTATTGCTTACATTTGCTTCTGACACAACTGTGTTCACTAGCAACCTCAAACAGACACCATGGTGCACCTGACTCCTGAGGAGAAGTCTGCCGTTACTGCCCTGTGGGGCAAGGTGAACGTGGATGAAGTTGGTGGTGAGGCCCTGGGCAGGTTGGTATCAAGGTTACAAGACAGGTTTAAGGAGACCAATAGAAACTGGGCATGTGGAGACAGAGAAGACTCTTGGGTTTCTGATAGGCACTGACTCTCTCTGCCTATTGGTCTATTTTCCCACCCTTAGGCTGCTGGTGGTCTACCCTTGGACCCAGAGGTTCTTTGAGTCCTTTGGGGATCTGTCCACTCCTGATGCTGTTATGGGCAACCCTAAGGTGAAGGCTCATGGCAAGAAAGTGCTCGGTGCCTTTAGTGATGGCCTGGCTCACCTGGACAACCTCAAGGGCACCTTTGCCACACTGAGTGAGCTGCACTGTGACAAGCTGCACGTGGATCCTGAGAACTTCAGGGTGAGTCTATGGGACCCTTGATGTTTTCTTTCCCCTTCTTTTCTATGGTTAAGTTCATGTCATAGGAAGGGGAGAAGTAACAGGGTACAGTTTAGAATGGGAAACAGACGAATGATT'
dna = 'GGGATGTTTGGGCCCTACGGGCCCTGATCGGCT'

def startCodonIndex(seq):
    # input: list of CAPs characters corresponding to DNA sequence  
    # output: index of first letter of start codon; return -1 if none are found
    start_idx = seq.find('ATG')
    return start_idx

def stopCodonIndex(seq, start_codon):
    # input: list of CAPs characters corresponding to DNA sequence and index of start codon  
    # output: index of first stop codon; return -1 if none are found
    stop_idx = -1
    codon_length = 3
    search_start = start_codon + codon_length
    search_stop = len(seq)

    for i in range(search_start, search_stop, codon_length):
        codon = seq[i: i+codon_length]
        if codon == "TAA" or codon == "TGA" or codon == "TAG":
            stop_idx = i 
            break
    return stop_idx

def codingDNA(seq):
    # input: list of CAPs characters corresponding to DNA   
    # output: coding sequence only, including start and stop codons 
    start_idx = startCodonIndex(seq)
    stop_idx = stopCodonIndex(seq, start_idx)
    codon_length = 3
    new_seq = dna[start_idx: stop_idx + codon_length] 
    return new_seq

def numCodons(seq):
    # calculate the number of codons in the gene
    # input: coding DNA sequence
    # output: number of codons
    codon_length = 3
    num_codons = len(seq) / codon_length
    # You don't need to run this line in python 2 because
    # of integer division.
    num_codons = int(num_codons)
    return num_codons

def transcription(seq): 
    # Transcription: (A->U), (T->A), (C->G), (G->C)
    # input: DNA coding squence
    # ouput: RNA sequence
    rna_seq=''
    for base in seq:
        if base == "A":
            rna_seq += "U"
        if base == "T":
            rna_seq += "A"
        if base == "C":
            rna_seq += "G"
        if base == "G":
            rna_seq += "C"
    return rna_seq
                        

# calling the functions

# It would be more accurate to calculate the number of codons from coding_dna
codons = numCodons(dna)
start =  startCodonIndex(dna)
stop = stopCodonIndex(dna, start)
coding_dna = codingDNA(dna) 
coding_rna = transcription(coding_dna)

print("DNA: {}".format(dna))
print("CODONS: {}".format(codons))
print("START: {}".format(start))
print("STOP: {}".format(stop))
print("CODING DNA: {}".format(coding_dna))
print("TRANSCRIBED RNA: {}".format(coding_rna))
