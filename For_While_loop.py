
# For loop
for num in range(0,11): #range(0,11) --> [0,1,2,3,4,5,6,7,8,9,10]
    print(num)

for num in range(11):
    print(num)


for num in range(0,11,2): # with step=2 
    print(num)

for num in range(10,0,-1):
    print(num)


list1 =[30,'Abhi',30.5,[1,2,3]]
for num in list1:
    print(num)


for num in enumerate(list1): # returns elements in form of tuples of (index,value)
    print(num)


list2 = [12, 75, 150, 180, 145, 525, 50]
total = 0
for num in list2:
    total=total+num
print('Total from for loop : ',total)


# Break 
# Print first even number from list and exit
list3 = [1, 3, 5, 8, 10, 7, 11]
for num in list3:
    if(num%2==0):
        print('Even :',num)
        break


# Continue
# Print numbers from list greater than 10
list4 = [1, 12, 5, 8, 10, 7, 11]
for num in list4:
    if (num <= 10):
        continue
    print("Numbers >10 :",num)


for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=' ')    # end=  allow to print o/p in single row
    print('')


# While loop
counter=1
while counter<=11: # Either True or False
    print(counter)
    counter+=1


list2 = [12, 75, 150, 180, 145, 525, 50]
total=0
count=0
while count<len(list2):
    total=total+list2[count]
    count+=1
print("Total from while loop :",total)
