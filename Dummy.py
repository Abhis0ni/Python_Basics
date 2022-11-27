
# Declare Empty Tuple (Immutable)
T2=(1213,'werwer') 
print("Initial length of tuple :",len(T2))

T1=(123,'werre',23.32)
print(T1+T2)


# How to check is tuple are equal to each other?
T3 = (1,"Abhi",20,"Hi")
T4 = (1,"Abhi",20,"Hi")
print("Tuples are equal ?? ", T3 == T4)

T3 = (1,"Abhi",20,"Hi")
T4 = (1,"Abhi","Hi",20)
print("Tuples are equal ?? ", T3 == T4)


# Tuple slicing - works same as string
T6=('hi',2022,32.8,'SAP')
print(T6[0:2])
print(T6[::-1]) #Reverse whole tuple
print(T6[-1::-1]) #Reverse whole tuple
# Tuple does't support T6.reverse()
print(T6)


# Repeat Tuple content 3 times
print(T6*3)


#Checking content in Tuple
print('SAP' in T6)

#count the occurance of any content
print(T6.count('hi'))

T5=([12,34,45,67],'Hello',32.45)
print(T5)
T5[0][2]='Soni'
print(T5)

#Convert Tuple to List or vice versa
L1=list(T5)
print(L1)
