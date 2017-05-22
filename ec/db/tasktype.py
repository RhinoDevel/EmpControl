
import secrets
import mt.db
import ec.db

tablename = 'tasktype'
s_read_all = 'SELECT Nr, Id, Title FROM ' + tablename + ' ORDER BY Title'
s_create = 'INSERT INTO ' + tablename + ' (Id, Title) VALUES (%s, %s) RETURNING Nr'
s_read_by_id = 'SELECT Nr, Id, Title FROM ' + tablename + ' WHERE Id = %s'
s_update_by_id = 'UPDATE ' + tablename + ' SET Title = %s WHERE Id = %s'
s_delete_by_id = 'DELETE FROM ' + tablename + ' WHERE Id = %s'

def _create_id():
    return ec.db.create_id(tablename)

def _get_data(row):
    return {
        'nr': row[0],
        'id': row[1],
        'title': row[2]
    }

def read_nr(i):
    return ec.db.read_nr(i, tablename)

def read_id(nr):
    return ec.db.read_id(nr, tablename)

def read_all():
    return list(map(_get_data, mt.db.read_all(s_read_all)))

def read_by_id(i):
    return _get_data(mt.db.read_all(
        s_read_by_id, [ i.strip() ])[0])

def create(data_without_nr_or_id):
    return mt.db.write_return(
        s_create,
        [
            _create_id(),
            data_without_nr_or_id['title'].strip()
        ])[0]

def update_by_id(data):
    mt.db.write(
        s_update_by_id,
        [
            data['title'].strip(),
            data['id'].strip()
        ])

def delete_by_id(i):
    mt.db.write(s_delete_by_id, [ i.strip() ])
