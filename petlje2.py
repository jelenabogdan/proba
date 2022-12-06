for sledeci in ['marko', 'milos', 'marija', 'ana', 'sofija']:
    print("hello", sledeci)
print("prva sledeća linija....")


for broj in [1, 2, 3, 4 , 4, 5]:
    print(broj)


for broj in range(21):
    print("stampanje brojeva ", broj)

for broj in range(5, 10, 2):
    print(broj)

for broj in range(100, 0, -1):
    print("prikaz", broj)

pozicija_automobila = 0
pozicija_cilja = 10

for kretanje in range(5):
    pozicija_automobila += 2
    print(pozicija_automobila == pozicija_cilja)

startDate = 2010
endDate = 2015
for i in range(startDate, endDate + 1):
    print(i)
for i in range(100):
    print("*", end="")
print()

print("1\t2\t3")
print("******************")

for i in range(1, 6):
    print(i * 1, end="\t")
    print(i * 2, end="\t")
    print(i * 3)


print(1 * 1, end="\t")
print(1 * 2, end="\t")
print(1 * 3, end="\n")
print(2 * 1, end="\t")
print(2 * 2, end="\t")
print(2 * 3, end="\n")
print(3 * 1, end="\t")
print(3 * 2, end="\t")
print(3 * 3)

print("volim \"Python\"")
print("delim brojeve: a/t")

for x in range(6):
    print(x, end="")
    for y in range(6):
        print("*", end=" ")
    print()

for x in range(5):
    for y in range(5):
        if x == y:
            print("#", end=" ")
        else:
            print("*", end=" ")
    print()

for x in range(5):
    for y in range(5):
        print("#" if (x + y) == 4 else "*", end=" ")
    print()

for x in range(5):
    for y in range(10):
        if (x == 0) or (y == 0) or (x == 4) or (y == 9):
            print("#", end=" ")
        else:
            print(" ", end=" ")
    print()

string = "3,9,13,4,42"
lista = string.split(",")
novi_string = ""
for i in range(5):
    if i != 4:
        novi_string = novi_string + str(int(lista[i])**2) + ","
    else:
        novi_string = novi_string + str(int(lista[i])**2)
print(novi_string)


def f_one(): 
    pass 
 
def f_two(): 
    pass 
 
def f_three(f): 
    print(id(f)) 
 
 
t = (f_one, f_two, f_three) 
for i in t: 
    print("Function:", i.__name__) 
    print("Object is instance of object:", isinstance(i, object)) 
    print("Id:", id(i))     
 
f_three(f_one)
