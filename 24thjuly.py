# list
# to merge the 2 lists

input_lst1 = ["bat","ball","gaurd"]
input_lst2 = ["helmet","arm gaurd","bells"]
input_lst1.extend(input_lst2)
print(input_lst1)

#to remove the element at given index

input_lst = ["css","javascript","python",,"django","html"]
input_lst.pop(2)
print(input_lst)

# to remove the given elements in the list

input_lst = ["html","python","css","django","javascript"]
input_lst.remove("django")
print(input_lst)

# to check the common elements in 2 lists

input_lst1 = [10,20,30,40]
input_lst2 = [40,50,60,70]

common_element = False

for elements in input_lst1:
    if elements in input_lst2:
        common_element = True
        break
if common_element:
    print("there is a common element")
else:
    print("they is no common element")

# to remove the element in nested listed

nested_lst = [1,2,3,[4,5,6,[7,8,9]]]
nested_lst.remove(nested_lst[3])
print(nested_lst)

# to store the enter list into the single integer

lst = [10,20,30,40]

result =""
for num in lst:
    result += str(num)

result_int = int(result)
print(result_int)

#remove of the duplicate elements in the list

lst = [1,2,3,4,3,2,5,3,1,4,5,4,3,2]

unique_lst =[]

for new_element in lst:
    if new_element not in unique_lst:
        unique_lst.append(new_element)
print("the new list is",unique_lst)
