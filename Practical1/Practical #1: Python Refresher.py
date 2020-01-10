v = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'
k = 'ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT'
w = 'AAAACCCGGT'
s = 'GAGCCTACTAACGGGAT'
t = 'CATCGTAATGACGGCCT'
Sequence_header = ("ABC123", "DEF456", "HIJ789")
DNA_sequence = ("ATCGTACGATCGATCGATCGCTAGACGTATCG", "actgatcgacgatcgatcgatcacgact", "ACTGAC-ACTGT--ACTGTA----CATGTG")


def Counting_DNA_Nucleotides(v):
    A = 0
    C = 0
    G = 0
    T = 0
    value = 0
    for i in v:
        if i == 'A':
            A += 1
        elif i == 'C':
            C += 1
        elif i == 'G':
            G += 1
        elif i == 'T':
            T += 1
    return A, C, G, T


print(Counting_DNA_Nucleotides(v), "\n")


def Calculating_AT_content(k):
    AT = 0

    for i in k:
        if i == "A":
            AT += 1
        elif i == "T":
            AT += 1

    AT_content = (AT * 100) / len(k)
    return (AT_content)


print(Calculating_AT_content(k), "%\n")


def Complementing_a_strand_of_DNA(w):
    w = w[::-1]

    a = w.replace('A', 'R')
    b = a.replace('T', 'A')
    c = b.replace('R', 'T')

    d = c.replace('C', 'R')
    e = d.replace('G', 'C')
    f = e.replace('R', 'G')
    return(f)


print(Complementing_a_strand_of_DNA(w), "\n")


def Counting_point_mutations(s, t):
    result = 0

    for i, j in zip(s, t):
        if i != j:
            result += 1

    return(result)


print (Counting_point_mutations(s, t), "\n")


def Writing_a_FASTA_file(Sequence_header, DNA_sequence):
    f = open("FASTA_file.txt", "w+")
    for i, j in zip(Sequence_header, DNA_sequence):
        j = j.upper()
        for w in j:
            if w not in "ACGT":
                j = j.replace(w, '')
        f.write(">sequence_" + i + "\n" + j + "\n")
    f.close()
    return


print(Writing_a_FASTA_file(Sequence_header, DNA_sequence), "\n")


def Writing_multiples_FASTA_files(Sequence_header, DNA_sequence):

    for i, j in zip(Sequence_header, DNA_sequence):
        j = j.upper()
        for w in j:
            if w not in "ACGT":
                j = j.replace(w, '')
        file_name = i + ".fasta"

        f = open(file_name, "w+")
        f.write(">sequence_" + i + "\n" + j + "\n")
        f.close()
    return


print(Writing_multiples_FASTA_files(Sequence_header, DNA_sequence), "\n")


def Conditional_tests():
