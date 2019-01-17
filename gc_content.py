sequence = 'atgcggctgtgatgtagtcctttc'
def contentGC(seq):
    c = seq.count('c')
    g = seq.count('g')
    seqLength = len(seq)
    gcContent = 100 * float(c + g) / seqLength
    return gcContent

print contentGC(sequence)
