
import secrets
import mt.db
import ec.db
import ec.db.company

tablename = 'client'
s_read_all = ('SELECT Nr, Id, Company_nr, Lastname, Firstname FROM '
             + tablename + ' ORDER BY Lastname, Firstname')
s_create = ('INSERT INTO ' + tablename
           + ' (Id, Company_nr, Lastname, Firstname)'
           + ' VALUES (%s, %s, %s, %s) RETURNING Nr')
s_read_by_id = ('SELECT Nr, Id, Company_nr, Lastname, Firstname FROM '
               + tablename + ' WHERE Id = %s')
s_update_by_id = ('UPDATE ' + tablename +
                 ' SET Company_nr = %s, Lastname = %s, Firstname = %s'
                 + ' WHERE Id = %s')
s_delete_by_id = 'DELETE FROM ' + tablename + ' WHERE Id = %s'

def _create_id():
    return ec.db.create_id(tablename)

def _get_data(row):
    """Return data.

    Return value does not contain company nr., but ID.
    """

    company_id = ec.db.company.read_id(row[2])

    return {
        'nr': row[0],
        'id': row[1],
        'company_id': company_id,
        'lastname': row[3],
        'firstname': row[4]
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

def create(data):
    """Create new client entry in DB, returns DB nr.

    No company nr. in given data, but company ID.
    """

    company_nr = ec.db.company.read_nr(data['company_id'])

    return mt.db.write_return(
        s_create,
        [
            _create_id(),
            company_nr,
            data['lastname'].strip(),
            data['firstname'].strip()
        ])[0]

def update_by_id(data):
    """Update client entry in DB.

    No company nr. in given data, but company ID.
    """

    company_nr = ec.db.company.read_nr(data['company_id'])

    mt.db.write(
        s_update_by_id,
        [
            company_nr,
            data['lastname'].strip(),
            data['firstname'].strip(),
            data['id'].strip()
        ])

def delete_by_id(i):
    mt.db.write(s_delete_by_id, [ i.strip() ])
