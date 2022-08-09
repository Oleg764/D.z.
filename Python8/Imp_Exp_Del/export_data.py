# модуль экспорта данных 
import re
def export_data():
    with open('Python8/phone.txt', 'r+') as f:
        data =[]    
        
        for line in f:
            line = re.sub(r'[.;,]',' ',line) 
            data.append(line)    
    return data