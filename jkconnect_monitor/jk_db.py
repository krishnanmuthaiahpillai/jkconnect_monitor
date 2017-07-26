import json
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
        print time
        print company
        print rssi
        print mac



if __name__ == '__main__':
    # test1.py executed as script
    # do something
   parse_data(data_dump)
