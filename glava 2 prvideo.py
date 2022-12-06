#8


for i in range(11):
    print(i, end=" ")
#9
for i in range(101):
    if i % 2 == 0:
        print(i, end = " ")

i = 1
while i < 101:
    if i % 2 == 0:
        print(i, end = " ")
    i = i + 1
#11
for i in range(31):
    if i % 3 != 0:
        print (i)

#12
a = int(input('Unesite broj'))
b = int(input('Unesite broj'))
if b < a:
    print('Greška')
else:
    for i in range(a, b + 1):
        print(i)
    print('Završeno')
#13
a = int(input('Unesite broj'))
i = a // 2
while i > 1:
    if (a % i == 0):
        print('NE')
        break
    else:
        if i == 2:
            print('DA')
    i = i - 1

#14
n = int(input('Unesite broj'))
suma = 0
for i in range (1, n + 1):
    if i% 6 == 0:
        suma = suma + i
print(suma)

#15
for i in range(5):
    for j in range(5):
        if j <= i:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()

#16
n = int(input('Unesite broj'))
m = int(input('Unesite broj'))
for i in range(m + 1):
    for j in range(n):
        if (i == 0) or (j == 0) or (i == m) or (j == n - 1):
            print('*', end = '')
        else:
            print(' ', end = '')
    print()



        

