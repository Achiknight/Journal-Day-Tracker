import mysql.connector as msc
from Journal_py_.config import password,user,host


try:
    data = msc.connect(host = 'localhost',
                   user = "root",
                   password = "Achintya2008",
                   database = "sys" )
except:
    print("worng id or pass")