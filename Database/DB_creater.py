from Journal_py_.Database.Connection import data,cursor
def database_check():
    cursor.execute("""SHOW DATABASES;""")
    for i in cursor.fetchall():
        if i in 'JournalPYbyachi' or i == 'JournalPYbyachi':
            return True
    


    return False
if not database_check():
    cursor.execute("CREATE DATABASE JournalPYbyachi;")

cursor.execute("USE DATABASE JournalPYbyachi;")

Table_name = "Journal_Data"

Tableno = 0

def check_table(Tname):
    cur = data.cursor()
    cur.execute("SHOW TABLES")
    Tableno =len(cur.fetchall)
    for i in cur.fetchall():
        if Tname in i:
            cur.close()
            return True
    cur.close()
    return False

