import random, sqlite3

def go():
    kapcsolat = sqlite3.connect('adatokkpo.db')
    ab = kapcsolat.cursor()
    ab.execute('CREATE TABLE IF NOT EXISTS scours (nev TEXT, win INTEGER, draw INTEGER, loose INTEGER)')
    nev = input('Add meg a neved')
    print('Kedves', nev, 'kezdődjék a játék!')
    aiWin = 0
    plWin = 0
    draw = 0
    endGame = 0
    rounds = 0
    while endGame < 5:
        try:
            plBe = int(input('Nyomd emg amelyiket választod: 1 - Kő | 2 - Papír | 3 - Olló'))
        except ValueError:
            print('Nem számot adtál meg')
        aiBe = random.randint(1,3)
        print('Ai Tipp: ' , aiBe, 'Te tipped: ', plBe)
        print(rounds , ' Forduló!')
        if(plBe == aiBe):
            print('Döntetlen! Ai tipp: ', aiBe, ' Te tipped: ', plBe)
            draw = draw + 1
        elif(plBe == 1 and aiBe == 3):
            print('Nyertél! Ai tipp: ', aiBe, ' Te tipped: ', plBe)
            plWin = plWin + 1
        elif(plBe == 2 and aiBe == 1):
            print('Nyertél! Ai tipp: ', aiBe, ' Te tipped: ', plBe)
            plWin = plWin + 1
        elif(plBe == 1 and aiBe == 2):
            print('Vesztettél! Ai tipp: ', aiBe, ' Te tipped: ', plBe)
            aiWin = aiWin + 1
        elif(plBe == 2 and aiBe == 3):
            print('Vesztettél! Ai tipp: ', aiBe, ' Te tipped: ', plBe)
            aiWin = aiWin + 1

        endGame = endGame + 1

    if(aiWin == plWin):
        print('Döntetlen lett a játék!')
    elif(aiWin < plWin):
        print('Nyertél!')
    else:
        print('Vesztettél!')

    ab.execute('INSERT INTO scours VALUES (?,?,?,?)', (nev, plWin, draw, aiWin))
    kapcsolat.commit()

    ab.close()
    kapcsolat.close()
