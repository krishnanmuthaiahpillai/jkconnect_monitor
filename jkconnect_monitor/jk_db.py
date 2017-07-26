import json
import sqlite3
import datetime

def parse_data(data_dump):
    #print data_dump
    parsed_input = json.loads(data_dump)
    cellphones = parsed_input['cellphones']
    #print cellphones
    for element in parsed_input['cellphones']:
        company = element['company']
        time = datetime.datetime.fromtimestamp(int(parsed_input['time'])).strftime('%Y-%m-%d %H:%M:%S')
        rssi=element['rssi']
        mac=element['mac']
        #print time
        #print company
        #print rssi
        #print mac
        check_field_already_exist_in_database(rssi,company,mac,time)

# Check Fields Already Exist in Database
# Check with MAC address which already exists.
def check_field_already_exist_in_database(rssi,company,mac,time ):
  try:
    conn = sqlite3.connect('jkconnect.db')
    conn.execute('''CREATE TABLE IF NOT EXISTS CONNECT
         (MAC TEXT PRIMARY KEY     NOT NULL,
         COMPANY           TEXT    NOT NULL,
         RSSI            TEXT     NOT NULL,
         TIME         TEXT);''')

    cursor = conn.execute("SELECT MAC from CONNECT where MAC=(?)", (mac,))
    data = cursor.fetchall()
    if not data:
        #normal_insert_field_into_database(rssi,company,mac,time)
        print ('not found')
    else:
        #time_insert_field_into_database(rssi,company,mac,time)
        print ('found')

    conn.close()
  except Exception as e:
    print e
  finally:
    conn.close()


if __name__ == '__main__':
    # test1.py executed as script
    # do something
   parse_data(data_dump)
