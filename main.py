
import db

def str_is_nonwhitespace(s):
    """Return, if given parameter is a string that is neither empty, nor whitespace-only."""

    return isinstance(s, str) and s and not s.isspace()

def test():
    #db.write("UPDATE Task SET Title='01a' WHERE Nr = 11;")
    print(db.read_all("SELECT * FROM Task;"))
    #close_conn()
#
test()
test()
db.close()

with open('dbinit.sql', 'r') as dbInitFile:
    dbInit=dbInitFile.read()

#db.write(dbInit)
