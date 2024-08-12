# to filter the number of the given list

l = [1,2,3,4,5,6,7,8,9,10]
def fil(a):
    if a%2 == 0:
        return a
new = list(filter(fil,l))
print(new)

# to map the given list and to square the elements of list

input_list = [1,2,3,4,5,6,7,8,9,10]
def square(a):
    return a * a
result_list = list(map(square,input_list))
print(result_list)

# to find the even numbers in the list and to square them 

input_list = [1,2,3,4,5,6,7,8,9,10]
def numbers(a):
    if a%2 == 0:
        return a
def even_squares(a):
    return a * a
even_numbers = filter(numbers,input_list)
squares_evens = map(even_squares,even_numbers)
result_list = list(squares_evens)
print(result_list)

# to make the even numbers squares list in the range of  1 to 20 

numbers = range(1,21)
def filters(a):
    if a%2 == 0:
        return a

even_numbers = filter(filters,numbers)
result_list = list(even_numbers)
print(result_list)

# to make the map of the even number of the list

numbers = range(1,21)
def filters(a):
    if a%2 == 0:
        return a
def squares(a):
    return a * a

even_numbers = filter(filters,numbers)
square_list = map(squares,even_numbers)
result_list = list(square_list)
print(result_list)

# to create a class and a sub class

class American:
    def _init_(self,name,age):
        self.name = name
        self.age = age

    def greet(self):
        return f"my name is {self.name} and my age is {self.age}"
    
    def nationality(self):
        return "American"
    
class NewYorker(American):
    def _inti_(self,name,age,purpose):
        super()._init_(self,name,age)
        self.purpose = purpose

    def greet(self):
        base_greeting = super.greet()
        return f"{base_greeting} i am here is for {self.purpose}"
    
    def nationality(self):
        return "NewYorker"
    
if __name__ == "_main_":
    person = American("venkat",27)
    reason = NewYorker("virat",27,"for masters")

    print(person.greet())
    print(person.nationality())

    print(reason.greet())
    print(reason.nationality())
    

# to captilize the first and fourth letter of a string using function 

def captial(name):
    if len(name) < 4 :
        print("in valid string")

    first_letter = name[0].upper()
    forth_letter = name[3].upper()

    new_string = first_letter + name[1:3] + forth_letter +name[4:]
    return new_string

name = "venkat"
print(captial(name))

# to create a class with name rectangle an to find the area of it 

class Rectangle:
    def _init_(self,width,length):
        self.width = width
        self.length = length

    def area(self):
        return self.length * self.width
    
if __name__ == "_main_":
    rect = Rectangle(5,3)

    print(f"the area of rectangle is:{rect.area()}")

# to check where the 2 strings match with same letters or not using function

def same_string(two_strings):
    words = two_strings.split()

    if len(words) != 2:
        print("input must be 2 worded string")

    word1 = words[0][0].lower()
    word2 = words[1][0].lower()

    return word1 == word2

print(same_string("hello venkat"))
print(same_string("hello virat"))

# comparision of 2 numbers using function

def numbers(num1,num2):

    if num1%2 == 0 and num2%2 == 0:
        return min(num1,num2)
    else:
        return max(num1,num2)
    
print(numbers(5,6))
print(numbers(10,1))