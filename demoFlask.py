from flask import Flask, request,json,jsonify
app = Flask(__name__)
import mysql.connector
con = mysql.connector.connect(host="localhost", user="root", password="PASSWORD", database="CRUD")

@app.route('/user',methods = ["POST"])
def create():
    user_name = request.json['name']
    user_email = request.json['email']
    user_phone = request.json['phone']
    cur = con.cursor()
    sql = "insert into students(name,email,phone) values(%s,%s,%s)"
    cur.execute(sql, (user_name, user_email, user_phone))
    cur.execute("select last_insert_id()")
    studentID = cur.fetchone()[0]
    con.commit()
    print("Student data inserted")
    return jsonify(
        {
            'message':"User created",
            'user_ID' :{'id' : studentID
            }
        }
    ),201

if __name__ == "__main__":
    app.run(debug=True)