#6.2
ceo = int(input('Unesite ceo broj: '))
realan = float(input('Unesite realan broj: '))
string = input('Unesite string: ')
lista = [ceo, realan, string]
lista1 = [float(ceo), round(realan), string]
lista2 = [str(ceo), str(realan), string]
print(lista)
print(lista1)
print(lista2)

#7
br1 = int(input('Unesite broj:'))
br2 = int(input('Unesite broj:'))
if br1 != br2:
    if br1 > br2:
        print(' Brojevi su različiti. Broj {} je veći od {}.'.format(br1, br2))
    else:
        print(' Brojevi su različiti. Broj {} je manji od {}.'.format(br1, br2))
else:
    print('Brojevi su jednaki')

#8
broj = float(input('Unesite realan broj:'))
print('Broj je veći ili jednak 0' if (broj >= 0) else 'Broj je manji od 0')

#9
broj = int(input('Unesite broj:'))
if (broj < 10) and (broj > 0):
    print('Broj {} je u intervalu od 1 do 10'.format(broj))
else:
    print('Broj {} nije u intervalu'.format(broj))
#print(broj > 0 and broj < 10)
#10
broj = int(input('Unesite broj:'))
if broj != 5:
    print('Broj {} nije jednak 5'.format(broj))
else:
    print('Broj {} je jednak 5'.format(broj))
# print(broj != 5)
#11
broj = int(input('Unesite broj: '))
print('DA' if (broj % 2 == 0) else 'NE')

#12





#13
lista = [1, 2, 3, 4]
print(lista[2])
print(lista[0:3])
lista.pop(1)
print(lista)
lista.reverse()
print(lista)

#14
n = (3.4, 5.6, 7.2, 1.2, 13.4)
print(n)
print(n[4])
l = list(n)
l[4] = 0
n = tuple(l)
print(n)

#15
recnik = {'RS':'Srbija', 'ES': 'Španija', 'GB': 'Engleska', 'DE': 'Nemačka'}
recnik['BG'] = 'Bugarska'
print(recnik)
print(recnik['RS'])




