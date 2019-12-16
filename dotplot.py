#!/usr/bin/env python
"""
A script to read 2 FASTA files from the command line  and print a dotplot

A sequence is retrieved from each file. The dotplot shows places where
the sequences match, or where they complement each other if specified.
There are other options to filter out lone matches/complements and to
display the output with dots and slashes.
"""
import argparse
import sys
from copy import deepcopy


def get_lines_from_file(file_):
    """Returns list of lines read from given file"""
    contents = file_.read()
    lines = contents.splitlines()
    return lines


def check_fasta_lines(lines):
    """Returns true if given file lines are in FASTA format, false if not"""
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
    """ Returns first sequence from given list of file lines

    Based on FASTA format
    """
    sequence = ''
    if check_fasta_lines(lines):
        for line in lines[1:]:
            if line[0] == '>':
                break
            sequence += line
    return sequence


def create_matches_table(seq_a, seq_b):
    """Returns a list of lists of places where the sequences match

    Each list is formed by comparing each item in seq_a with all the
    items in seq_b. Matches appear in the list and non-matches
    appear as whitespaces
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
    """Returns a filtered list of lists of matches

    Changes matches which do not form part of a
    forwards diagonal line to lowercase
    """
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
            elif (table[row_index + 1][cell_index + 1] == ' ') and (
                    table[row_index - 1][cell_index - 1] == ' '):
                row[cell_index] = cell.lower()
    return table


def ascii_filter(filtered_table, slash):
    """Returns a list of lists of matches filtered with symbols

    Changes uppercase letters in filtered matches list to a
    forward or back slash depending on what is specified and
    lowercase letters to the period character
    """
    for row in filtered_table:
        for cell_index, cell in enumerate(row):
            if cell.strip().isupper():
                row[cell_index] = slash
            elif cell.strip().islower():
                row[cell_index] = '.'
    return filtered_table


def find_palindromes(table):
    """Returns a list of lists of matches filtered to show palindromes

    Changes matches which do not form part of a backwards diagonal
    line to lowercase
    """
    for row_index, row in enumerate(table):
        for cell_index, cell in enumerate(row):
            if (row_index == 0) and (cell_index == 0):
                row[cell_index] = cell.lower()
            elif (row_index + 1 == len(table)) and (
                    cell_index + 1 == len(row)):
                row[cell_index] = cell.lower()
            elif (row_index == 0) or (cell_index + 1 == len(row)):
                if table[row_index + 1][cell_index - 1] == ' ':
                    row[cell_index] = cell.lower()
            elif (row_index + 1 == len(table)) or (cell_index == 0):
                if table[row_index - 1][cell_index + 1] == ' ':
                    row[cell_index] = cell.lower()
            elif (table[row_index + 1][cell_index - 1] == ' ') and (
                    table[row_index - 1][cell_index + 1] == ' '):
                row[cell_index] = cell.lower()
    return table


def create_complement_table(seq_a, seq_b):
    """Returns a list of lists of places where sequences complement each other

    Each list is formed by comparing each item in seq_a with all the items in
    seq_b. DNA/RNA complements appear in the list as 'X's and non-complements
    appear as whitespaces
    """
    table = []
    for base_a in seq_a:
        row = []
        for base_b in seq_b:
            if (base_a, base_b) in (('G', 'C'), ('C', 'G'), ('A', 'T')
                                    , ('T', 'A'), ('A', 'U'), ('U', 'A')):
                row.append('X')
            else:
                row.append(' ')
        table.append(row)
    return table


def merge_tables(table_1, table_2):
    """Returns a merged filtered and palindrome list of lists

    Allows both the forward and backward diagonal matches to
    be in the same table so the filter and palindrome options
    can be combined
    """
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
    """Parses options from the command line, returns args"""
    description = ('Prints dotplot based on matches in sequences from 2 '
                   'FASTA files. Abnormal exit if files not in correct format')
    parser = argparse.ArgumentParser(description=description)
    help_msg = 'first FASTA file'
    parser.add_argument('file_a', type=argparse.FileType('r'), help=help_msg)
    help_msg = 'second FASTA file'
    parser.add_argument('file_b', type=argparse.FileType('r'), help=help_msg)
    help_msg = 'instead of matches, finds DNA/RNA complements in sequences'
    parser.add_argument('-c', '--complement', action='store_true'
                        , help=help_msg)
    help_msg = 'converts fowards lone matches to lowercase'
    parser.add_argument('-f', '--filter', action='store_true', help=help_msg)
    help_msg = ('converts lone matches to dots and joined matches to slashes, '
                'must be used with --filter or --palindrome')
    parser.add_argument('-a', '--ascii', action='store_true', help=help_msg)
    help_msg = 'converts backwards lone matches to lowercase'
    parser.add_argument('-p', '--palindrome', action='store_true'
                        , help=help_msg)
    return parser


def print_dotplot(seq_a, seq_b, table):
    """Prints a dotplot

    Given the 2 sequences and the
    corresponding list of lists of
    matches
    """
    print('  ' + seq_b)
    print(' +' + len(seq_b) * '-')
    for base_a, row in zip(seq_a, table):
        print(base_a + '|' + ''.join(row))


def main():
    """Function invoked when this is run as a script"""
    parser = parse_command_line_args()
    args = parser.parse_args()
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
