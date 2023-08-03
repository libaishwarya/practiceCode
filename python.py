import mysql.connector
con = mysql.connector.connect(host="localhost",user="root", password="PASSWORD",database="CRUD")

def insert():
    
    Name = input("Enter the name: ")
    Email = input("Enter the emailID: ")
    Phone = input("Enter the phone number : ")
    
    res = con.cursor()
    sql ="insert into students(name,email,phone) values(%s,%s,%s)"
    res.execute(sql,(Name,Email,Phone))
    res.execute("select last_insert_id()")
    studentID = res.fetchone()[0]
    con.commit()
    print("\n")
    print("Student data inserted ")
    print("\n")
    print("Student ID is",studentID)
    
def select():
    res = con.cursor()
    sql = "select name,email,phone from students WHERE id = %s "
    id = int(input("Enter the ID: "))
    res.execute(sql,(id,))
    result = res.fetchone()
    con.commit()
    print(result)
    
    # if result:
    #     print(result[0])
    #     print(result[1])
    #     print(result[2])

def update():
    res = con.cursor()
    sql = "select name from students WHERE id = %s "
    id = int(input("Enter the ID: "))
    # sql = "UPDATE students SET name = %s WHERE id = %s;"
    # id = int(input("Enter the Id to be changed: "))
    res.execute(sql,[id,])
    result = res.fetchone()
    con.commit()
    
    def updateName():
        res = con.cursor()
        sql = "UPDATE students SET name = %s WHERE id = %s;"
        id = int(input("Enter the Id to be changed: "))
        name = str(input("Enter the name to be changed: "))
        res.execute(sql,(name,id))
        result = res.fetchall()
        con.commit()
        print(result)
        
    def updateEmail():
        res = con.cursor()
        sql = "UPDATE students SET email = %s WHERE id = %s;"
        id = int(input("Enter the Id to be changed: "))
        email = str(input("Enter the emailID to be changed: "))
        res.execute(sql,(email,id))
        result = res.fetchall()
        con.commit()
        print(result)
        
    def updatePhone():
        res = con.cursor()
        sql = "UPDATE students SET phone = %s WHERE id = %s;"
        id = int(input("Enter the Id to be changed: "))
        phone = str(input("Enter the phone number to be changed: "))
        res.execute(sql,(phone,id))
        result = res.fetchall()
        con.commit()
        print(result)
    
    if result:
        print("1. Update Name")
        print("2. Update Email")
        print("3. Update Phone")
        print("4. Exit")
        print("\n")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            updateName()
        elif choice == 2:
            updateEmail()
        elif choice == 3:
            updatePhone()
        else:
            quit()
        
while True:
        print('\n')
        print("1. Insert Record")
        print("2. Select Record")
        print("3. Update Record")
        print("4. Delete Record")
        print("5. Exit")
        print("\n")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            insert()
        elif choice == 2:
            select()
        elif choice == 3:
            update()
        # elif choice == 4:
        #     delete()
        elif choice == 5:
            quit()
        else:
            print("Invalid choice")
            
        