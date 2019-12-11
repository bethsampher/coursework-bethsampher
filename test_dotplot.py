from dotplot import *
from unittest.mock import patch

def mocked_read_lines(contents):
    lines = contents.splitlines()
    return lines

with patch('dotplot.read_lines', side_effect=mocked_read_lines) as read_lines:

    def test_read_lines_with_no_lines():
        assert read_lines('') == []

    def test_read_lines_with_one_line():
        one_line_string = 'This is the first line'
        assert read_lines(one_line_string) == ['This is the first line']

    def test_read_lines_with_multiple_lines():
        multiline_string = 'This is the first line\nThis is the second line\nThis is the third line'
        assert read_lines(multiline_string) == ['This is the first line', 'This is the second line', 'This is the third line']

def test_get_sequence_single():
    lines = ['>ID', 'ATCG']
    assert get_sequence(lines) == 'ATCG'

def test_get_sequence_with_concatenation():
    lines = ['>ID', 'ATCG', 'ATCGATCG', 'A']
    assert get_sequence(lines) == 'ATCGATCGATCGA'

def test_get_matches():
    seq_a = 'GGTCATTCAGGA'
    seq_b = 'AGGATCAAAC'
    assert get_matches(seq_a, seq_b) == [
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

def test_match_filter():
    match_table = [
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
    assert match_filter(match_table) == [
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


