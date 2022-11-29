from tkinter import *
import sqlite3

def ponts():
    kapcsolat = sqlite3.connect('adatok.db')
    ab = kapcsolat.cursor()
    ab.execute('SELECT * FROM scours ORDER BY pontok')
    tomb = ab.fetchall()
    ablak = Tk()
    ablak.title('Pontok')
    ablak.minsize(height=250, width=100)
    ablak.maxsize(height=250, width=100)
    adatok = Label(ablak, text='Pontok', fg='red', font=10)
    adatok.grid(row=0, column=1, columnspan=2)
    nev = Label(ablak, text='Név')
    nev.grid(row=1, column=0)
    kor = Label(ablak, text='Pontok')
    kor.grid(row=1, column=2)
    sor = 3
    for t in tomb:
        cimke = Label(ablak, text=t[0])
        cimke.grid(row=sor, column=0)
        cimke2 = Label(ablak, text=t[1])
        cimke2.grid(row=sor, column=2)
        sor = sor + 1

    mainloop()
