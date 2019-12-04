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
    pass
