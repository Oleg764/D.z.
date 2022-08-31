
# В программе создаётся виджет показа погоды в искомом городе.
#Город вводите в поле русскими или анг. буквами и нажимаете кнопку "показать погоду"

import tkinter as tk
import requests

api_key = '9a2dd6e4e2ea993332b549c1f50dea24'

def show():
    city = city_entry.get()
    weather = get_weather(city)
    location_label['text'] = f'{weather[0]}, {weather[1]}'
    img['file'] = f'Python10/weather_icons/{weather[3]}.png'
    weather_lbl['text'] = f'{weather[4]}'
    temp_lbl['text'] = f'Температура: {weather[2]:.0f}°C'
    

def get_weather(city):    
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)
    data = response.json()
    city = data['name']
    country = data['sys']['country']
    temp = data['main']['temp']-273.15
    icon = data['weather'][0]['icon']
    weather = data['weather'][0]['main']
    final = (city, country, temp, icon, weather)
    return final

root = tk.Tk()
root.title('Погода')
root.geometry('300x300')

city_entry = tk.Entry(root,font=14, width = 300, justify='center')
city_entry.pack()

location_label = tk.Label(root, text='Город', font=('bold', 20))
location_label.pack()

img = tk.PhotoImage(file='')
weather_image = tk.Label(root, image=img)
weather_image.pack()

weather_lbl = tk.Label(root, text='Погода', font=11)
weather_lbl.pack()

temp_lbl = tk.Label(root, text='Температура', font=11)
temp_lbl.pack()

show_btn = tk.Button(root, text='Показать погоду', font=10, command=show)
show_btn.pack()

root.mainloop()
 
  
