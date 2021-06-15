from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Column
from App import db
from sqlalchemy import Integer, String, Date, Time, ForeignKey

class Employee(db.Model):
    __tablename__ = 'employee'
    employee_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False)
    image_path = Column(String(40), nullable=False)
    attendances = relationship('Attendance',backref='employee', lazy=False)

    def __str__(self):
        return self
    

class Attendance(db.Model):
    __tablename__ = 'attendance'
    checkin_id = Column(Integer, primary_key=True, autoincrement=True)
    attendance_status = Column(Integer, autoincrement=True) # 0 là check in, 1 là check out
    attendance_date = Column(Date, nullable=False)
    attendance_time = Column(Time, nullable=False)
    employee_id = Column(Integer, ForeignKey(Employee.employee_id), nullable= False)

    def __str__(self):
        return self


if __name__ == "__main__":
    db.create_all()