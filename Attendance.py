import time
import requests

def attendance(name):
    json_to_export = {}
    json_to_export['name'] = name
    json_to_export['hour'] = f'{time.localtime().tm_hour}:{time.localtime().tm_min}'
    json_to_export['date'] = f'{time.localtime().tm_year}-{time.localtime().tm_mon}-{time.localtime().tm_mday}'
    r= requests.post(url='http://127.0.0.1:5000/receive_data', json=json_to_export)
    #print(r.text)
        