import sqlite3
import mysql.connector as msc

def sql3():
    data = sqlite3.connect("Journal.db")
    cur = data.cursor()
    return data,cur

def Mysql(Host,User,Pass,Database):
    try:    
        data = msc.connect(
            localhost=Host,
            user = User,
            password = Pass,
            database = Database
        )
        cur = data.cursor()
        return data,cur,True
    except:
        return False,False,False    