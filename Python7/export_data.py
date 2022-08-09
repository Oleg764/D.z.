# модуль экспорта данных 

def export_data():
    with open('Python8/phonebook/phone1.txt', 'r+') as f:
        data = []
        t = []
        for line in f:
            if ',' in line:
                temp = line.strip().split(',')
                data.append(temp)
            elif ';' in line:
                temp = line.strip().split(';')
                data.append(temp)
            elif ':' in line:
                temp = line.strip().split(':')
                data.append(temp)        
            elif line != '':
                if line != '\n':
                    t.append(line.strip())
                else:
                    data.append(t)
                    t= []
    return data
print (export_data())    