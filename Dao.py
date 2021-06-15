from sqlalchemy.orm import query
from App import db
from Models import *
from flask import jsonify


def checkAttendance(employee_id, date, status):
    c= db.session.execute("SELECT * FROM attendance.attendance WHERE attendance_status= "+ str(status) +" and employee_id = "+ str(employee_id) +" and attendance_date = '" + str(date) + "';")
    c = [p for p in c]
    print(c)
    if c:
        return True
    return False

def selectEmployeeByPath(path):
    c = db.session.execute("SELECT employee_id FROM attendance.employee WHERE image_path = '"+ path+ "';")
    c = [p for p in c]
    return c[0]

def attendance(employee_id, date,time, status):
    c = Attendance(attendance_status = status, attendance_date=date, attendance_time=time, employee_id=employee_id)
    db.session.add(c)
    db.session.commit()

def updateCheckOut(employee_id,date, time):
    db.session.execute("UPDATE attendance.attendance SET attendance_time = '"+ time +"' WHERE attendance_status = 1 AND employee_id = "+ str(employee_id) +" AND attendance_date = '" + str(date) + "';")
    db.session.commit()
    