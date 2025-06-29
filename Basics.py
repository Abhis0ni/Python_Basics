# Checking datatype
x= 3.99
X= 10
y= True
z= "SQL"
# or we can declare variables like x,X,y,z= 3.99,10,True,"SQL"
print(type(x))
print(type(X))
print(type(y))
print(type(z))   # both "SQL" or 'SQL' will return string
print(type(5+6j))
# True=1/False=0
print(True+True)
print(y+y)

# Prompt input from user
Num1 = int(input("Please enter No.1: "))
Num2 = int(input("Please enter No.2: "))
FName = input("Please enter first name: ")
LName = input("Please enter last name: ")
print("Sum =",Num1+Num2)
print("Float Division =",Num1/Num2)
print("Integer Division =",Num1//Num2)
print("Mod =",Num1%Num2)
print("Power =",Num1**Num2)
print("Concatenate Name =",FName+" "+LName)
print("Repeat Name 3 times=",FName*3)
Num2+=7
print("Num2 +=7 ",Num2)
print("Is Num1 = Num2 ? ", Num1 == Num2)

# logical operators in Python ( Logical check will happen for expression result)
# and -> Returns true if both statements are true 
# or -> Returns true if one of statements are true
# not -> Reverse the result, returns false if the result is true

print("Is Num1>10 and Num2<10 ? " , Num1>10 and Num2<10)
print("Is Num1>20 or Num2<10 ? " , Num1>10 or Num2<10)
print("not(Num1>20 and Num2<10) ? " , not(Num1>10 and Num2<10)) 

# Taking multiple inputs using Split function
x, y = input("Enter two values: ").split()
print("Number of boys: ", x)
print("Number of girls: ", y)

# IF else conditions
Marks = int(input("Enter Marks :"))
if Marks > 90:
    Print("A+")
elif Marks<90 and Marks>70:
    print("A")
elif Marks<70 and Marks>50:
    print("B+")
else: 
    print("B")
