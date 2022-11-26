# Hold elements in key value fashion
# Key must be immutable element

D1 = {}
print("Initial length of list :",len(D1))

D2 = {'Name':'Abhi','Age':30,'Key1':[1,2,3],'Key2':(22,33,44),'Key3':{'ab',123},'Key4':{1:'HANA',2:'SQL'}}
print(D2)

# Insert elements to Dict
D2['Key5']=3.14
D2['Key6']=5+6j
print(D2)
print(len(D2))

# Update values in Dict
D2['Name']='Soni'
print(D2)

# Delete element from Dict
del D2['Key6']
del D2['Age']
print(D2)

# Access values from Dict
print(D2['Key4'][1])
print(list(D2['Key2'])[0])

print(D2.get('Name'))
print(D2.keys())
print(D2.values())
print(D2.items()) # returns individual key value pair in the form of tuple

# Compare dictionary 
dict3 = {'a' : 1, 'b' : 2, 'c' : 3}
dict4 = {'b' : 2, 'c' : 3, 'a' : 1}
print(dict3 == dict4)

dict3 = {'a' : 1, 'b' : 2, 'c' : 3}
dict4 = {'b' : 2, 'c' : 3, 'a' : 5}
print(dict3 == dict4)



D4= {'K1':123,'K2':'eret'}
print(D4)
D5= {'K3':5.4,'K4':[1,2,3]}
print(D5)
D4.update(D5)
print(D4)
