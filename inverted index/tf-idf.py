import nltk
from nltk.tokenize import word_tokenize
import pymysql
import math
# MySQL Connection 연결
conn = pymysql.connect(host = '147.46.15.66',
        user = 'bde11',
        password = 'bde1234',
        db = 'bde11',
        charset = 'utf8',
        cursorclass=pymysql.cursors.DictCursor
        )

curs = conn.cursor()
# Drop table if it already exist using execute() method.
curs.execute("DROP TABLE IF EXISTS INVERTED")

sql = """CREATE TABLE INVERTED (
         TERM  VARCHAR(1000) NOT NULL,
         id  int(11)
         )"""

curs.execute(sql)

sql = "show tables"
curs.execute(sql)
result = curs.fetchall()
print(result)


words=['debut', 'two', 'language', 'also' ]
for word in words:
    sql="select id from bde11.wiki where text like '%{}%'".format(word)
    curs.execute(sql)
    rows=curs.fetchall()

    for row in rows:
        sql = "INSERT INTO INVERTED(TERM,id) VALUES (%s, %s)"
        try:
            # Execute the SQL command
            curs.execute(sql,(word, row["id"]))
            # Commit your changes in the database
            conn.commit()
        except:
            # Rollback in case there is any error
            conn.rollback()
#Query 1

def tf_idt(id, w):
    sql="select text from bde11.wiki where id=%s"
    curs.execute(sql,id)
    text=curs.fetchall()
    words=word_tokenize(text[0]['text'])
    count=len(words)
    count_word=0
    for word in words:
        if word==',' or word=='.':
            count-=1
        elif word==w:
            count_word+=1
    tf=math.log(1+(count_word/count))

    sql="select count(id) from INVERTED where TERM=%s"
    curs.execute(sql,w)
    num=curs.fetchall()[0]['count(id)']
    idt=1/num
    print(tf*idt)

tf_idt(41631770,'also')
tf_idt(6688599,'debut')
tf_idt(13794826,'language')
# disconnect from server
conn.close()


