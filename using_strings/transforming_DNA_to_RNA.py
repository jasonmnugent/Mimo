"""
use your knowledge of splitting and updating strings to transform 
DNA sequences into RNA sequences

DNA and RNA encode information about out genetic material.
We represent them as sequences of letters, where each letter
stands for a nucleotide
"""

# split the string to get 3 DNA sequences
sequence = "tatgctttcc#tataggtctg#ctattcaatg"
dna_list = sequence.split("#")
print(dna_list)

# convert them into RNA by replacing the letter 't' (Thymine) with 'u' (Uracil)
# use a for loop to go through every value in the list, and then use the .replace() function
# code an rna variable and assign it to the DNA sequence with replaced latters
for dna in dna_list:
    rna = dna.replace("t", "u")
    print(f"DNA: {dna} --> RNA: {rna}")