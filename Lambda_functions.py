# Normal way
def Sqr1(x):
    return x**2
print("Squere :",Sqr1(3))

# Lambda function
# Calculate square of a given number
Sqr = lambda x : x**2 # syntax --> lambda <parameters> : <expression>
print("Square of no. :",Sqr(3))


# Find the max of two numbers
Max_num = lambda a,b : a if a>b else b if b>a else 'both are equal'
x= int(input("First No. :"))
y=int(input("Second No. :"))
print("Max no. :",Max_num(x,y)) 


# Map function --> will return n values if there are n values in list
# Calculate square of each item in list
L1 = [1,2,3,4,5]
Sqr = lambda x : x**2 
num = 3
L2 = list(map(Sqr,L1))
print("List of Square :",L2)


# Calculate the sum of 2 list elements
L1=[1,1,3,6,2]
L2=[3,4,1,6,7]

Sum_Num = lambda x,y : x+y
L3 =list(map(Sum_Num,L1,L2))
print(L3)


# Reduce function --> always return single value
# Calculate the sum of all elements of a list
import functools
L= [100,20,33,45,12]
sum_list = lambda a,b : a+b
result = functools.reduce(sum_list, L,100) # 100 is initial value and added to main result,it is optional if not given it is 0 by default 
print("Sum :",result)


# Filter function --> returns n or less than n values if there are n elements in list
# Filter even numbers from given list
L4 = [2,1,6,7,3,5,9,8]
Even_list = lambda x : x%2 == 0
result_list = list(filter(Even_list, L4))
print("Even list :",result_list)
