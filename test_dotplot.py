from unittest.mock import patch

from dotplot import get_lines_from_file, check_fasta_lines, get_sequence_from_fasta_lines, create_matches_table, filter_matches, ascii_filter, find_palindromes, create_complements_table

def mocked_get_lines_from_file(contents):
    lines = contents.splitlines()
    return lines

with patch('dotplot.get_lines_from_file', side_effect=mocked_get_lines_from_file) as get_lines_from_file:

    def test_get_lines_from_file_with_no_lines():
        assert get_lines_from_file('') == []

    def test_get_lines_from_file_with_one_line():
        one_line_string = 'This is the first line'
        assert get_lines_from_file(one_line_string) == ['This is the first line']

    def test_get_lines_from_file_with_multiple_lines():
        multiline_string = 'This is the first line\nThis is the second line\nThis is the third line'
        assert get_lines_from_file(multiline_string) == ['This is the first line', 'This is the second line', 'This is the third line']

def test_check_fasta_lines_correct():
    lines = ['>ID', 'ATCG']
    assert check_fasta_lines(lines) == True

def test_check_fasta_lines_empty():
    lines = []
    assert check_fasta_lines(lines) == False

def test_check_fasta_lines_lowercase():
    lines = ['>ID', 'atcg']
    assert check_fasta_lines(lines) == False

def test_check_fasta_lines_no_id():
    lines = ['ID', 'ATCG']
    assert check_fasta_lines(lines) == False

def test_check_fasta_lines_blank_line():
    lines = ['>ID', '']
    assert check_fasta_lines(lines) == False

def test_get_sequence_from_fasta_lines_single():
    lines = ['>ID', 'ATCG']
    assert get_sequence_from_fasta_lines(lines) == 'ATCG'

def test_get_sequence_from_fasta_lines_with_concatenation():
    lines = ['>ID', 'ATCG', 'ATCGATCG', 'A']
    assert get_sequence_from_fasta_lines(lines) == 'ATCGATCGATCGA'

