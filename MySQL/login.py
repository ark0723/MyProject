
#login.py

from userAcc import *
from DBconnection import *
from studentMenu import *
from instructorMenu import *


def login():

    print("Welcome")
    
    while(user_acc.conn is None):
        
        print("Please sign in")

        ID = input("%-10s:"%"ID")
        name = input("%-10s:"%"Name")

        auth(ID,name)
    
    switcher = {
        0 : student_menu,
        1 : instructor_menu
    }

    role_menu = switcher.get(user_acc.role)

    role_menu()



def auth(ID,name):

    #입력 받은 ID, name이 student DB에 존재하는지 확인
    user_connect = get_connect()
    c = user_connect.cursor()

    sql_1 = '''SELECT * FROM student WHERE (id ,name) IN  
                    (SELECT ID, name FROM student WHERE ID = %s and name=%s )'''
    c.execute(sql_1, (ID,name))
    result1 = c.fetchone()

    if result1:
        user_acc.set_attrs(ID, name, 0, user_connect)
    else : 
    #입력 받은 ID, name이 instructor DB에 존재하는지 확인
        sql_2 = '''SELECT * FROM instructor WHERE (id ,name) IN  
                        (SELECT ID, name FROM instructor WHERE ID = %s and name=%s )'''
        c.execute(sql_2, (ID,name))
        result2 = c.fetchone()
        if result2:
            user_acc.set_attrs(ID, name, 1, user_connect)
        else :
            print("Invalid call")
            c.close()
            return 

