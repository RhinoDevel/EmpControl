
# Windows:
#
# python -m pip install --upgrade pip
# python -m pip install psycopg2

# Linux (Manjaro):
#
# sudo systemctl start postgresql
#
# pip install -U pip
# pip install psycopg2

import psycopg2
import logging

dbname = 'mtdatabase'
user = 'mtuser'
password = 'resutm'
#
conn = None

def _get_conn():
    """Return connection to DB."""

    global conn, dbname, user, password

    if conn is None or conn.closed:
        conn = psycopg2.connect(
            'dbname=' + dbname
            + ' user=' + user
            + ' password=' + password)

    return conn

def close():
    """Close global connection to DB, if open."""

    global conn

    if conn is None:
        return

    if not conn.closed:
        conn.close()

    conn = None

def write_return(query, params=None):
    """Write to DB, return result."""

    ret_val = None

    conn = _get_conn()
    cur = conn.cursor()

    cur.execute(query, params)

    ret_val = cur.fetchone()

    conn.commit()
    cur.close()
    return ret_val

def write(query, params=None):
    """Write to DB."""

    conn = _get_conn()
    cur = conn.cursor()

    cur.execute(query, params)
    conn.commit()
    cur.close()

def read_all(query, params=None):
    """Return all entries read."""

    logging.debug('mt.db.read_all: Query = "' + query + '".')

    retVal = None
    conn = _get_conn()
    cur = conn.cursor()

    cur.execute(query, params)
    retVal = cur.fetchall()
    cur.close()
    return retVal
