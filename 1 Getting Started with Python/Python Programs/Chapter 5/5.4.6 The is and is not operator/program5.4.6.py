# smallest value using 'is' and'is not' operator
smallest = None
print('Before')
for value in [3, 41, 9, 74, 15] :
    if smallest is None :
        smallest = value
    elif value < smallest :
        smallest = value
    print (smallest, value)

print('After', smallest)