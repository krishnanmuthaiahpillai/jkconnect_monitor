import json
def parse_data(data_dump):
    #print data_dump
    parsed_input = json.load(data_dump)
    cellphones = parsed_input['cellphones']
    print cellphones



if __name__ == '__main__':
    # test1.py executed as script
    # do something
   parse_data(data_dump)
