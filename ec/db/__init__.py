
import secrets
import mt.db

id_byte_len = 4

s_id_exists = 'SELECT COUNT(*) > 0 FROM {0} WHERE Id = %s'

def create_id(tablename):
    ret_val = None
    s = s_id_exists.format(tablename)

    while True:
        ret_val = secrets.token_hex(id_byte_len)
        if not mt.db.read_all(s, [ ret_val ])[0][0]:
            break
    return ret_val
