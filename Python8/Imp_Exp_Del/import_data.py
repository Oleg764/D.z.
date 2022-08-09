# модуль 

def import_data(data):
    with open('Python8/phone.txt', 'a+') as file:
        
        file.write(data)
       # file.write(f"\n")
#def del_data(data) : 
#   global selection
#   with open("Python8/phone.txt", "r+") as file:
#    lines = file.readlines()
#    print(lines)
#    del lines[selection]
#    with open("Python8/phone.txt", "w+") as file:
#        file.writelines(lines)         