import random
import sqlite3

def ki():
    kapcsolat = sqlite3.connect('adatok.db')
    ab = kapcsolat.cursor()
    ab.execute('CREATE TABLE IF NOT EXISTS scours (nev TEXT, pontok INTEGER)')
    nev = input('Add meg a neved')
    print('Kedves',nev, 'gondoltam egy számra 1 és 100 között: ')
    igaz = True
    db = 0
    talal = random.randint(0, 100)
    while igaz:
        print(talal)
        beker = input()
        szam = int(beker)
        if (szam < talal):
            print('Kicsi a szám')
            db = db + 1
        elif (szam > talal):
            print('Nagy a szám')
            db = db + 1
        else:
            print('Erre a számra gondoltam')
            db = db + 1
            print(db, '.-re találtad el')
            ab.execute('INSERT INTO scours VALUES (?,?)',(nev, db))
            kapcsolat.commit()
            print('Újra megpróbálod?')
            beker = input()
            if (beker == 'y'):
                talal = random.randint(0, 100)
            else:
                igaz = False

    ab.close()
    kapcsolat.close()