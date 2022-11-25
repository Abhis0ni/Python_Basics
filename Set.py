# Hold unique elements only
# Hold immutable collections so don't hold List,Set
# Set is unordered selection so don't support indexing,Slicing

s = {}
print(type(s)) # returns Dictionary
s1 = {123,30.5,'Abhi'}
print(type(s1)) # returns Set
set1 = set()
print(type(set1)) # returns Set
t = ('qwe')
print(type(t)) # returns string
t1 = ()
print(type(t1)) # returns tuple
t2 = ('qwe',123,30.5)
print(type(t2)) # returns tuple


S2 = {123,'Soni',30.6,(123,456,'abc'),565,(123,456,'abc')}
print(S2)

# Insert data to set
S2.add('Abhi') # Append always insert content in last of set
S2.add(123)
S2.add(32.56)
S2.add(3+5j)
S2.add(True)
print(S2)


tmp = {2,3,4,5,2,3,4,5,2,3}
S2.update(tmp)
print('Updated :',S2)



# Delete content from Set
S2.remove(565)
print(S2) # If element not present then gives error
S2.discard(30.6)
print(S2)
S2.pop() # by default it remove First content from Set
print(S2)



# How to check is set are equal to each other?
S3 = {1,"Abhi",20,"Hi"}
S4 = {1,"Abhi",20,"Hi"}
print("Sets are equal ?? ", S3 == S4)

S3 = {1,"Abhi",20,"Hi"}
S4 = {1,"Abhi","Hi",20}
print("Sets are equal ?? ", S3 == S4)



#Checking content in Set
print('Hi' in S3)


# Convert List to Set
List1 = [1,2,3,4,1,2,3,4,5,6,7,8,1]
set2 = set(List1)
print(set2)

# Convert Set to List
List1 = [1,2,3,4,1,2,3,4,5,6,7,8,1]
List5 = list((set(List1)))
print(List5)
print(List5[-1])

# Set operations
set_a = {1,2,3,4,5,6}
set_b = {3,6,8,9,10}

# union operation
print(set_a | set_b)

# intersection operation
print(set_a & set_b)

# A - B ? 
# B - A ?
# Difference in Sets
print(set_a - set_b)
print(set_b - set_a)


# clear set
print(S2)
S2.clear()  # will delete all items in a set
print(S2)  
