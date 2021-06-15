from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
import pymysql
import Dao



app = Flask(__name__)
CORS(app, support_credentials=True)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:ToFu;475632891@localhost/attendance?charset=utf8mb4"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db =SQLAlchemy(app=app)

# def DATABASE_CONNECTION():
#     cnx = mysql.connector.connect(user='root', password='ToFu;475632891',
#                             host='127.0.0.1',
#                             database='attendance')
#     return cnx


@app.route('/receive_data', methods=['POST'])
def get_receive_data():
    if request.method == 'POST':
        json_data = request.get_json()
        id =  Dao.selectEmployeeByPath(json_data["name"])
        if(Dao.checkAttendance(id[0],json_data["date"],0) == False):
            Dao.attendance(id[0],json_data["date"],json_data["hour"],0)
        else:
            if(Dao.checkAttendance(id[0],json_data["date"],1)== False):
                Dao.attendance(id[0],json_data["date"],json_data["hour"],1)
            else:
                Dao.updateCheckOut(id[0],json_data["date"],json_data["hour"])
    return jsonify("Hello")


# * -------------------- RUN SERVER -------------------- *
if __name__ == '__main__':
    # * --- DEBUG MODE: --- *
    app.run(host='127.0.0.1', port=5000, debug=True)