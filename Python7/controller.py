from import_data import import_data
from export_data import export_data
from print_data import print_data
def greeting():
    print("Здравствуйте!")

def input_data():
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    phone_number = input("Введите телефон: ")
    note = input("Введите примечание: ")
    return [last_name, first_name, phone_number, note]

def choice_sep():
    sep = input("Введите разделитель: ")
    if sep == "":
        sep = None
    return sep

def choice_first():
    print("Что желаем сделать:\n\
    1 - импорт;\n\
    2 - экспорт;\n ")
    ch = input("Введите цифру: ")
    if ch == '1':
        sep = choice_sep()
        import_data(input_data(), sep)
    elif ch == '2':
        data = export_data()
        print_data(data)
    