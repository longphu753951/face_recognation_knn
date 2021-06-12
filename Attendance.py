from datetime import datetime


def attendance(name):
    with open('checkin.csv','r+') as f:
        nowDate = datetime.today().strftime('%d-%m-%Y')
        nowTime = datetime.today().strftime('%H:%m:%S')
        for row in f:
            column = row.split(",")
            if(column[0] == name):
                return
        f.writelines(f'\n{name},{nowDate},{nowTime}')
        

        