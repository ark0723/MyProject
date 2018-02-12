
#studentMenu.py

from userAcc import *
from DBconnection import *

def student_menu():
    
    menu_num = -1

    while(menu_num != '0'):
        print("\n\nWelcome %s"%user_acc.name)
        print("select student menu")
        print("1) Student Report")
        print("2) Check Course Qualification")
        print("3) View Time Table")
        print("0) Quit")
        menu_num = input("Enter : ")

        switcher = {
            '0' : quit_menu,
            '1' : print_stud_report,
            '2' : print_course_qual,
            '3' : print_time_table
        }

        selected_func = switcher.get(menu_num, print_wrong)

        selected_func()
    
    return


def print_stud_report():
    
    c = user_acc.conn.cursor()
    c.execute("SELECT * FROM student \
                WHERE ID = \"%s\" and name= \"%s\""%(user_acc.ID, user_acc.name))
    data = c.fetchone()
    
    print("You are a member of %s"%data[2])
    print("You have taken total %s credits\n"%data[3])
    print("Semester report\n")
		

    #평점 구하는 과정
    #수강한 학기, 연도 정보 모두 가져오기(distinct로 중복계산 방지)
    c.execute(''' select distinct year, semester from takes where ID=%s order by year desc'''%(user_acc.ID))
    data = c.fetchall()
    for year, semester in data :
        c.execute('''select credits,grade,title,dept_name ,course_id
                        from takes natural join course  
                        where ID=%s
                        and year = %s 
                        and semester= \"%s\" ''' %(user_acc.ID, year, semester))
        #year, semester 정보 cursor에서 받아오기
        data1 = c.fetchall()
        grades=list(zip(*data1))[1]
        credits =list(zip(*data1))[0]

        #수강한 과목들의 grade와 credit으로 평점을 계산
        #grade, credit 정보 cursor에서 받아오기
        #(zip쓰면 grade끼리, credit끼리 묶기 쉬움)
        grades_li=[]
        credits_li=list(map(lambda x : float(x),credits))
        for grade in grades :
            grades_li.append(gp_to_float(grade))
        gps=grades_li

#        gps=[a*b for a,b in zip(grades_li,credits_li)]
        print("\n%s\t%s\tGPA : %d"%(year, semester,sum(gps)/len(gps)))
        #과목들 정보 출력
        print("%10s\t%40s\t%15s\t%8s\t%8s"\
              %("course_id","title","dept_name","credit","grade"))

        #course_id, title, dept_name, credit, grade 정보를 cursor에서 받아온 후
        #위 표 모양대로 출력
        for credits,grade,title,dept_name ,course_id in data1 :
            print("%10s\t%40s\t%15s\t%8s\t%8s"\
              %(course_id,title,dept_name,credits,grade))




    #cursor 닫기
    c.close()

    return

  
def print_course_qual():

    c = user_acc.conn.cursor()
    
    while(True):
        print("\nCheck Course Qualification")
        course_info = input("Enter course ID or Title (Enter q to go back) : ")

        if(course_info == "q" or course_info == "Q"):
            break

        #입력 받은 게 course_id인지 title인지 확인해야 한다
        try : 
            c.execute("Select * from course where course_id = %s " %(course_info))
            data = c.fetchone()
            course_id =  course_info 
            course_title = data[1]
              
        except:        
         # course id가없다면
            c.execute("Select * from course where title = \"%s\"" %(course_info))
            data = c.fetchall()
            if not data :
                print("sorry, no data ")
                continue
            elif len(data) >=2 :
                print("There are several Course, Please, Choose cours id ")
                print("%10s\t %40s\t %15s\t %8s "\
              %('course_id','title','dept_name','credits'))
                
                for course_id,title,dept_name,credits in data :
                    print("%10s\t %40s\t %15s\t %8s "\
              %(course_id,title,dept_name,credits))  
                course_id = str(input("Enter course ID '000' "))
                course_title=course_info 
                
            else :
                course_id = data[0][0]
                course_title=course_info 

        #prereq_id 가져오기 
        c.execute("select prereq_id, title, dept_name, credits from prereq join course on (prereq_id = course.course_id ) where prereq.course_id=%s;" %(course_id ))
        prereq= c.fetchall()
        #선수과목 없을 경우
        if not prereq:
            print("no prereqisite course for the course.")
             

        #선수과목 있을 경우
        else :          
            c.execute("""select id, course_id from takes 
                        where id =%s and course_id in (select prereq_id from prereq where course_id=%s ) """ %(user_acc.ID,course_id))
            taken_pre = c.fetchall()
            if len(prereq)==len(taken_pre):
                print("you satisfy qualification to take the course.")
                print("there are prerequisite courses for the course.")    
            else:
                print("you have to take these courses to take the course.")
            print("%10s\t %40s\t %15s\t %8s "\
              %('prereq_id','title','dept_name','credits'))    
            for prereq_id, title, dept_name, credits in prereq:
                print("%10s\t %40s\t %15s\t %8s "\
              %(prereq_id,title,dept_name,credits))                



    #사용한 cursor 닫기
    c.close()        
    return

def print_time_table():
    c = user_acc.conn.cursor()

    #user가 수강한 year, semester 정보 받아오기
    c.execute(''' select distinct year, semester from takes where ID=%s order by year desc'''%(user_acc.ID))
    data = c.fetchall()

    print("\nTime Table\n")
    print("%10s\t%40s\t%15s\t%10s\t%10s"%("course_id","title","day","start_time","end_time"))

    #user가 수강한 year, semester중 가장 최근 year, semester를 이용하여
    #time table 만들기

    c.execute(''' select course_id,title , day ,start_hr,start_min,end_hr ,
                    end_min from  takes natural join course natural join section natural join time_slot
                    where ID=%s and  year=%s and semester=\"%s\" '''%(user_acc.ID,data[0][0],data[0][1]))
    timetable = c.fetchall()
    for course_id,title , day ,start_hr,start_min,end_hr,end_min  in timetable:
        start_time=str(start_hr)+':'+str(start_min)
        end_time=str(end_hr) +':'+str(end_min)
        print("%10s\t%40s\t%15s\t%10s\t%10s" %(course_id,title , day ,start_time,end_time ))        


    #사용한 cursor 닫기
    c.close()
    
    return

def quit_menu():
    
    global user_acc #global 변수 write할 때는 명시 필요

    #user가 사용하던 connection 반납
    return_connect(user_acc.conn)

    del user_acc

    return

def print_wrong():
    print("\nwrong menu number.")
    return

def gp_to_float(grade):
    return {
        "A+" : 4.3,
        "A " : 4,
        "A-" : 3.7,
        "B+" : 3.3,
        "B " : 3,
        "B-" : 2.7,
        "C+" : 2.3,
        "C " : 2,
        "C-" : 1.7,
        "D+" : 1.3,
        "D " : 1,
        "D-" : 0.7,
        "F" : 0
    }[grade]
