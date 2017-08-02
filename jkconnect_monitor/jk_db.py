import json
import sqlite3
import datetime

# Parse Method
# parse the json file with values: Mac,rssi,company,time
def parse_data(data_dump):
   parsed_input = json.loads(data_dump)
   cellphones = parsed_input['cellphones']
   for element in parsed_input['cellphones']:
         company = element['company']
         #time = datetime.datetime.fromtimestamp(int(parsed_input['time'])).strftime('%Y-%m-%d %H:%M:%S')
         time = str(parsed_input['time'])
         rssi=element['rssi']
         mac=element['mac']
         check_field_already_exist_in_database(rssi,company,mac,time)

   #retrive_data_from_database()


# Retrive Data :
# retrive the data from DataBase
# def retrive_data_from_database():
#   try:
#    path = '/home/pi/jkconnect.db'
#    conn = sqlite3.connect(path)
#    print "Opened database successfully";
#    cursor = conn.execute("SELECT MAC, COMPANY, RSSI, TIME from CONNECT")
#    for row in cursor:
#       print "MAC = ", row[0]
#       print "COMPANY = ", row[1]
#       print "RSSI = ", row[2]
#       print "TIME = ", row[3], "\n"
#       print 'HELLO'
#   except Exception as e:
#     print e
#   finally:
#     conn.close()


# Check Fields Already Exist in Database
# Check with MAC address which already exists.
def check_field_already_exist_in_database(rssi,company,mac,time ):
  try:
    path = '/home/pi/jkconnect.db'
    conn = sqlite3.connect(path)
    conn.execute('''CREATE TABLE IF NOT EXISTS CONNECT
         (MAC TEXT PRIMARY KEY     NOT NULL,
         COMPANY           TEXT    NOT NULL,
         RSSI            TEXT     NOT NULL,
         TIME         TEXT);''')

    cursor = conn.execute("SELECT MAC from CONNECT where MAC=(?)", (mac,))
    data = cursor.fetchall()
    if not data:
        normal_insert_field_into_database(rssi,company,mac,time)
       #  print ('not found')
    else:
        time_insert_field_into_database(rssi,company,mac,time)
       #  print data

    conn.close()
  except Exception as e:
    print e
  finally:
    conn.close()



# Normal INSERT fields into Database
# Normally Insert field into database with Mac,rssi,company,time
def normal_insert_field_into_database(rssi,company,mac,time ):
  try:
    path = '/home/pi/jkconnect.db'
    conn = sqlite3.connect(path)
    conn.execute('''CREATE TABLE IF NOT EXISTS CONNECT
         (MAC TEXT PRIMARY KEY     NOT NULL,
         COMPANY           TEXT    NOT NULL,
         RSSI            TEXT     NOT NULL,
         TIME         TEXT);''')
    conn.execute('''INSERT INTO CONNECT(MAC, COMPANY, RSSI, TIME)
                  VALUES(?,?,?,?)''', (mac,company,rssi, time))
    conn.commit()
    print "Records created successfully";
    conn.close()

  except Exception as e:
    print e
  finally:
    conn.close()




# Normal INSERT fields into Database
# Normally Insert field into database with Mac,rssi,company,time
def time_insert_field_into_database(rssi,company,mac,time ):
  try:
    path = '/home/pi/jkconnect.db'
    conn = sqlite3.connect(path)
    conn.execute('''CREATE TABLE IF NOT EXISTS CONNECT
         (MAC TEXT PRIMARY KEY     NOT NULL,
         COMPANY           TEXT    NOT NULL,
         RSSI            TEXT     NOT NULL,
         TIME         TEXT);''')
    time_cursor = conn.execute("SELECT TIME from CONNECT where MAC=(?)", (mac,))
    rssi_cursor = conn.execute("SELECT RSSI from CONNECT where MAC=(?)", (mac,))
    old_time =time_cursor.fetchone()[0]
    old_rssi=rssi_cursor.fetchone()[0]
    time_list= [str(old_time),str(time)]
    rssi_list=[str(old_rssi),str(rssi)]
    join_time=':$:'.join(time_list)
    join_rssi=':$:'.join(rssi_list)
    conn.execute("UPDATE CONNECT SET TIME = (?) WHERE MAC= (?)",(join_time, mac))
    conn.execute("UPDATE CONNECT SET RSSI = (?) WHERE MAC= (?)",(join_rssi, mac))
    conn.commit()
    conn.close()

  except Exception as e:
    print e
  finally:
    conn.close()



if __name__ == '__main__':
    # test1.py executed as script
    # do something
   parse_data(data_dump)
