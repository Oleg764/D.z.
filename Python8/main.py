# Дом. задание: 
#    Доработать тел. справочник: добавить графическую оболочку; использовать пакет модулей. 

from tkinter import *
import Imp_Exp_Del. import_data as imp
import Imp_Exp_Del. export_data as ex
root = Tk()
root.title("Телефонная книга")
root.iconbitmap("Python8\call-list.ico")

# создаем список
data = ex.export_data()

listbox = Listbox()

# добавляем в список начальные элементы
for data in data:
    listbox.insert(END, data)

listbox.pack(side=LEFT, fill=BOTH)
listbox.grid(row=2, column=0, columnspan=2, sticky=N+S+W+E, padx=5, pady=5)


# удаление выделенного элемента
def delete():
    #global selection
    selection = listbox.curselection()[0]


    # мы можем получить удаляемый элемент по индексу
    selected_data = listbox.get(selection)
    listbox.delete(selection)

    with open("Python8/phone.txt", "r+") as file:
        lines = file.readlines()
    
        del lines[selection]
    with open("Python8/phone.txt", "w+") as file:
        file.writelines(lines)

# добавление нового элемента


def add():
    new_data = tel_entry.get()
    listbox.insert(END, new_data)
    imp.import_data(new_data)


# Колонки ФИО ТЕЛ Примечание
Fio_label = Label(
    text="Фамилия     |    Имя      |   тел.          |   Примечание")
Fio_label.grid(row=1, column=0, sticky="w")

# текстовое поле и кнопка для добавления в список
tel_entry = Entry(textvariable=data, width=70)
tel_entry.grid(column=0, row=0, padx=6, pady=6)
add_button = Button(text="Добавить", command=add).grid(
    column=1, row=0, padx=6, pady=6)
delete_button = Button(text="Удалить", command=delete).grid(
    row=4, column=2, padx=5, pady=5)
root.mainloop()
