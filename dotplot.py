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
    table = []
    for base_a in seq_a:
        row = []
        for base_b in seq_b:
            if base_a == base_b:
                row.append(base_a)
            else:
                row.append(' ')
        table.append(row)
    return table

def match_filter(table):
    """ TODO: write docstring """
    for row_index, row in enumerate(table):
        for cell_index, cell in enumerate(row):
            if (row_index == 0) and (cell_index + 1 == len(row)):
                row[cell_index] = cell.lower()
            elif (row_index + 1 == len(table)) and (cell_index == 0):
                row[cell_index] = cell.lower()
            elif (row_index == 0) or (cell_index == 0):
                if table[row_index + 1][cell_index + 1] == ' ':
                    row[cell_index] = cell.lower()
            elif (row_index + 1 == len(table)) or (cell_index + 1 == len(row)):
                if table[row_index - 1][cell_index - 1] == ' ':
                    row[cell_index] = cell.lower()
            elif (table[row_index + 1][cell_index + 1] == ' ') and (table[row_index - 1][cell_index - 1] == ' '):
                row[cell_index] = cell.lower()
    return table

def ascii_switcher(table):
    """TODO: write docstring """
    filtered_table = match_filter(table)
    for row in filtered_table:
        for cell_index, cell in enumerate(row):
            if cell.strip().isupper():
                row[cell_index] = '\\'
            elif cell.strip().islower():
                row[cell_index] = '.'
    return filtered_table
