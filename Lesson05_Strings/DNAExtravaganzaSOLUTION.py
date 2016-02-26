def codons(dna):
	return len(dna) / 3

def start(dna):
	return dna.find('ATG')

def stop(dna):
	first_stop = -1
	taa = dna.find('TAA')
	tag = dna.find('TAG')
	tga = dna.find('TGA')
	if taa > first_stop:
		first_stop = taa
	if tag > first_stop:
		first_stop = tag
	if tga > first_stop:
		first_stop = tga
	return first_stop

def gene(dna):
	beginning = start(dna)
	end = stop(dna) + 3
	return dna[beginning: end]

def transcription(dna):
	rna = ''
	for base in dna:
		if base == 'A':
			rna += 'U'
		elif base == 'T':
			rna += 'A'
		elif base == 'C':
			rna += 'G'
		elif base == 'G':
			rna += 'C'
	return rna

def dnaExtravaganza(dna):
	num_codons = codons(dna)
	beginning = start(dna)
	end = stop(dna) 
	orf = gene(dna)
	rna = transcription(dna)
	print "DNA: {0}\nCODONS: {1}\nSTART: {2}\nSTOP: {3}\nGENE: {4}\nRNA: {5}\n".format(dna, num_codons, beginning, end, orf, rna)

dnaExtravaganza("CAGTAGTAGCTACGACTATGCAGTCGATGCTAGTGACTGAACGTACGATAGCTGATAACGATGATGCATGTAGCTGA")
	
