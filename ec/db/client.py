
import secrets
import mt.db
import ec.db

tablename = 'client'
s_read_all = 'SELECT Nr, Id, Company_nr, Lastname, Firstname FROM '
             + tablename + ' ORDER BY Lastname, Firstname'
s_create = 'INSERT INTO ' + tablename
           + ' (Id, Company_nr, Lastname, Firstname)'
           + ' VALUES (%s, %s, %s, %s) RETURNING Nr'
s_read_by_id = 'SELECT Nr, Id, Company_nr, Lastname, Firstname FROM '
               + tablename + ' WHERE Id = %s'
s_update_by_id = 'UPDATE ' + tablename
                 + ' SET Company_nr = %s, Lastname = %s, Firstname = %s'
                 + ' WHERE Id = %s'
s_delete_by_id = 'DELETE FROM ' + tablename + ' WHERE Id = %s'

def _create_id():
    return ec.db.create_id(tablename)

def _get_data(row):
    return {
        'nr': row[0],
        'id': row[1],
        'company_nr': row[2], # TODO!
        'lastname': row[3],
        'firstname': row[4]
    }

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
            data_without_nr_or_id['company_nr'], # TODO!
            data_without_nr_or_id['lastname'].strip(),
            data_without_nr_or_id['firstname'].strip()
        ])[0]

def update_by_id(data):
    mt.db.write(
        s_update_by_id,
        [
            data['company_nr'], # TODO!
            data['lastname'].strip(),
            data['firstname'].strip(),
            data['id'].strip()
        ])

def delete_by_id(i):
    mt.db.write(s_delete_by_id, [ i.strip() ])
