# Here are inputs example I use in my function.  
v = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'
k = 'ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT'
w = 'AAAACCCGGT'
s = 'GAGCCTACTAACGGGAT'
t = 'CATCGTAATGACGGCCT'

# For exercise 5 and 6 I m asked to read values of a board, rather than creating and using a csv file (which I am asked to use later), I prefer creating 2 lists (which gives the same at the end as a csv file)
Sequence_header = ("ABC123", "DEF456", "HIJ789")
DNA_sequence = ("ATCGTACGATCGATCGATCGCTAGACGTATCG", "actgatcgacgatcgatcgatcacgact", "ACTGAC-ACTGT--ACTGTA----CATGTG")


# Exercise 1
def Counting_DNA_Nucleotides(v):
    # I itterate each base pair count to 0
    A = 0
    C = 0
    G = 0
    T = 0
    for i in v:     # I go through each nucleotides of the sequence one by one and itterate the base pair count
        if i == 'A':
            A += 1
        elif i == 'C':
            C += 1
        elif i == 'G':
            G += 1
        elif i == 'T':
            T += 1
            
    return A, C, G, T       # My function return the number of each nucleotide in the sequence


print(Counting_DNA_Nucleotides(v), "\n")        # Here I print the output of the function I am calling, then I skip a line


# Exercise 2
def Calculating_AT_content(k):
    k = k.upper()       # This line is useful because I use this function for exercise 7 and the DNA strands are in lower case

    A, C, G, T = Counting_DNA_Nucleotides(k)        # I call the function I build above to get the base pair count of each nucleotide
    AT = A + T                                      # Then I calculate the total AT amount

    # Another method to obtain total AT amount is showcase below :
    # AT = 0            # Here I iterate total AT amount to 0 
    # for i in k:       # Here I go through each nucleotides of the sequence one by one and itterate the total AT amount
    #     if i == "A":
    #         AT += 1
    #     elif i == "T":
    #         AT += 1
    
    AT_content = (AT * 100) / len(k)            # Here is the calculus to obtain the AT content in %
    return (AT_content)


print(Calculating_AT_content(k), "%\n")


# Exercise 3
def Complementing_a_strand_of_DNA(w):
    w = w[::-1]                 # Here I reverse the DNA strand by reading it upside down and assignating it to my stran name, so my new strand is reverse

    # Here I use a made up nucelotide (R) to help me replace each nucleotide one by one.
    # In the first bloc I replace A by T and T by A
    a = w.replace('A', 'R')
    b = a.replace('T', 'A')
    c = b.replace('R', 'T')
    # In the first bloc I replace C by G and G by C
    d = c.replace('C', 'R')
    e = d.replace('G', 'C')
    f = e.replace('R', 'G')
    return(f)


print(Complementing_a_strand_of_DNA(w), "\n")


# Exercise 4
def Counting_point_mutations(s, t):
    result = 0      # Number of mutations

    for i, j in zip(s, t):          # With this method I can go through both list at the same time
        if i != j:
            result += 1

    return(result)


print (Counting_point_mutations(s, t), "\n")


# Exercise 5
def Writing_a_FASTA_file(Sequence_header, DNA_sequence):
    f = open("FASTA_file.txt", "w+")                    # Here I create and write a Fasta file
    for i, j in zip(Sequence_header, DNA_sequence):
        j = j.upper()                                   # I put in upper case if it is not the case my DNA sequence
        for w in j: 
            if w not in "ACGT":                         # I remove every character that is not A, C, T or G of my DNA sequence
                j = j.replace(w, '')
        f.write(">sequence_" + i + "\n" + j + "\n")
    f.close()
    return          # My function returns nothing, but calling it will create a Fasta file and write in it


print(Writing_a_FASTA_file(Sequence_header, DNA_sequence), "\n")


# Exercise 6
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


# Exercise 7
def Conditional_tests():
    import csv

    # I decided to create multiples lists which correspond to each exercise I am asked to complete, It is less nicely presented as if I just used the print option, but the data will be more easily accesible
    Q1 = [] 
    Q2 = [] 
    Q3 = []
    Q4 = [] 
    Q5 = ""

    with open('data - data.csv', newline='') as csvfile:                    # I open the csv file attached to my exercise
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')      

        # It will read each row of my file:
        for row in spamreader:

            # Q1: Gene names for all genes belonging to Drosophila melanogaster or Drosophila simulans
            if row[0] == 'Drosophila melanogaster' or 'Drosophila simulans':
                Q1.append(row[2])

            # Q2: Gene names for all genes between 90 and 110 bases long
            if len(row[1]) > 90 and len(row[1]) < 110:
                Q2.append(row[2])

            # Q3: Gene names for all genes whose AT cotent is less than 0.5 and whose expression level is greater than 200
            if int(row[3]) > 200 and Calculating_AT_content(row[1]) < 50.0:     # here I right 50.0 because 0.5 is equivalent to 50%, and I want it to be a float like the result of the function I call
                Q3.append(row[2])

            # Q4: Gene names for all genes whose name begins with "k" or "h" except those of Drosophila melanogaster
            if row[2][0] == "k" or row[2][0] == "h":
                if row[0] !=  'Drosophila melanogaster':
                    Q4.append(row[2])

            # Q5: Gene names and AT conetent details
            a = Calculating_AT_content(row[1])
            if a > 65.0:
                b = "high"
            elif a < 45.0:
                b = "low"
            else:
                b = "medium"
            Q5 += "The gene is named " + row[2] + " and its AT content is " + b + " : " + str(a) + " .  \n "

    # To give more readible results, I decided to print directly in my function (in oposite to printing what my function returns)            
    print(" Q1: ", Q1, "\n Q2: ", Q2,"\n Q3: ", Q3, "\n Q4: ", Q4, "\n Q5: ", Q5)


    return Q1, Q2, Q3, Q4, Q5

Conditional_tests()
