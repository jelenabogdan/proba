#1
print('Hello world')

#2
a = 5 
b = 3
x = a + b
y = a - b
z = a * b
print(x, y, z)

print( 'Zbir je {}, razlika je {}, proizvod je {}'.format(x, y, z))
print( 'Zbir je {0}, razlika je {1}, proizvod je {2}'.format(x, y, z))
print( 'Zbir je {0:d}, razlika je {1:d}, proizvod je {2:d}'.format(x, y, z))
print( 'Zbir je %d, razlika je %d, proizvod je %d'%(x, y, z))

#3
a = int(input('Unesite prvi broj: '))
b = int(input('Unesite drugi broj: '))
kolicnik = a / b
celobrojni_kolicnik = a // b
stepen = a ** b
print('Količnik je {0:f}, celobrojni količnik je {1:d}, a stepen {2:d}'.format(kolicnik, celobrojni_kolicnik, stepen))

#4
a = float(input('Unesite prvi realan broj: '))
b = float(input('Unesite drugi realan broj: '))

print('Prvi broj je %.2f, drugi broj je %.3f'%(a, b))

#4.2
string = input('unestite string: ')
print("\"{}\"".format(string))

#5
s1 = input('Unestite string: ')
s2 = input('Unesite string: ')
print('{},{}'.format(s1, s2))

#6
broj1 = int(input('Unesite broj: '))
broj2 = int(input('Unesite broj: '))
broj1, broj2 = broj2, broj1
print(broj1, broj2)


