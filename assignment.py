"""#write a program which will find all such numbers 
which are divisible by 7 but are not a multible of 5 betwwen
 2000 and 3200(both included).the numbers obtained should 
be printed in a comma-seperated sequence on a single line"""
first_digit=int(input())
second_digit=int(input())
for divisible_by_7 in range(first_digit,second_digit+1):
    if divisible_by_7%7==0 and divisible_by_7%5!=0:
        print(divisible_by_7,end=",")

"""2.With a given integral number n, write a program to generate a dictionary that contains (i, 
i*i) such that is an integral number between 1 and n (both included). and then the program 
should print the dictionary. Suppose the following input is supplied to the program: 8 Then, 
the output should be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}"""

integral_num=int(input())
add_dic={}
for  dict_num in range(1,integral_num+1):
    add_dic[dict_num]=dict_num*dict_num
print(add_dic)

"""3..Write a program which accepts a sequence of comma-separated numbers from console 
and generate a list and a tuple which contains every number. Suppose the following input 
is supplied to the program: 34,67,55,33,12,98 Then, the output should be: ['34', '67', '55', 
'33', '12', '98'] ('34', '67', '55', '33', '12', '98')"""

number_add=eval(input())
list=[]
res=""
for change_num in number_add:
    change_num=str(change_num)
    list.append(change_num)
res=res+str((list))+" "+str((tuple(list)))
print(res)

"""4.Write a program that accepts a comma separated sequence of words as input and prints 
the words ina comma-separated sequence after sorting them alphabetically. Suppose the 
following input is supplied to the program: without, hello, bag, world Then, the output 
should be: bag,hello,without,world"""
comma_sep=eval(input()).split( )
list_1=[]
comma_sep=",".join(comma_sep)
for nums in comma_sep.split(","):
    nums=(str(nums))
    list_1.append(str(nums))
list_1.sort()
print(list_1)

"""5.Write a program that accepts a sentence and calculate the number of letters and digits. 
Suppose the following input is supplied to the program: hello world! 123 Then, the output 
should be: LETTERS 10 DIGITS 3"""

num_letters_digit=eval(input()).split()
num_letters_digit="".join(num_letters_digit)
letter=0
digit=0
result=""
for numbrs in num_letters_digit:
    if numbrs.isalpha():
        letter=letter+1
    elif numbrs.isdigit():
        digit=digit+1
    else:
        pass
result=result+"LETTERS " +str(letter)+" "+"DIGITS "+str(digit)
print(result)

"""6.Write a program that accepts a sentence and calculate the number of upper case letters 
and lower case letters. Suppose the following input is supplied to the program: Hello 
world! Then, the output should be: UPPER CASE 1 LOWER CASE 9"""

upper_lower=eval(input()).split()
upper_lower="".join(upper_lower)
count_upper=0
count_lower=0
ress=""
for upper_and_lower in upper_lower:
    if upper_and_lower.isupper():
        count_upper=count_upper+1
    elif upper_and_lower.islower():
        count_lower=count_lower+1
    else:
        continue
ress=ress+"UPPER CASE "+str(count_upper)+" "+"LOWER CASE "+str(count_lower)
print(ress)

"""7.Write a program that computes the net amount of a bank account based a transaction 
log from console input.The transaction log format is shown as following: D 100 W 200 D 
means deposit while W means withdrawal. Suppose the following input is supplied to the
program:" D 300 D 300 W 200 D 100 "Then, the output should be: 500"""

bank_account=eval(input()).split()
bank_account=",".join(bank_account)
bank_account=bank_account.split(",")
ADD_DIBIT=0
withdraw=0
for number in range(len(bank_account)):
    if bank_account[number]=="D":
        adding=bank_account[number+1]
        ADD_DIBIT=ADD_DIBIT+int(adding)
    elif bank_account[number]=="W":
        add=bank_account[number+1]
        withdraw=withdraw+int(add)
print(ADD_DIBIT-withdraw)
"""8.A website requires the users to input username and password to register. Write a 
program to check the validity of password input by users. Following are the criteria for 
checking the password:
At least 1 letter between [a-z]
At least 1 number between [0-9]
At least 1 letter between [A-Z]
At least 1 character from [$#@]
Minimum length of transaction password: 6
Maximum length of transaction password: 12 Your program should accept a sequence of 
comma separated passwords and will check them according to the above criteria. 
Passwords that match the criteria are to be printed, each separated by a comma. Example 
If the following passwords are given as input to the program: ABd1234@1,a 
F1#,2w3E*,2We3345 Then, the output of the program should be: ABd1234@1"""
password_checking=input().split(",")
for password_checkings in password_checking:
    password_checkings=password_checkings.strip()
    lower=False
    upper=False
    digit=False
    special=False
    if len(password_checkings)>=6 and len(password_checkings)<=12:
        for  char in password_checkings:
            print(char)
            if char.isalpha():
                if char.islower():
                    lower=True
                elif char.isupper():
                    upper=True
            elif char.isdigit():
                digit=True
            elif char in "@#$":
                special=True
        if lower and upper and digit and special:
            print("sucessfull")
        else:
            print("TRY AGAIN")
"""9.Define a function which can print a dictionary where the keys are numbers between 1 
and 20 (both included) and the values are square of keys."""

def add_elements():
    dic={}
    for number in range(1,l+1):
        dic[number]=number*number
    return dic
l=int(input())
print(add_elements())

"""10.Define a function which can generate a list where the values are square of numbers 
between 1 and 20 (both included). Then the function needs to print the last 5 elements in 
the list"""


def add():
    list=[]
    for num in range(1,nums):
        list.append([num,num*num])
    print(list)
nums=int(input())
add()