# to create an empty list in the tuple
 
word1 = ()
print(word1)
print(type(word1))
 
# to add an item into the tuple
 
word2 = ("python","css","html","js")
list = list(word2)
list[3] = "java script"
word2 = tuple(list)
print(word2)
 
# to convert a tuple into a string
 
word3 = ("python",)
changed_tuple = str(word3)
print(changed_tuple)    
 
 
 