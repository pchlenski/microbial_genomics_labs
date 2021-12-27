#!/usr/bin/python
import argparse

def get_options():
	description = "Match patterns within strings"
	parser = argparse.ArgumentParser(description = description,prog = 'patternCount.py')
	parser.add_argument('sequence', action='store',help='DNA sequence string')
	return parser.parse_args()

def reverse_comp(sequence):
    DNA_dict = {'A':'T','T':'A','G':'C','C':'G'}
    comp_sequence = []
    for nucleotide in sequence:
        comp_sequence.append(DNA_dict[nucleotide])
    output = ''.join(reversed(comp_sequence))
    return output

if __name__ == "__main__":
    options = get_options()
    rev_com_sequence = reverse_comp(options.sequence)
    print("Reverse complemented sequence = {}".format(rev_com_sequence))