# Inbuilt functions
L1=[12,24,13,5,10]
print("Max :",max(L1))
print("Min :",min(L1))
print("Sum :",sum(L1))


def Welcome(): # Defining function
    print("Welcome to Python!!")
Welcome() # Calling function


def bot_message():
    print("Message from Bot using Print!!")
    return "Message from Bot !!"
bot_message()
print( bot_message())


def Avg(a,b):
    c=(a+b)/2
    return c
print("Average of number is ",Avg(3,6))


def square_and_cube(n):
    sqr = n*n
    cube = n*n*n
    return sqr,cube
num = 3
sqr_ans , cube_ans = square_and_cube(num)
print(square_and_cube(num)) # (9,27)
print("Square of ",num," is : ",sqr_ans)
print("Cube of ",num," is : ",cube_ans)


# Creating optional parameters
def Multiply(x,y=2,z=3):
    result = x*y*z
    return result
R1 = Multiply(int(input("Please enter value :")))
print(R1)
R2 = Multiply(int(input("Please enter 1st value :")),int(input("Please enter 2nd value :")))
print(R2)
R3 = Multiply(int(input("Please enter 1st value :")),int(input("Please enter 2nd value :")),int(input("Please enter 3rd value :")))
print(R3)


# Non-Key Valued arguments
def non_keyed_argv(*argv):
    for val in argv:
        print(val)
non_keyed_argv(12,'Abhi',30.5,'Soni',23,2,4,34)


# Key Value type of arguments in Python
def ex_kwargs(**kwargs):
    for key,val in kwargs.items():
        print('key is :',key,', Value is :',val)
ex_kwargs(host='192.168.20.12',port=3030,pwd='XYZ123')


