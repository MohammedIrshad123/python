# Find even number from the list or array

# traditonal Method
even=[]
for i in range(1,100):
    if i%2==0: 
        print( "even number")
        even.append(i)
print (even)         

# Using list comprehensions with generator expression
even_number=(num for num in range(1,10) if num % 2==0)
print (list(even_number))


# Using list comprehensions with generator expression
even_number=(num for num in range(1,10) if num % 2==0)
for i in even_number:
    print (i)

