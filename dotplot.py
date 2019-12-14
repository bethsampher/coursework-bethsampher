#!/usr/bin/env python
"""
TODO: write docstring
"""
import argparse

def get_lines_from_file(file_):
    """ Returns list of lines read from given file (filename) """
    contents = file_.read()
    lines = contents.splitlines()
    return lines

def check_fasta_lines(lines):
    """ TODO: write docstring """
    if not lines:
        return False
    for line in lines:
        if len(line) == 0:
            return False
        if (line[0] != '>') and (line.islower()):
            return False
    if lines[0][0] != '>':
        return False
    return True

def get_sequence_from_fasta_lines(lines):
    """ Returns first sequence from list of file lines (lines), based on FASTA format """
    sequence = ''
    for line in lines[1:]:
        if line[0] == '>':
            break
        else:
            sequence += line
    return sequence

def create_matches_table(seq_a, seq_b):
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

def filter_matches(table):
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

def ascii_filter(table):
    """ TODO: write docstring """
    filtered_table = filter_matches(table)
    for row in filtered_table:
        for cell_index, cell in enumerate(row):
            if cell.strip().isupper():
                row[cell_index] = '\\'
            elif cell.strip().islower():
                row[cell_index] = '.'
    return filtered_table

def find_palindromes(table):
    """ TODO: write docstring """
    ascii_table = ascii_filter(table)
    for row_index, row in enumerate(ascii_table):
        for cell_index, cell in enumerate(row):
            if cell == '.':
                if (row_index == 0) and (cell_index == 0):
                    pass
                elif (row_index + 1 == len(ascii_table)) and (cell_index + 1 == len(row)):
                    pass
                elif (row_index == 0) or (cell_index + 1 == len(row)):
                    if ascii_table[row_index + 1][cell_index - 1] in ('.', '\\', '/'):
                        row[cell_index] = '/'
                elif (row_index + 1 == len(ascii_table)) or (cell_index == 0):
                    if ascii_table[row_index - 1][cell_index + 1] in ('.', '\\', '/'):
                        row[cell_index] = '/'
                elif (ascii_table[row_index + 1][cell_index - 1] in ('.', '\\', '/')) or (ascii_table[row_index - 1][cell_index + 1] in ('.', '\\', '/')):
                    row[cell_index] = '/'
    return ascii_table

def create_complements_table(seq_a, seq_b):
    """ TODO: write docstring """
    table = []
    for base_a in seq_a:
        row = []
        for base_b in seq_b:
            if (base_a, base_b) in (('G', 'C'), ('C', 'G'), ('A', 'T'), ('T', 'A'), ('A', 'U'), ('U', 'A')):
                row.append('C')
            else:
                row.append(' ')
        table.append(row)
    return find_palindromes(table)

def print_dotplot(seq_a, seq_b, table):
    """ TODO: write docstring """
    print('  ' + seq_b)
    print(' +' + len(seq_b) * '-')
    for base_a, row in zip(seq_a, table):
        print(base_a + '|' + ''.join(row))

def main():
    """ TODO: write docstring """
    parser = argparse.ArgumentParser()
    parser.add_argument('file_1', type=argparse.FileType('r'))
    parser.add_argument('file_2', type=argparse.FileType('r'))
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-f', '--filter', action='store_true')
    group.add_argument('-a', '--ascii', action='store_true')
    group.add_argument('-p', '--palindrome', action='store_true')
    group.add_argument('-c', '--complements', action='store_true')
    args = parser.parse_args()
    seq_a = get_sequence_from_fasta_lines(get_lines_from_file(args.file_1))
    seq_b = get_sequence_from_fasta_lines(get_lines_from_file(args.file_2))
    table = create_matches_table(seq_a, seq_b)
    if args.complements:
        table = create_complements_table(seq_a, seq_b)
    elif args.filter:
        table = filter_matches(table)
    elif args.ascii:
        table = ascii_filter(table)
    elif args.palindrome:
        table = find_palindromes(table)
    print_dotplot(seq_a, seq_b, table)

if __name__ == '__main__':
    main()
