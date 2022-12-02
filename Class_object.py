class list_parser: 
    count = 5                     # Class Variable/Static variable
    def __init__(self,L1):        # __init__ is a constructor used to accept data and not compulsory
        self.L1 = L1              # self is a pointer and it can be any name and used to assign data to instance/object variables

    def parser(self):
        if type(self.L1)==list:
            for num in self.L1:
                print(num)
            list_parser.count+=5

    def reverse(self):
        if type(self.L1)==list:
            return(self.L1[::-1])

Obj = list_parser([1,3,2,5,4])     # Obj is object of class list_parser
Obj2 = list_parser([100,300,200])
print(Obj.count)
Obj.parser()
Obj2.parser()
print(Obj.reverse())
print(Obj2.reverse())
print(Obj2.count)
print(list_parser.count)

Obj.count = 50    # Updating count value using object(instance variable)
Obj2.count = 60   

print(Obj.count)  # count value changed for object Obj
print(Obj2.count)
print(list_parser.count)  # count value not changed because it is tightly bound with class
list_parser.count = 70
print(list_parser.count)



class dict_parse:
    def __init__(self,D):
        self.D=D
    
    def key_Dict(self):  # show keys
        if type(self.D)==dict:  
            print(self.D.keys())
        else:
            print("It is not a dictionary")

    def Value_Dict(self):  # show values
        if type(self.D)==dict:
            print(self.D.values())
        else:
            print("It is not a dictionary")

    def Check_Dict(self):  # take I/P from user and get keys/value
        self.D = eval(input())
        self.key_Dict()
        self.Value_Dict()


    def insert_Dict(self,K1,V1): # insert key/value to dictionary
        if type(self.D)==dict:
            self.D[K1]=V1
            print(self.D)
        else:
            print("It is not a dictionary")


Dobj = dict_parse({'K1':123,'K2':'abc'})
print(Dobj.D)
Dobj.key_Dict()
Dobj.Value_Dict()
Dobj.insert_Dict('K3',30.44)
Dobj.Check_Dict()
