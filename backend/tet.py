# Importing module
import pymysql

def connection():
    s = 'localhost' 
    d = 'studentdb' 
    u = 'root' #Your login user
    p = 'Sidarth@63' #Your login password
    conn = pymysql.connect(host=s, user=u, password=p, database=d)
    return conn


stu = []
conn = connection()
cursor = conn.cursor()
 

def print_table():
    cursor.execute("SELECT * FROM stud")
    for row in cursor:
        stu.append({"name": row[0], "Rollno": row[1], "class": row[2], "section": row[3], "classteacher": row[4], "GPA": row[5], "Fee_status": row[6]})
    print(stu)


def sort_by_name():
    cursor.execute('SELECT * from stud order by name')
    print_table()

def sort_by_rollno():
    cursor.execute('SELECT * from stud order by rollno')
    print_table()

def sort_by_gpa():
    cursor.execute('SELECT * from stud order by gpa')
    print_table()

def sort_by_section():
    cursor.execute('SELECT * from stud order by class,section')
    print_table()

def search_by_rollno(num):
    cursor.execute('select * from stud where rollno = num')
    rows = cursor.fetchall()
    print(rows)

def update_by_rollno(rollno):
    new_gpa=int(input())
    cursor.execute("update stud SET gpa=new_gpa where rollno=rollno")

def filter_above_gpa(v_gpa):
    cursor.execute("select * from stud where gpa>%s",v_gpa)
    print_table()

def filter_below_gpa(v_gpa):
    cursor.execute("select * from stud where gpa<=%s",v_gpa)
    print_table()

def filter_by_paid():
    cursor.execute("select * from stud where fee LIKE '%PAID%'")
    print_table()

def filter_by_not_paid():
    cursor.execute("select * from stud where fee LIKE '%NOTPAID%'")
    print_table()

def delete (name):
    cursor.execute('DELETE FROM stud WHERE name=%s;', (name,))
    conn.commit
    print_table()

delete("John")
filter_below_gpa("4")

