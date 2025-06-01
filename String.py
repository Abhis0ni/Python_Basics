# Working with string datatype

a='abcdefghijk'
print(a[0])
print(a[-1])
print(a[-4])
print(a[0:10])
print(a[0:10:2]) 
# 0 is start index,10 is end index
# end index is always exclusive
# 2 is step and by default it is 1
print(a[-2:-14:-2])
print(a[::]) # by default it will give whole string
print(a[::-1]) # Gives reverse of string
print(a[-8:3:])
# below both will give same output
print(a[-2:3:-1])
print(a[-2:-8:-1])

b='I love Python'
print(b.split()) # It will result into a List
print(b.split('o'))

c='AbhIshek'
print(c.swapcase())
print(c.title())
print(c.capitalize()) # title and capitalize will give exact same O/P

d1='Abhi'
d2='Soni'
print(d1.join(d2))
print(d1+' '+d2)

# Update character in string (String is immutable)
s='Python'
s=s.replace('y', 'o')
print(s)


# how to write multiline string
str4 = '''Abhishek is
going
to attend 
the seminar
'''
print(str4)
