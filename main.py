
import mt.db
import mt.str

def test():
    #mt.db.write("UPDATE Task SET Title='01a' WHERE Nr = 11;")
    print(mt.db.read_all("SELECT * FROM Task;"))
    #close_conn()
#
test()
test()
mt.db.close()

dbInit = mt.str.read_file('dbinit.sql')

print(dbInit)
