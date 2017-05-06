
# sudo systemctl start postgresql

# pip install -U pip
# pip install psycopg2
#
import psycopg2

dbname = "mtdatabase"
user = "mtuser"
password = "resutm"
#
conn = None

def _get_conn():
    """Return connection to DB."""

    global conn, dbname, user, password

    if conn is None or conn.closed:
        conn = psycopg2.connect("dbname="+dbname+" user="+user+" password="+password)

    return conn

def close():
    """Close global connection to DB, if open."""

    global conn

    if conn is None:
        return

    if not conn.closed:
        conn.close()

    conn = None

def write(query):
    """Write to DB."""

    conn = _get_conn()
    cur = conn.cursor()

    cur.execute(query)
    conn.commit()
    cur.close()

def read_all(query):
    """Return all entries read."""

    retVal = None
    conn = _get_conn()
    cur = conn.cursor()

    cur.execute(query)
    retVal = cur.fetchall()
    cur.close()
    return retVal
