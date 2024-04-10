# Operators: +, -, *, /


# remainder %
print(24 % 5)

# exponents **
print(2 ** 3)
print(2 ** 4)
print(2 ** 5)

meaning = 42
meaning += 1 # increment addition
print(meaning)

meaning -= 1 # increment subtraction
print(meaning)

meaning *= 10 # increment multiplication
print(meaning)

meaning /= 10 # increment division
print(meaning)

round(meaning) # removes decimal point
print(round(meaning))

# adding strings
name = 'Dave ' + 'Gray'
print(name)

# comparisons
print(42 == 41) # prints false (boolean)
print(42 != 42) # prints false
print(43 != 42) # prints true

print(10 >=10) # prints true

x = True
y = False
z = True

print(not x) # prints false
print(not y) # prints true
print(not z) #prints false
print(x and y) # prints false, one value is false so the value is false (like multiplication and negatives)
print(x and z) # prints true because both are true
print(x or y) # prints true because at least one is true
print(y or z)

#################################################################
meaning = 42
print('')
if meaning > 43:
    print('Right on!')
else:
    print('You\'re not asking the right question')

# ternary operator
print('Right on!') if meaning > 10 else print('Not today')