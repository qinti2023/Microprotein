# Amino acid sequences with a length greater than 20
import iupred3_lib
input = open("./test.txt","r")
result = open("result.txt","w")
for line in input:
    output = open("iupred.txt","w")
    identifier, sequence = line.strip().split('\t')
    output.write(f'>{identifier}\n{sequence}\n')
    output.close()
    sequence = iupred3_lib.read_seq("./iupred.txt")
    iupred2_result = iupred3_lib.iupred(sequence,"short")
    total_score = 0
    num_positions = len(sequence)
    for pos, residue in enumerate(sequence):
        total_score += iupred2_result[0][pos]
    average_score = total_score / num_positions
    result.write(f'{identifier}\t{sequence}\t{average_score}\n')
result.close()

