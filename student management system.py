import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
course TEXT,
age INTEGER)
""")

conn.commit()

def add_student():
    name = input("Enter Name: ")
    course = input("Enter Course: ")
    age = int(input("Enter Age: "))

    cursor.execute("INSERT INTO students(name,course,age) VALUES(?,?,?)",
                   (name,course,age))
    conn.commit()
    print("Student Added Successfully")

def view_students():
    cursor.execute("SELECT * FROM students")
    data = cursor.fetchall()

    for i in data:
        print(i)

def search_student():
    name=input("Enter Name:")
    cursor.execute("SELECT * FROM students WHERE name=?",(name,))
    print(cursor.fetchall())

def delete_student():
    sid=int(input("Enter Student ID:"))
    cursor.execute("DELETE FROM students WHERE id=?",(sid,))
    conn.commit()
    print("Deleted Successfully")

while True:

    print("""
1.Add Student
2.View Students
3.Search Student
4.Delete Student
5.Exit
""")

    choice=input("Enter Choice:")

    if choice=="1":
        add_student()

    elif choice=="2":
        view_students()

    elif choice=="3":
        search_student()

    elif choice=="4":
        delete_student()

    elif choice=="5":
        break

conn.close()