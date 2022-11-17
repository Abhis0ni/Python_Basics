
# Declare Empty List
L2=[] 
print("Initial length of list :",len(L2))

L1=['Hello'] 
# Insert data to list
L1.append('Abhi') # Append always insert content in last of list
L1.append(123)
L1.append(32.56)
L1.append(3+5j)
L1.append(True)
L1.append([1,2,3])
print(L1)
print(type(L1))

L1.insert(3,'Ahhhaa')
print(L1)

# Update data in List
L1[2]='Soni'
print(L1)


# Delete content from List
L1.remove('Hello')
print(L1) # If element not present then gives error

L1.pop() # by default it remove content from last
print(L1)
L1.pop(2)
print(L1)


# How to check is list are equal to each other?
list1 = [1,"Abhi",20,"Hi"]
list2 = [1,"Abhi",20,"Hi"]
print("Lists are equal ?? ", list1 == list2)

list1 = [1,"Abhi",20,"Hi"]
list2 = [1,"Abhi","Hi",20]
print("Lists are equal ?? ", list1 == list2)

#Both Extend function and Concatenate List returns same O/P
L3 = [1,'abc',32.5]
L4 = [2,'ABC']
L3.extend(L4)
print(L3)
L3 = [1,'abc',32.5]
L4 = [2,'ABC']
L5=L3+L4
print(L5)

# List slicing - works same as string
L6=['hi',2022,32.8,'SAP']
print(L6[0:2])
print(L6[::-1]) #Reverse whole list
print(L6[-1::-1]) #Reverse whole list
L6.reverse() #Reverse whole list
print(L6)


# Repeat List content 3 times
print(L6*3)

# Replace a char in content of list
L6[3]=L6[3].replace('S','M')
print(L6)

#Checking content in List
print('MAP' in L6)

#count the occurance of any content
print(L6.count('hi'))
