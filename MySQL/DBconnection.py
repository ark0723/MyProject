
#DBconnection.py

import MySQLdb

db_host = "localhost"
db_user = "root"
db_pw = "alth1031!"
db_name = "test"


connect_pool = []

def connectDB():
    connect = MySQLdb.connect(db_host,db_user,db_pw,db_name)
    return connect

def get_connect():
    global connect_pool
    if not connect_pool:
        connect_tmp = connectDB()
        connect_pool.append(connect_tmp)
    return connect_pool.pop()

def return_connect(conn):
    global connect_pool
    connect_pool.append(conn)
    return

def close_db(db):
    db.close()
    return
    

"""
def test_connection():
    db = get_connect()
    c = db.cursor()
    c.execute("select version()")
    data = c.fetchall()
    print (data)

test_connection()
    
"""
