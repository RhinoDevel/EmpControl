
def is_nonwhitespace(s):
    """Is given argument a string that is neither empty, nor whitespace-only?"""

    return isinstance(s, str) and s and not s.isspace()

def read_file(path):
    """Return content of file at given path as string."""

    with open(path, 'r') as f:
        return f.read()
