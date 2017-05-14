
import secrets
import mt.db

id_byte_len = 4
tablename = 'company'
s_read_all = 'SELECT Nr, Id, Title FROM '+tablename+' ORDER BY Title'
s_create = 'INSERT INTO '+tablename+' (Id, Title) VALUES (%s, %s) RETURNING Nr'
s_update = 'UPDATE '+tablename+' SET Title = %s WHERE Nr = %s'
s_delete_by_id = 'DELETE FROM '+tablename+' WHERE Id = %s'
s_id_exists = 'SELECT COUNT(*) > 0 FROM '+tablename+' WHERE Id = %s'

def _create_id():
    ret_val = None

    while True:
        ret_val = secrets.token_hex(id_byte_len)
        if not mt.db.read_all(s_id_exists, [ ret_val ])[0][0]:
            break
    return ret_val

def _get_data(row):
    return {
        'nr': row[0],
        'id': row[1],
        'title': row[2]
    }

def read_all():
    return list(map(_get_data, mt.db.read_all(s_read_all)))

def read(nr):
    return _get_data(mt.db.read_all(
        s_read_all+' WHERE Nr = %s', [ str(nr) ])[0])

def create(data_without_nr_or_id):
    return mt.db.write_return(
        s_create,
        [
            _create_id(),
            data_without_nr_or_id['title'].strip()
        ])[0]

def update(data):
    mt.db.write(
        s_update,
        [
            data['title'].strip(),
            data['nr']
        ])

def delete_by_id(id):
    mt.db.write(s_delete_by_id, [ id ])
