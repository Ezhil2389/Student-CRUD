from flask import Flask, render_template, request, jsonify
import pymysql
from flask_cors import CORS

studentdb = Flask(__name__)
CORS(studentdb)

def connection():
    s = 'localhost' 
    d = 'stable' 
    u = 'ezhilr' # Your login user
    p = 'pass' # Your login password
    conn = pymysql.connect(host=s, user=u, password=p, database=d)
    return conn

conn = connection()
cursor = conn.cursor()

@studentdb.route("/")
def main():
    cursor.execute("SELECT * FROM stud")
    stu = []
    for row in cursor:
        stu.append({"name": row[0], "Rollno": row[1], "class": row[2], "section": row[3], "classteacher": row[4], "GPA": row[5], "Fee_status": row[6]})
    return render_template("login.html", stu=stu)

@studentdb.route("/add-student", methods=["POST"])
def add_student():
    try:
        data = request.get_json()
        name = data.get("name")
        rollno = data.get("rollNumber")
        clas = data.get("selectedClass")
        section = data.get("selectedSection")
        class_teacher = data.get("classTeacher")
        GPA = data.get("gpa")
        Fee_status = data.get("feeStatus")

        cursor.execute('INSERT INTO stud (name, rollno, CLASS, SECTION, CLASS_TEACH, GPA, FEE) VALUES (%s, %s, %s, %s, %s, %s, %s)', (name, rollno, clas, section, class_teacher, GPA, Fee_status))
        conn.commit()

        return jsonify({"message": "Student added successfully!"}), 200
    except Exception as e:
        conn.rollback()
        return jsonify({"message": "Error occurred while adding student.", "error": str(e)}), 500

@studentdb.route("/update-student", methods=["POST"])
def update_student():
    try:
        data = request.get_json()
        rollno = data.get("rollNumberUpdated")
        criteria = data.get("updateBy")
        value = data.get("gpaUpdated" if criteria == "GPA" else "feeStatusUpdated")

        if criteria == "GPA":
            cursor.execute("UPDATE stud SET GPA=%s WHERE rollno=%s", (value, rollno))
        elif criteria == "Fee Status":
            cursor.execute("UPDATE stud SET FEE=%s WHERE rollno=%s", (value, rollno))
        conn.commit()

        return jsonify({"message": "Student updated successfully!"}), 200
    except Exception as e:
        conn.rollback()
        return jsonify({"message": "Error occurred while updating student.", "error": str(e)}), 500

@studentdb.route("/delete-student/<string:roll_number>", methods=["DELETE"])
def delete_student(roll_number):
    try:
        cursor.execute("DELETE FROM stud WHERE rollno=%s", (roll_number,))
        conn.commit()

        return jsonify({"message": "Student deleted successfully!"}), 200
    except Exception as e:
        conn.rollback()
        return jsonify({"message": "Error occurred while deleting student.", "error": str(e)}), 500

@studentdb.route("/view-students")
def view_students():
    try:
        cursor.execute("SELECT * FROM stud")
        stu = []
        for row in cursor:
            stu.append({
                "name": row[0],
                "rollNumber": row[1],
                "selectedClass": row[2],
                "selectedSection": row[3],
                "classTeacher": row[4],
                "gpa": row[5],
                "feeStatus": row[6]
            })
        return jsonify(stu), 200
    except Exception as e:
        return jsonify({"message": "Error occurred while fetching students.", "error": str(e)}), 500

if __name__ == "__main__":
    studentdb.run()
