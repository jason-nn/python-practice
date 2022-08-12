a = 200
b = 33

if a > b:
    print('a is greater than b')
elif a < b:
    print('a is less than b')
else:
    print('a is equal to b')

print(a) if a > b else print(b)

if a > b and a > 1000:
    print('a is greater than b and greater than 1000')

if a > b or b > a:
    print('a and b are not equal')

if 3 > 2:
    pass
