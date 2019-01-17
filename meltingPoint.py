sequence = 'ACTAATGCCTGA'

def meltingPoint(seq):
    seqLength = len(seq)
    a = seq.count('A')
    t = seq.count('T')
    g = seq.count('G')
    c = seq.count('C')
    strongBonds = g + c
    weakBonds = a + t
    if seqLength < 14:
        meltingPoint = 4 * strongBonds + 2 * weakBonds
    else:
        meltingPoint = 64.9 + 41 * (strongBonds - 16.4) / seqLength
    return meltingPoint
# print meltingPoint(sequence)

def getRNASequence(dna):
    flippedRna = ''
    for i in dna:
        if i == 'A':
            i = 'U'
        elif i == 'C':
            i = 'G'
        elif i == 'T':
            i = 'A'
        elif i == 'G':
            i = 'C'
        flippedRna += i
        rna = flippedRna[::-1]
    return rna
# print getRNASequence(sequence)



codons = {
"UUU" : "F",
"CUU" : "L",
"AUU" : "I",
"GUU" : "V",
"UUC" : "F",
"CUC" : "L",
"AUC" : "I",
"GUC" : "V",
"UUA" : "L",
"CUA" : "L",
"AUA" : "I",     
"GUA" : "V",
"UUG" : "L",
"CUG" : "L",
"AUG" : "M",
"GUG" : "V",
"UCU" : "S",
"CCU" : "P",
"ACU" : "T",
"GCU" : "A",
"UCC" : "S",
"CCC" : "P",
"ACC" : "T",
"GCC" : "A",
"UCA" : "S",
"CCA" : "P",
"ACA" : "T",
"GCA" : "A",
"UCG" : "S",
"CCG" : "P",
"ACG" : "T",
"GCG" : "A",
"UAU" : "Y",
"CAU" : "H",
"AAU" : "N",
"GAU" : "D",
"UAC" : "Y",
"CAC" : "H",
"AAC" : "N",
"GAC" : "D",
"UAA" : "Stop",
"CAA" : "Q",
"AAA" : "K",
"GAA" : "E",
"UAG" : "Stop",
"CAG" : "Q",
"AAG" : "K",
"GAG" : "E",
"UGU" : "C",
"CGU" : "R",
"AGU" : "S",
"GGU" : "G",
"UGC" : "C",
"CGC" : "R",
"AGC" : "S",
"GGC" : "G",
"UGA" : "Stop",
"CGA" : "R",
"AGA" : "R",
"GGA" : "G",
"UGG" : "W",
"CGG" : "R",
"AGG" : "R",
"GGG" : "G"
}

def getCodons(dna):
    aminos=[]
    aminosFrequencies = codons.values()
    rna = getRNASequence(dna)
    for i in range(0, len(rna), 3):
        aminos.append(codons[rna[i:i+3]])
    for i in aminosFrequencies:
        print i, aminos.count(i)

print getCodons(sequence)

