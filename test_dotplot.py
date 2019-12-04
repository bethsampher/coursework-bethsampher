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

def test_get_sequence_short():
    lines = ['>ID', 'ATCG']
    assert get_sequence(lines) == 'ATCG'

def test_get_sequence_long():
    lines = ['>ID', 'ATCG', 'ATCGATCG', 'A']
    assert get_sequence(lines) == 'ATCGATCGATCGA'
