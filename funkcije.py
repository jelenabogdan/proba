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

f = lambda x : x^2 if x < 5 else (x^3 if x > 5 else x)
print(f(2))
print(f(3))
print(f(4))
print(f(5))
print(f(6))
print(f(7))
print(f(8))