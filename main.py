from bs4 import BeautifulSoup
import datetime
import tkinter as tk
from tkinter import ttk
from constants import *
import requests

window = tk.Tk()
window.title("Currency Converter")

today = datetime.datetime.now()
date = ""
date += today.strftime("%b") + " " + today.strftime("%d") + " " + today.strftime("%H") + ":" + \
        today.strftime("%M") + " " + today.strftime("%p") + " " + today.strftime("%Z")
dates = tk.Label(text=str(date))
dates.grid(row=1, column=1)

currname = tk.Label(text="Currency Name")
currname.grid(row=1, column =2)

combobox = ttk.Combobox(window, values=currency_list, state='readonly')
combobox.grid(row=2, column=2)
combobox.current(0)

combobox_two = ttk.Combobox(window, values=currency_list, state='readonly')
combobox_two.grid(row=3, column=2)
combobox_two.current(0)

currval = tk.Label(text="Currency Value")
currval.grid(row=1, column=0)

val = tk.Entry(window, justify='center')
val.grid(row=2, column=0)

def converter():
    curr_temp = combobox.get()
    curr_temp_two = combobox_two.get()

    curr1 = ""
    curr2 = ""

    for i in range(len(curr_temp)):
        if curr_temp[i] == " ":
            curr1 += "+"

        else:
            curr1 += curr_temp[i]

    for i in range(len(curr_temp_two)):
        if curr_temp_two[i] == " ":
            curr2 += "+"

        else:
            curr2 += curr_temp_two[i]



    url = f"https://www.google.com/search?q={curr1}+to+{curr2}"
    data = requests.get(url)

    soup = BeautifulSoup(data.text, 'html.parser')

    values = soup.get_text()

    index = values.find("=")
    index2 = values.find(" ", index)

    value = values[index + 1: index2]

    x = val.get()

    if curr1 == curr2:
        final = tk.Label(text=str(x))

    else:
        new_curr = float(value) * float(x)
        final = tk.Label(text=str(new_curr))

    final.grid(row=3, column = 0)


button = tk.Button(window,
    text="Convert!",
    width=15,
    height=3,
    command=converter)

button.grid(row=4, column=1)

window.mainloop()