def test_create_matches_table():
    seq_a = 'GGTCATTCAGGA'
    seq_b = 'AGGATCAAAC'
    assert create_matches_table(seq_a, seq_b) == [
            [' ', 'G', 'G', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', 'G', 'G', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', 'T', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', 'C', ' ', ' ', ' ', 'C'],
            ['A', ' ', ' ', 'A', ' ', ' ', 'A', 'A', 'A', ' '],
            [' ', ' ', ' ', ' ', 'T', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', 'T', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', 'C', ' ', ' ', ' ', 'C'],
            ['A', ' ', ' ', 'A', ' ', ' ', 'A', 'A', 'A', ' '],
            [' ', 'G', 'G', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', 'G', 'G', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['A', ' ', ' ', 'A', ' ', ' ', 'A', 'A', 'A', ' ']
            ]

def test_filter_matches():
    table = [
            [' ', 'G', 'G', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', 'G', 'G', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', 'T', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', 'C', ' ', ' ', ' ', 'C'],
            ['A', ' ', ' ', 'A', ' ', ' ', 'A', 'A', 'A', ' '],
            [' ', ' ', ' ', ' ', 'T', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', 'T', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', 'C', ' ', ' ', ' ', 'C'],
            ['A', ' ', ' ', 'A', ' ', ' ', 'A', 'A', 'A', ' '],
            [' ', 'G', 'G', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', 'G', 'G', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['A', ' ', ' ', 'A', ' ', ' ', 'A', 'A', 'A', ' ']
            ]
    assert filter_matches(table) == [
            [' ', 'G', 'g', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', 'g', 'G', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', 'T', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', 'C', ' ', ' ', ' ', 'c'],
            ['a', ' ', ' ', 'A', ' ', ' ', 'A', 'a', 'a', ' '],
            [' ', ' ', ' ', ' ', 'T', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', 'T', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', 'C', ' ', ' ', ' ', 'c'],
            ['A', ' ', ' ', 'a', ' ', ' ', 'A', 'a', 'a', ' '],
            [' ', 'G', 'g', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', 'g', 'G', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['a', ' ', ' ', 'A', ' ', ' ', 'a', 'a', 'a', ' ']
            ]

def test_ascii_filter():
    table = [
            [' ', 'G', 'G', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', 'G', 'G', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', 'T', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', 'C', ' ', ' ', ' ', 'C'],
            ['A', ' ', ' ', 'A', ' ', ' ', 'A', 'A', 'A', ' '],
            [' ', ' ', ' ', ' ', 'T', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', 'T', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', 'C', ' ', ' ', ' ', 'C'],
            ['A', ' ', ' ', 'A', ' ', ' ', 'A', 'A', 'A', ' '],
            [' ', 'G', 'G', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', 'G', 'G', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['A', ' ', ' ', 'A', ' ', ' ', 'A', 'A', 'A', ' ']
            ]
    assert ascii_filter(table) == [
            [' ', '\\', '.', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', '.', '\\', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', '\\', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', '\\', ' ', ' ', ' ', '.'],
            ['.', ' ', ' ', '\\', ' ', ' ', '\\', '.', '.', ' '],
            [' ', ' ', ' ', ' ', '\\', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', '\\', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', '\\', ' ', ' ', ' ', '.'],
            ['\\', ' ', ' ', '.', ' ', ' ', '\\', '.', '.', ' '],
            [' ', '\\', '.', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', '.', '\\', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['.', ' ', ' ', '\\', ' ', ' ', '.', '.', '.', ' ']
            ]

def test_find_palindromes():
    table = [
            [' ', 'G', 'G', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', 'G', 'G', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', 'T', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', 'C', ' ', ' ', ' ', 'C'],
            ['A', ' ', ' ', 'A', ' ', ' ', 'A', 'A', 'A', ' '],
            [' ', ' ', ' ', ' ', 'T', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', 'T', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', 'C', ' ', ' ', ' ', 'C'],
            ['A', ' ', ' ', 'A', ' ', ' ', 'A', 'A', 'A', ' '],
            [' ', 'G', 'G', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', 'G', 'G', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['A', ' ', ' ', 'A', ' ', ' ', 'A', 'A', 'A', ' ']
            ]
    assert find_palindromes(table) == [
            [' ', '\\', '/', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', '/', '\\', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', '\\', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', '\\', ' ', ' ', ' ', '/'],
            ['.', ' ', ' ', '\\', ' ', ' ', '\\', '.', '/', ' '],
            [' ', ' ', ' ', ' ', '\\', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', '\\', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', '\\', ' ', ' ', ' ', '/'],
            ['\\', ' ', ' ', '/', ' ', ' ', '\\', '.', '/', ' '],
            [' ', '\\', '/', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', '/', '\\', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['/', ' ', ' ', '\\', ' ', ' ', '.', '.', '.', ' ']
            ]

def test_create_complements_table():
    seq_a = 'GGTCATTCAGGA'
    seq_b = 'AGGAUCAAAC'
    assert create_complements_table(seq_a, seq_b) == [
            [' ', ' ', ' ', ' ', ' ', '.', ' ', ' ', ' ', '.'],
            [' ', ' ', ' ', ' ', ' ', '\\', ' ', ' ', ' ', '/'],
            ['\\', ' ', ' ', '/', ' ', ' ', '\\', '.', '/', ' '],
            [' ', '\\', '/', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', '/', ' ', ' ', ' ', ' ', ' '],
            ['.', ' ', ' ', '/', ' ', ' ', '\\', '\\', '/', ' '],
            ['\\', ' ', ' ', '/', ' ', ' ', '/', '\\', '\\', ' '],
            [' ', '\\', '/', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', '\\', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', '\\', ' ', ' ', ' ', '.'],
            [' ', ' ', ' ', ' ', ' ', '/', ' ', ' ', ' ', '.'],
            [' ', ' ', ' ', ' ', '/', ' ', ' ', ' ', ' ', ' '],
            ]
