#!/usr/bin/env python
"""
TODO: write docstring
"""

def read_lines(filename):
    """ Returns list of lines read from given file (filename) """
    with open(filename) as file:
        contents = file.read()
        lines = contents.splitlines()
    return lines

def get_sequence(lines):
    """ Returns first sequence from list of file lines (lines), based on FASTA format """
    sequence = ''
    for line in lines[1:]:
        if line[0] == '>':
            break
        else:
            sequence += line
    return sequence

def get_matches(seq_a, seq_b):
    """ Returns a list of lists of matches
    TODO: improve docstring
    """
    rows = []
    for base_a in seq_a:
        row = []
        for base_b in seq_b:
            if base_a == base_b:
                row.append(base_a)
            else:
                row.append(' ')
        rows.append(row)
    return rows

def match_filter(match_table):
    """ TODO: write docstring """
    for row_index, row in enumerate(match_table):
        for base_index, base in enumerate(row):
            if (row_index == 0) and (base_index + 1 == len(row)):
                row[base_index] = base.lower()
            elif (row_index + 1 == len(match_table)) and (base_index == 0):
                row[base_index] = base.lower()
            elif (row_index == 0) or (base_index == 0):
                if match_table[row_index + 1][base_index + 1] == ' ':
                    row[base_index] = base.lower()
            elif (row_index + 1 == len(match_table)) or (base_index + 1 == len(row)):
                if match_table[row_index - 1][base_index - 1] == ' ':
                    row[base_index] = base.lower()
            elif (match_table[row_index + 1][base_index + 1] == ' ') and (match_table[row_index - 1][base_index - 1] == ' '):
                row[base_index] = base.lower()
    return match_table

