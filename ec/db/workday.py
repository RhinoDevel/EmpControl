
import secrets
import mt.db
import ec.db
import ec.db.worker

tablename = 'workday'
s_read_all = 'SELECT Nr, Id, Worker_nr, Begin_at, End_at, Break, Vacation, Sick FROM ' + tablename + ' ORDER BY Begin_at'
s_create = 'INSERT INTO ' + tablename + ' (Id, Worker_nr, Begin_at, End_at, Break, Vacation, Sick)' + ' VALUES (%s, %s, %s, %s, %s, %s , %s) RETURNING Nr'
s_read_by_id = 'SELECT Nr, Id, Worker_nr, Begin_at, End_at, Break, Vacation, Sick FROM ' + tablename + ' WHERE Id = %s'
s_update_by_id = 'UPDATE ' + tablename + ' SET Worker_nr = %s, Begin_at = %s, End_at = %s, Break = %s, Vacation = %s, Sick = %s' + ' WHERE Id = %s'
s_delete_by_id = 'DELETE FROM ' + tablename + ' WHERE Id = %s'

def _create_id():
    return ec.db.create_id(tablename)

def _get_data(row):
    """Return data.

    Return value does not contain worker nr., but ID.
    """

    worker_id = ec.db.worker.read_id(row[2])

    return {
        'nr': row[0],
        'id': row[1],
        'worker_id': worker_id,
        'begin_at': row[3],
        'end_at': row[4],
        'break': row[5],
        'vacation': row[6],
        'sick': row[7]
    }

def _is_valid_input(data):
    """Check stuff the DB does not."""

    # Workday
    #
    # - Begin_at not NULL
    # - End_at not NULL and later than begin_at
    # - End_at-Begin_at greater than Break+1 (at least one minute before and after break)
    # - Vacation False
    # - Sick False

    # Vacation day
    #
    # - Begin_at time is 00:00
    # - End_at is NULL
    # - Break is 0
    # - Vacation True
    # - Sick False

    # Sick day
    #
    # Like vacation day, but with vacation and sick values swapped.

    # Workday with some vacation time
    #
    # Like workday, but with vacation True.

    # Workday with some sick time
    #
    # Like workday, but with sick True.

    # Sick vacation day
    #
    # Like vacation day, but also with sick True.

    return True # TODO: Implement!

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
    """Create new workday entry in DB, returns DB nr.

    No worker nr. in given data, but worker ID.
    """

    if not _is_valid_input(data):
        raise ValueError('Invalid data given!')

    worker_nr = ec.db.worker.read_nr(data['worker_id'])

    return mt.db.write_return(
        s_create,
        [
            _create_id(),
            worker_nr,
            data['begin_at'],
            data['end_at'],
            data['break'],
            data['vacation'],
            data['sick']
        ])[0]

def update_by_id(data):
    """Update workday entry in DB.

    No worker nr. in given data, but worker ID.
    """

    if not _is_valid_input(data):
        raise ValueError('Invalid data given!')

    worker_nr = ec.db.worker.read_nr(data['worker_id'])

    mt.db.write(
        s_update_by_id,
        [
            worker_nr,
            data['begin_at'],
            data['end_at'],
            data['break'],
            data['vacation'],
            data['sick'],
            data['id'].strip()
        ])

def delete_by_id(i):
    mt.db.write(s_delete_by_id, [ i.strip() ])
