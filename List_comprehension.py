
# Normal way
l=[]
for x in range(1,11):
    l.append(x)
print(l)

# list comprehension
l1 = [x for x in range(1,11)] 
print(l1)


# Get all even elements from list
l=[1,4,2,5,8,3,5,6]
result_list = [x for x in l if x%2==0] # syntax --> [<expression> <for statement> <if conditions>]
print("Even list :",result_list)

# Get the square of all elements in list
l=[1,4,2,5,8,3,5,6]
Sqr_list = [x**2 for x in l]
print("Square list :",Sqr_list)


# Put all negative numbers after positive numbers from given list
list_a = [9,-1,2,-5,1,10,-6]
result = [ x for x in list_a if x>0 ] + [ x for x in list_a if x<0 ]
print (result)
