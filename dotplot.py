#!/usr/bin/env python
"""
TODO: write docstring
"""
import argparse
import sys
from copy import deepcopy

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
    if check_fasta_lines(lines):
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

def ascii_filter(table, slash):
    """ TODO: write docstring """
    for row in table:
        for cell_index, cell in enumerate(row):
            if cell.strip().isupper():
                row[cell_index] = slash
            elif cell.strip().islower():
                row[cell_index] = '.'
    return table

def find_palindromes(table):
    """ TODO: write docstring """
    for row_index, row in enumerate(table):
        for cell_index, cell in enumerate(row):
            if (row_index == 0) and (cell_index == 0):
                row[cell_index] = cell.lower()
            elif (row_index + 1 == len(table)) and (cell_index + 1 == len(row)):
                row[cell_index] = cell.lower()
            elif (row_index == 0) or (cell_index + 1 == len(row)):
                if table[row_index + 1][cell_index - 1] == ' ':
                    row[cell_index] = cell.lower()
            elif (row_index + 1 == len(table)) or (cell_index == 0):
                if table[row_index - 1][cell_index + 1] == ' ':
                    row[cell_index] = cell.lower()
            elif (table[row_index + 1][cell_index - 1] == ' ') and (table[row_index - 1][cell_index + 1] == ' '):
                row[cell_index] = cell.lower()
    return table

def create_complement_table(seq_a, seq_b):
    """ TODO: write docstring """
    table = []
    for base_a in seq_a:
        row = []
        for base_b in seq_b:
            if (base_a, base_b) in (('G', 'C'), ('C', 'G'), ('A', 'T'), ('T', 'A'), ('A', 'U'), ('U', 'A')):
                row.append('X')
            else:
                row.append(' ')
        table.append(row)
    return table

def merge_tables(table_1, table_2):
    """ TODO: write docstring """
    merged_table = []
    for row_1, row_2 in zip(table_1, table_2):
        merged_row = []
        for cell_1, cell_2 in zip(row_1, row_2):
            if cell_1 == cell_2:
                merged_row.append(cell_1)
            elif cell_1 == '.':
                    merged_row.append(cell_2)
            else:
                merged_row.append(cell_1.upper())
        merged_table.append(merged_row)
    return merged_table

def parse_command_line_args():
    """ TODO: write docstring """
    parser = argparse.ArgumentParser()
    parser.add_argument('file_a', type=argparse.FileType('r'))
    parser.add_argument('file_b', type=argparse.FileType('r'))
    parser.add_argument('-c', '--complement', action='store_true')
    parser.add_argument('-f', '--filter', action='store_true')
    parser.add_argument('-a', '--ascii', action='store_true')
    parser.add_argument('-p', '--palindrome', action='store_true')
    return parser.parse_args()

def print_dotplot(seq_a, seq_b, table):
    """ TODO: write docstring """
    print('  ' + seq_b)
    print(' +' + len(seq_b) * '-')
    for base_a, row in zip(seq_a, table):
        print(base_a + '|' + ''.join(row))

def main():
    """ TODO: write docstring """
    args = parse_command_line_args()
    seq_a = get_sequence_from_fasta_lines(get_lines_from_file(args.file_a))
    seq_b = get_sequence_from_fasta_lines(get_lines_from_file(args.file_b))
    if not (seq_a and seq_b):
        sys.exit('Invalid FASTA file')
    if args.complement:
        table = create_complement_table(seq_a, seq_b)
    else:
        table = create_matches_table(seq_a, seq_b)
    if args.filter and args.palindrome:
        filtered_table = filter_matches(deepcopy(table))
        palindrome_table = find_palindromes(deepcopy(table))
        if args.ascii:
            ascii_filter(filtered_table, '\\')
            ascii_filter(palindrome_table, '/')
        table = merge_tables(filtered_table, palindrome_table)
    elif args.filter:
        filter_matches(table)
        if args.ascii:
            ascii_filter(table, '\\')
    elif args.palindrome:
        find_palindromes(table)
        if args.ascii:
            ascii_filter(table, '/')
    elif args.ascii:
        parser.error('--ascii requires --filter or --palindrome')
    print_dotplot(seq_a, seq_b, table)

if __name__ == '__main__':
    main()
