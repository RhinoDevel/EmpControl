
import secrets
import mt.db

id_byte_len = 4

s_id_exists = 'SELECT COUNT(*) > 0 FROM {0} WHERE Id = %s'
s_read_nr = 'SELECT Nr FROM {0} WHERE Id = %s'
s_read_id = 'SELECT Id FROM {0} WHERE Nr = %s'

def create_id(tablename):
    ret_val = None
    s = s_id_exists.format(tablename)

    while True:
        ret_val = secrets.token_hex(id_byte_len)
        if not mt.db.read_all(s, [ ret_val ])[0][0]:
            break
    return ret_val

def read_nr(i, tablename):
    """Return DB nr. of entry with ID given."""

    s = s_read_nr.format(tablename)
    return mt.db.read_all(s, [ i ])[0][0]

def read_id(nr, tablename):
    """Return ID of entry with DB nr. given."""

    s = s_read_id.format(tablename)
    return mt.db.read_all(s, [ nr ])[0][0]
