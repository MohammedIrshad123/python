# casting Probelms

# integer + integer = integer
a=10
b=10
c=a+b
print(c)

# string + string = string
a="20"
b="20"
c=a+b
print(c)

'''
# int + string = Type Error
a=20
b="20"
e=a+b
print(e)
'''

# int + string (convert into int) = int
a=10
b=int('10')
c=a+b
print(c)

#User input (while here input for a & b always string)
a=input()
b=input()
c=a+b
print(c)

# Casting in user input (while here input for a & b can be casted as int)
a=int(input())
b=int(input())
c=a+b
print(c)