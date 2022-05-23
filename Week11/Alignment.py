import pandas as pd
import re

with open('DLX5_human.fa') as Dhuman, open('DLX5_mouse.fa') as Dmouse, open('RandomSeq.fa') as Rseq:
    # get both the sequence and its name
    human = re.search(r'>([^ ]+).+\n([ARNDCQEGHILKMFPSTWYVBZX]+)', Dhuman.read())
    mouse = re.search(r'>([^ ]+).+\n([ARNDCQEGHILKMFPSTWYVBZX]+)', Dmouse.read())
    random = re.search(r'>([^ ]+).+\n([ARNDCQEGHILKMFPSTWYVBZX]+)', Rseq.read())
matrix = pd.read_excel('BLOSUM.xlsx', index_col=[0])


def seq_compare(seq1, seq2):
    """
    input seq1, seq2; both are match objects
    compare the two sequences; calculate the percentage of identical amino acids and the alignment score using BLOSUM
    return none
    """
    seq1_seq2 = 0
    same = 0
    link = ''
    space = ' '
    for i in range(len(min(seq1.group(2), seq2.group(2)))):
        index1 = seq1.group(2)[i]  # get each amino acid name
        index2 = seq2.group(2)[i]
        seq1_seq2 += matrix.loc[index1, index2]  # look up the score in BLOSUM using two amino acid names
        if index1 == index2:
            same += 1
            link += '|'
        else:
            link += ' '
        percentage = same / len(min(seq1.group(2), seq2.group(2)))
    print(f'comparison between {seq1.group(1)} and {seq2.group(1)}:')
    print(f'{seq1.group(1):12}{seq1.group(2)}\n{space:12}{link}\n{seq2.group(1):12}{seq2.group(2)}')
    print(f'the score of alignment is: {seq1_seq2}')
    print(f'the percentage of identical amino acids is: {percentage:.2%}\n')
    return


seq_compare(human, mouse)
seq_compare(human, random)
seq_compare(mouse, random)

