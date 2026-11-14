from DBFile.Connection import cur,data


def fetch_tables(cur,data):
    cur.execute("show tables")
    k = cur.fetchall()
    return k

