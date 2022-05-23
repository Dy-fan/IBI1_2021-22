import re
seq = 'ATGCAATCGACTACGATCAATCGAGGGCC'
recognition_seq = re.compile('GAATTC')  # store the recognition sequence into a regular expression object
site_number = len(recognition_seq.findall(seq))  # calculate the number of recognition sites found in the sequence
if site_number > 0:  # at least 1 site can be found
    fragments_number = site_number + 1
    print(f'the total number of fragments into which this sequence would be cut is {fragments_number}')
else:  # no site can be found
    print('This sequence cannot be cut by EcoRI enzymes')
