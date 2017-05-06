
import db

def str_is_nonwhitespace(s):
    """Is given argument a string that is neither empty, nor whitespace-only?
    """

    return isinstance(s, str) and s and not s.isspace()

def str_read_file(path):
    """Return content of file at given path as string.
    """

    with open(path, 'r') as f:
        return f.read()

def test():
    #db.write("UPDATE Task SET Title='01a' WHERE Nr = 11;")
    print(db.read_all("SELECT * FROM Task;"))
    #close_conn()
#
test()
test()
db.close()

dbInit = str_read_file('dbinit.sql')

print(dbInit)
