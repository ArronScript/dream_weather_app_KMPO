import tkinter as tk
import requests
from PIL import Image, ImageTk

root = tk.Tk()

root.title("Weather App by Команда мечты КМПО")
root.geometry("600x500")


def format_response(weather):
    try:
        temp = weather['main']['temp']
        feels_like = weather['main']['feels_like']
        min_temp = weather['main']['temp_min']
        max_temp = weather['main']['temp_max']
        pressure = weather['main']['pressure']
        humidity = weather['main']['humidity']
        final_str = (f' Температура: {int(temp - 32)} \n Ощущается как: {int(feels_like - 32)} \n '
                     f'Мин. температура: {int(min_temp - 32)} \n Макс. температура: {int(max_temp - 32)} \n Давление: {int(pressure)} \n Влажность: {int(humidity)}')
    except:
        final_str = 'Город не найден!'
    return final_str


def get_weather(city):
    weather_key = '2c481575c96a35678b7b4ec3d1f441d6'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
    response = requests.get(url, params)
    weather = response.json()
    result['text'] = format_response(weather)

    icon_name = weather['weather'][0]['icon']
    open_image(icon_name)


def open_image(icon):
    size = int(frame_two.winfo_height() * 0.25)
    img = ImageTk.PhotoImage(Image.open('img/' + icon + '.png').resize((size, size)))
    weather_icon.delete('all')
    weather_icon.create_image(0, 0, anchor='nw', image=img)
    weather_icon.image = img


img = Image.open('bg.png')
img = img.resize((600, 500), Image.ANTIALIAS)
img_photo = ImageTk.PhotoImage(img)

bg_lbl = tk.Label(root, image=img_photo)
bg_lbl.place(x=0, y=0, width=600, height=500)

frame_one = tk.Frame(bg_lbl, bg="#2e3042", bd=5)
frame_one.place(x=80, y=60, width=450, height=50)

txt_box = tk.Entry(frame_one, font=('times new roman', 25), width=17)
txt_box.grid(row=0, column=0, sticky="w")

btn = tk.Button(frame_one, text="     Погода    ", fg='#242e87', font=('times new roman', 16, 'bold'),
                command=lambda: get_weather(txt_box.get()))
btn.grid(row=0, column=1, padx=10)

frame_two = tk.Frame(bg_lbl, bg="#2e3042", bd=5)
frame_two.place(x=80, y=130, width=450, height=300)

result = tk.Label(frame_two, font=('times new roman', 19), bg='white', justify='left', anchor='nw')
result.place(relwidth=1, relheight=1)

weather_icon = tk.Canvas(result, bg='white', bd=0)
weather_icon.place(relx=.75, rely=0, relwidth=1, relheight=0.5)

root.mainloop()
