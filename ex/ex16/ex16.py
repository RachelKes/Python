#! /usr/bin/python3

import sqlite3

# adds an entry to the students table
def student_add(con, id, first, last, email, username, college):
    cur = con.cursor()
    cur.execute("insert into students values(?, ?, ?, ?, ?, ?)", (id, first, last, email, username, college))
    cur.close()

# adds an entry to the enrollments table
def enrollment_add(con, course_id, section_no, semester_id, student_id):
    cur = con.cursor()
    cur.execute("insert into enrollments values(null, ?, ?, ?, ?)", (course_id, section_no, semester_id, student_id))
    cur.close()

# returns all the rows in the students table
def students_list(con):
    cur = con.cursor()
    cur.execute("select * from students")
    for row in cur:
        print(row)
    cur.close()

# returns all the rows in the enrollments table
def enrollments_list(con):
    cur = con.cursor()
    cur.execute("select * from enrollments")
    for row in cur:
        print(row)
    cur.close()

con = sqlite3.connect("umb.db")
student_add(con, '04686471', 'Joe', 'Riley', 'Joe.Reiley003@umb.edu', 'reily', 'CM')
students_list(con)
enrollment_add(con, 'it244', 1, 'f17', '04686471')
enrollments_list(con)
