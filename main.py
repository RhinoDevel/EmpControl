
import db
import str

def test():
    #db.write("UPDATE Task SET Title='01a' WHERE Nr = 11;")
    print(db.read_all("SELECT * FROM Task;"))
    #close_conn()
#
test()
test()
db.close()

dbInit = str.read_file('dbinit.sql')

print(dbInit)
