# varaibles in oops

# instance varaible 

class cricketer:
    def __init__(self,name,runs,avg):
        self.name = name
        self.runs = runs
        self.avg = avg
    def f1(self):
        print(self.name)  
        print(self.runs)
        print(self.avg) 
        print(self.role)
c = cricketer("virat",25000,58) 
c.role = "batsmen"
print(c.cricketer)        

class Actor:
    def act(self,name,number,value):
        self.name = name
        self.number = number
        self.value = value
    def action(self):
        print(self.name)
        print(self.number)
        print(self.value)
a=Actor("f10",10,"dom")
a.system = "intel"
print(a.system)
