import ijson
import re
def Wczytani(Json_file):
    with open (Json_file, 'rb') as file:
        pattern1 = 'v1.[0-2000]'
        pattern_width = 'width.[0-9]'
        pattern_height = 'height.[0-9]'
        parser = ijson.parse(file)
        v1=[]
        width=[]
        height=[]
        for prefix, event, value in parser:
            if re.match(pattern1,prefix):
                if event == 'start_array':
                    tmp = []
                if event == 'number':
                    tmp.append(value)
                if event == 'end_array':
                    v1.append(tmp)
            if re.match(pattern_width, prefix):
                width.append(value)
            if re.match(pattern_height, prefix):
                height.append(value)
        print(str(v1))
        return v1, width, height

