"""
TODO: write docstring
"""

def read_lines(filename):
    with open(filename) as file:
        contents = file.read()
        lines = contents.splitlines()
    return lines
