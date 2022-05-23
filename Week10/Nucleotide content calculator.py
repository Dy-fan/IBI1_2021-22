import re


def nucleotide_cal(sequence):
    """
     take a single string variable describing a DNA strand as input
     calculate the percentage of all four base A,T,G,C in the sequence
     return None
    """
    total = len(sequence)
    for base in ['A', 'T', 'G', 'C']:  # to calculate for the four bases in turn
        # calculate the number of a certain base in the sequence
        number = len(re.findall(f'{base}', sequence, re.I))  # re.I can ignore case when matching
        percentage = number / total
        print(f'The percentage of {base} in this sequence is {percentage:.2%}')
        # :.2% in {} makes the value into percent with two decimal places
    return


# example of how this function be used
DNA = 'ATCGATCG'  # input the DNA sequence as string
nucleotide_cal(DNA)
