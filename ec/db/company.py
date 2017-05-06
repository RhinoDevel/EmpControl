
import mt.db

tablename = "company"
s_read_all = "SELECT Nr, Title FROM "+tablename
s_create = "INSERT INTO "+tablename+" (Title) VALUES (%s) RETURNING Nr"
s_update = "UPDATE "+tablename+" SET Title = %s WHERE Nr = %s"

def _get_data(row):
    return {
        'nr': row[0],
        'title': row[1]
    }

def read_all():
    return list(map(_get_data, mt.db.read_all(s_read_all)))

def read(nr):
    return _get_data(mt.db.read_all(
        s_read_all+" WHERE Nr = %s", [ str(nr) ])[0])

def create(data_without_nr):
    return mt.db.write_return(s_create, [ data_without_nr['title'] ])[0]

def update(data):
    mt.db.write(s_update, [ data['title'], data['nr'] ])
