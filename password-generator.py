import ttkbootstrap
import tkinter as tk
from random import choice

def generate_password():
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789.+-*@#$%&_='
    password = ''
    password_lenght = entered_password_lenght.get()
    for num in range(password_lenght):
        password += choice(characters)
    output.set(f'{password}\n')

window = ttkbootstrap.Window(themename='minty')
window.title('Password Generator')
window.geometry('400x300')

title_label = ttkbootstrap.Label(master=window,
                                 text='Password Generator',
                                 font='Calibri 28')
title_label.pack()

input_frame = ttkbootstrap.Frame(master=window)

entered_password_lenght = tk.IntVar()
password_lenght_label = ttkbootstrap.Label(master=input_frame,
                                           text="What's the lenght of the password?",
                                           font='Calibri 12')
entry_password_lenght = ttkbootstrap.Entry(master=input_frame,
                                           textvariable=entered_password_lenght)

button = ttkbootstrap.Button(master=input_frame,
                             text='Generate Password',
                             command=generate_password)

password_lenght_label.pack(pady=5)
entry_password_lenght.pack(pady=5)

button.pack(pady=5)
input_frame.pack(pady=5)

output = tk.StringVar()
output_label = ttkbootstrap.Label(master=window,
                                  font='Calibri 20',
                                  textvariable=output)
output_label.pack(pady=10)

window.mainloop()
