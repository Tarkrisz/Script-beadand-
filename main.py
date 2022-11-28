import proba
import pontok
print('Melyik játékkal akarsz játszani?')
print('1: számkitaláló')
print('2: akármi')
print('8: számkitatláló pontok')
igaz = True
while igaz:
    try:
        be = int(input('Nyomj meg egy számot'))
    except ValueError:
        print('Nem számot adtál meg')

    igaz = False

if(be==1):
    proba.ki()
elif(be==8):
    pontok.ponts()