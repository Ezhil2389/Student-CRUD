from flask import Flask, redirect, request, render_template
from flask_restful import Api
import pymysql


db = pymysql.connect(host="localhost", user="ezhilr", password="pass", database="stable")

app = Flask(__name__)
api = Api(app)



cursor = db.cursor()
cursor.execute('INSERT INTO stud (name, rollno, CLASS, SECTION, CLASS_TEACH, GPA, FEE) VALUES ("MARY","cb.en.u4cce21064","ECE","C","Suresh",2,"NOTPAID"),("ALEX","cb.en.u4cce21065","IT","D","Shankar",1,"PAID")')

def print_table():
    row=cursor.fetchall()
    for row in row:
        print(row)


@app.route('/')
def someName():
    
    sql = "SELECT * FROM stud"
    cursor.execute(sql)
    profile = cursor.fetchall()
    return render_template("student.html", results=profile)



@app.route('/add', methods=['GET', 'POST'])
def add_student():
   
    return render_template("add.html")

@app.route('/add', methods=["POST"])
def profile():
        name = request.form.get("name")
        rollno = request.form.get("rollno")
        clas = request.form.get("class")
        section = request.form.get("section")
        class_teacher = request.form.get("class_teacher")
        GPA = request.form.get("GPA")
        Fee_status= request.form.get("Fee_status")
   

	
        if  name != '' and rollno != '' and clas != '' and section != '' and class_teacher != '' and GPA != '' and Fee_status != '':
            sql="INSERT INTO stud (name, rollno, CLASS, SECTION, CLASS_TEACH, GPA, FEE) VALUES (name, rollno, clas,section,class_teacher,GPA,Fee_status"
            cursor.execute(sql)
            sql = "SELECT * FROM stud"
            cursor.execute(sql)
            results = cursor.fetchall()
            return render_template("student.html", results=results)
        else:
            print_table()

        

        
        


@app.route('/update', methods=['POST'])
def update_student():
    id = request.form['id']
    name = request.form['name']
    rollno = request.form['rollno']
    class_name = request.form['class_name']
    section = request.form['section']
    teacher = request.form['teacher']
    gpa = request.form['gpa']
    fee = request.form['fee']
    sql = "UPDATE stud SET name=%s, rollno=%s, class_name=%s, section=%s, teacher=%s, gpa=%s, fee=%s WHERE id=%s"
    cursor = db.cursor()
    cursor.execute(sql, (name, rollno, class_name, section, teacher, gpa, fee, id))
    db.commit()
    return 'Student updated successfully!'

@app.route('/delete', methods=['POST'])
def delete_student():
    id = request.form['id']
    sql = "DELETE FROM stud WHERE id=%s"
    cursor = db.cursor()
    cursor.execute(sql, (id,))
    db.commit()
    return 'Student deleted successfully!'

@app.route('/search', methods=['POST'])
def search_student():
    name = request.form['name']
    sql = "SELECT * FROM stud WHERE name LIKE '%%{}%%'".format(name)
    cursor = db.cursor()
    cursor.execute(sql)
    results = cursor.fetchall()
    return render_template("student.html", results=results)

@app.route('/sort', methods=['POST'])
def sort_student():
    sort_by = request.form['sort_by']
    sql = "SELECT * FROM stud ORDER BY {}".format(sort_by)
    cursor = db.cursor()
    cursor.execute(sql)
    results = cursor.fetchall()
    return render_template("student.html", results=results)

if __name__ == '__main__':
 app.run(debug=True)