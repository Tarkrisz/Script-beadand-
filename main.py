import proba, pontok, ko_papir_ollo, ko_papir_ollo_pontok

print('Melyik játékkal akarsz játszani?')
print('1: számkitaláló')
print('2: kő-papír-olló')
print('7: számkitatláló pontok')
print('8: kő-papír-olló pontok')
igaz = True
vege = True

while igaz:
    try:
        be = int(input('Nyomj meg egy számot'))
    except ValueError:
        print('Nem számot adtál meg')

    igaz = False

if (be == 1):
    proba.ki()
elif (be == 2):
    ko_papir_ollo.go()
elif (be == 7):
    pontok.ponts()
elif (be == 8):
    ko_papir_ollo_pontok.kpopontok()
