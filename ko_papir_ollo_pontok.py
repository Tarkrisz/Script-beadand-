import sqlite3
from tkinter import *

def kpopontok():
    kapcsolat = sqlite3.connect('adatokkpo.db')
    ab = kapcsolat.cursor()
    ab.execute('SELECT * FROM scours ORDER BY win DESC')
    tomb = ab.fetchall()
    ablak = Tk()
    ablak.title('Pontok')
    ablak.minsize(width=250, height=400)
    adatok = Label(ablak, text='Pontok', fg='red', font=10, anchor='center')
    adatok.grid(row=1, column=1 , columnspan=5, pady=10)
    nev = Label(ablak, text='Név')
    nev.grid(row=2, column=0)
    win = Label(ablak, text='Győzelmek')
    win.grid(row=2, column=1)
    draw = Label(ablak, text='Döntetlenek')
    draw.grid(row=2, column=2)
    loose = Label(ablak, text='Veszteségek')
    loose.grid(row=2, column=3)
    sor = 4
    for t in tomb:
        cimke = Label(ablak, text=t[0])
        cimke.grid(row=sor, column=0)
        cimke2 = Label(ablak, text=t[1])
        cimke2.grid(row=sor, column=1)
        cimke3 = Label(ablak, text=t[2])
        cimke3.grid(row=sor, column=2)
        cimke4 = Label(ablak, text=t[3])
        cimke4.grid(row=sor, column=3)
        sor = sor + 1


    mainloop()