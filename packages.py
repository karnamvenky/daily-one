# functions

def add(a,b):
    return a + b
def sub(a,b):
    return a - b

# recursive function
# factorial programe

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)
result1 = fact(6)
print(result1)

#sum of numbers programe

def sum(n):
    if n == 0:
        return 0
    else:
        return n + sum(n-1)

result2 = sum(5)
print(result2)

# lambda function 

add = lambda x,y : x+y
print(add(30,2000))


condd = lambda x,y: x if x > y else y
print(condd(100,200))

#iterations
#map

l = [1,2,3,4,5,6,7,8,9]
def add(x):
    return x +1
new = list(map(add,l))
print(new)

# filter

l = [1,2,3,4,5,6,7,8,9]
def fil(x):
    if x%2 == 0:
        return x
new = list(filter(fil,l))
print(new)

l=[1,2,3,4,5,6,7]
fil = lambda x:x if x%2 == 0 else False
new = list(filter(fil,l))
print(new)

# reduce()
from functools import *
l = [1,2,3,4,5,6,7]
sum = sum(4)
print(sum)

def sum(x,y):
    return x + y
def_sum = reduce(sum,l)
print(def_sum)

l = [1,2,3,4,5,6,7,8,9]
add = lambda x,y:x+y
new = reduce(add,l)
print(new)
 