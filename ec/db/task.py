
import secrets
from datetime import datetime
import mt.db
import ec.db
import ec.db.workday
import ec.db.tasktype
import ec.db.client

tablename = 'task'
s_read_all = ('SELECT Nr, Id, Workday_nr, Type_nr, Client_nr'
             + ', Lastedit_at, Description FROM ' + tablename
             + ' ORDER BY Workday_nr, Description')
s_create = ('INSERT INTO ' + tablename
           + ' (Id, Workday_nr, Type_nr, Client_nr, Lastedit_at'
           + ', Description)'
           + ' VALUES (%s, %s, %s, %s, %s, %s) RETURNING Nr')
s_read_by_id = ('SELECT Nr, Id, Workday_nr, Type_nr, Client_nr'
               +', Lastedit_at, Description FROM ' + tablename
               + ' WHERE Id = %s')
s_update_by_id = ('UPDATE ' + tablename
                 + ' SET Workday_nr = %s, Type_nr = %s'
                 + ', Client_nr = %s, Lastedit_at = %s'
                 + ', Description = %s' + ' WHERE Id = %s')
s_delete_by_id = 'DELETE FROM ' + tablename + ' WHERE Id = %s'

def _create_id():
    return ec.db.create_id(tablename)

def _get_data(row):
    """Return data.

    Return value does not contain workday nr., but ID.
    Return value does not contain (task-)type nr., but ID.
    Return value does not contain client nr., but ID.
    """

    workday_id = ec.db.workday.read_id(row[2])
    type_id = ec.db.tasktype.read_id(row[3])
    client_id = ec.db.client.read_id(row[4])

    return {
        'nr': row[0],
        'id': row[1],
        'workday_id': workday_id,
        'type_id': type_id,
        'client_id': client_id,
        'lastedit_at': row[5],
        'description': row[6]
    }

def _is_valid_input(data):
    """Check stuff the DB does not."""

    # Is workday entry really a WORK day?

    return True # TODO: Implement and use!

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
    """Create new task entry in DB, returns DB nr.

    No workday nr. in given data, but workday ID.
    No (task-)type nr. in given data, but (task-)type ID.
    No client nr. in given data, but client ID.
    """

    if not _is_valid_input(data):
        raise ValueError('Invalid data given!')

    workday_nr = ec.db.workday.read_nr(data['workday_id'])
    type_nr = ec.db.tasktype.read_nr(data['type_id'])
    client_nr = ec.db.client.read_nr(data['client_id'])

    return mt.db.write_return(
        s_create,
        [
            _create_id(),
            workday_nr,
            type_nr,
            client_nr,
            datetime.now(),
            data['description'].strip()
        ])[0]

def update_by_id(data):
    """Update task entry in DB.

    No workday nr. in given data, but workday ID.
    No (task-)type nr. in given data, but (task-)type ID.
    No client nr. in given data, but client ID.
    """

    if not _is_valid_input(data):
        raise ValueError('Invalid data given!')

    workday_nr = ec.db.workday.read_nr(data['workday_id'])
    type_nr = ec.db.tasktype.read_nr(data['type_id'])
    client_nr = ec.db.client.read_nr(data['client_id'])

    mt.db.write(
        s_update_by_id,
        [
            workday_nr,
            type_nr,
            client_nr,
            datetime.now(),
            data['description'].strip(),
            data['id'].strip()
        ])

def delete_by_id(i):
    mt.db.write(s_delete_by_id, [ i.strip() ])
