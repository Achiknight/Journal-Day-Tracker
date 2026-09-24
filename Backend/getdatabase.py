from DBFile.Connection import Mysql,sql3



data = None
cur = None

def sqllite3():
    global data,cur
    data,cur = sql3()
    
def mysqlconnectior(host,user,Pass,Database):
    global data,cur
    con = None
    data,cur,con = Mysql(host,user,Pass,Database)
    return con

db_choice = {"sql3":sqllite3,"mysql":mysqlconnectior}