from bs4 import BeautifulSoup
from datetime import date
import tkinter as tk
import requests

window = tk.Tk()
title = tk.Label(text="Currency Converter")
title.grid(row=0, column=1)

today = date.today()
dates = tk.Label(text=str(today))
dates.grid(row=1, column=1)

currname = tk.Label(text="Currency Name")
currname.grid(row=1, column =2)

entry1 = tk.Entry(window, justify='center')
entry1.grid(row = 2, column=2)

entry2 = tk.Entry(window, justify='center')
entry2.grid(row=3, column=2)

currval = tk.Label(text="Currency Value")
currval.grid(row=1, column=0)

val = tk.Entry(window, justify='center')
val.grid(row=2, column=0)

def converter():
    curr1 = tk.Entry.get(entry1)
    curr2 = tk.Entry.get(entry2)

    url = f"https://www.google.com/search?q={curr1}+to+{curr2}"
    data = requests.get(url)

    soup = BeautifulSoup(data.text, 'html.parser')

    values = soup.get_text()

    index = values.find("=")
    index2 = values.find(" ", index)

    value = values[index + 1: index2]

    x = val.get()

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


