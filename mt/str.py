
def is_str(s):
    return isinstance(s, str)

def is_nonwhitespace(s):
    """Is given argument a string that is neither empty, nor whitespace-only?"""

    return is_str(s) and s and not s.isspace()

def read_file(path):
    """Return content of file at given path as string."""

    with open(path, 'r') as f:
        return f.read()
