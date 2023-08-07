import mysql.connector
from flask import Flask, request, json, jsonify
app = Flask(__name__)
con = mysql.connector.connect(
    host="localhost", user="root", password="PASSWORD", database="CRUD"
)
@app.route("/user", methods=["POST"])
def create():
    user_name = request.json["name"]
    user_email = request.json["email"]
    user_phone = request.json["phone"]
    cur = con.cursor()
    sql = "INSERT INTO students(name,email,phone) VALUE(%s,%s,%s)"
    cur.execute(sql, (user_name, user_email, user_phone))
    cur.execute("select last_insert_id()")
    studentID = cur.fetchone()[0]
    con.commit()
    print("Student data inserted")
    return jsonify({"message": "User created", "user_id": {"id": studentID}}), 201

@app.route("/user/<int:id>", methods=["GET"])
def view_details(id):
    cur = con.cursor()
    sql = "SELECT name, email, phone FROM students WHERE id = %s "
    cur.execute(sql, (id,))
    result = cur.fetchone()
    con.commit()
    if result:
        user_details = {"name": result[0],
                        "email": result[1],
                        "phone": result[2]}
        return jsonify(user_details)
    return "",404

@app.route('/user/<int:id>',methods = ["PUT","PATCH"])
def update_details(id):  
    if request.method == "PUT":
        user_name = request.json['name']
        user_email = request.json['email']
        user_phone = request.json['phone']
        cur = con.cursor()
        sql = "UPDATE students SET name = %s, email = %s, phone = %s WHERE id = %s"
        cur.execute(sql,(user_name,user_email,user_phone,id))
        con.commit()
        user_details = {"name": user_name,
                        "email": user_email,
                        "phone": user_phone}
        return 204
    return "", 404

@app.route('/user/<int:id>',methods = ["DELETE"])
def delete(id):
        cur = con.cursor()
        sql = " DELETE FROM students WHERE id = %s"
        cur.execute(sql,(id,))
        con.commit()
        return "", 204
        
if __name__ == "__main__":
    app.run(debug=True)
