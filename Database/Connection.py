import mysql.connector as msc
from Journal_py_.config import passwordn,usern,hostn

dynamic_db = "sys"

try:
    data = msc.connect(host = hostn,
                   user = usern,
                   password = passwordn,
                   database = dynamic_db )
except:
    print("worng id or pass")


cursor = data.cursor()