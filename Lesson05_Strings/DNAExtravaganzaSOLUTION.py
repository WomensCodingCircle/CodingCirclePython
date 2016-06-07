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



# dna ='GGCATGAAAGTCAGGGCAGAGCCATCTATTGCTTACATTTGCTTCTGACACAACTGTGTTCACTAGCAACCTCAAACAGACACCATGGTGCACCTGACTCCTGAGGAGAAGTCTGCCGTTACTGCCCTGTGGGGCAAGGTGAACGTGGATGAAGTTGGTGGTGAGGCCCTGGGCAGGTTGGTATCAAGGTTACAAGACAGGTTTAAGGAGACCAATAGAAACTGGGCATGTGGAGACAGAGAAGACTCTTGGGTTTCTGATAGGCACTGACTCTCTCTGCCTATTGGTCTATTTTCCCACCCTTAGGCTGCTGGTGGTCTACCCTTGGACCCAGAGGTTCTTTGAGTCCTTTGGGGATCTGTCCACTCCTGATGCTGTTATGGGCAACCCTAAGGTGAAGGCTCATGGCAAGAAAGTGCTCGGTGCCTTTAGTGATGGCCTGGCTCACCTGGACAACCTCAAGGGCACCTTTGCCACACTGAGTGAGCTGCACTGTGACAAGCTGCACGTGGATCCTGAGAACTTCAGGGTGAGTCTATGGGACCCTTGATGTTTTCTTTCCCCTTCTTTTCTATGGTTAAGTTCATGTCATAGGAAGGGGAGAAGTAACAGGGTACAGTTTAGAATGGGAAACAGACGAATGATT'
dna = 'GGGATGTTTGGGCCCTACGGGCCCTGATCGGCT'

# each function is a neat little bit of code with comments
# the name of the function reflects it's 'function'
# a function has well-defined input and output
# a function can call other functions

def startCodonIndex(seq):
    # input: list of CAPs characters corresponding to DNA sequence  
    # output: index of first letter of start codon; return -1 if none are found
    ind=seq.find('ATG')
    return ind

def stopCodonIndex(seq, start_codon):
    # input: list of CAPs characters corresponding to DNA sequence and index of start codon  
    # output: index of first stop codon; return -1 if none are found
    ii = start_codon+3
    st_codon = -1
    while st_codon == -1 and ii < len(seq):
        codon = seq[ii:(ii+3)]
        if codon == 'TAA':
            st_codon = ii
        if codon == 'TGA':
            st_codon = ii
        if codon == 'TAG':
            st_codon = ii
        ii += 3
    return st_codon

def codingDNA(seq):
    # input: list of CAPs characters corresponding to DNA   
    # output: coding sequence only, including start and stop codons 
    aa = startCodonIndex(seq)
    zz = stopCodonIndex(seq, startCodonIndex(seq))
    new_seq=dna[aa:(zz+3)]  # why the +3?
    return new_seq

def numCodons(seq):
    # calculate the number of codons in the gene
    # input: coding DNA sequence
    # output: number of codons
    coding_dna=codingDNA(seq)
    return len(coding_dna)/3

def dnaToRna(seq): # a better version than above; why?
    # Transcription: (A->U), (T->A), (C->G), (G->C)
    # input: DNA coding squence
    # ouput: RNA sequence
    rna_seq=''
    for base in seq:
        if base == 'A':
            rna_seq += 'U'
        if base == 'T':
            rna_seq += 'A'
        if base == 'C':
            rna_seq += 'G'
        if base == 'G':
            rna_seq += 'C'
    return rna_seq
                        

# calling the functions

start =  startCodonIndex(dna)
stop = stopCodonIndex(dna, start)
coding_dna=codingDNA(dna) # why the +3?
coding_rna = dnaToRna(coding_dna)

print 'start codon :    '.format(start)
print 'dna :            '.format(dna)
print 'coding dna:      '.format(coding_dna)
print 'transcribed rna: '.format(coding_rna)
print 'number of codons '.format(numCodons(coding_dna))
