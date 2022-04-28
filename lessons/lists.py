# a = [1, 2, 3, 1, 1, 'a', 'b']

# print(a)
# print(len(a))

# ----------------------------------------

# a = [1, 2, 3, 1, 1, 'a', 'b']

# print(a[0])
# print(a[-1])

# print(a[2:5])
# print(a[:5])
# print(a[2:])

# if 3 in a:
#     print('3 is in this list')

# ----------------------------------------

# a = [1, 2, 3, 1, 1, 'a', 'b']

# a[0] = 'jason'
# print(a)

# a[1:3] = ['c', 'd']
# print(a)

# a.insert(3, 'e')
# print(a)

# a.append('z')
# print(a)

# b = ['x', 'y']
# a.extend(b)
# print(a)

# ----------------------------------------

# a = [1, 2, 3, 1, 1, 'a', 'b']

# a.remove('a')
# print(a)

# a.pop(1)
# print(a)

# a.pop()
# print(a)

# del a[-1]
# print(a)

# a.clear()
# print(a)

# ----------------------------------------

# fruits = ['apple', 'banana', 'cherry']

# for i in fruits:
#     print(i)

# for i in range(len(fruits)):
#     print(i, fruits[i])

# i = 0
# while i < len(fruits):
#     print(fruits[i])
#     i += 1

# [print(i) for i in fruits]

# ----------------------------------------

# fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango']

# new_list = []
# for fruit in fruits:
#     if 'a' in fruit:
#         new_list.append(fruit)
# print(new_list)

# newer_list = [fruit for fruit in fruits if 'a' in fruit]
# print(newer_list)

# no_apples = [fruit for fruit in fruits if fruit != 'apple']
# print(no_apples)

# ----------------------------------------

# print([x for x in range(10) if x % 2 == 0])

# print([x + 1 for x in range(10) if x % 2 == 0])

# print(['fizz' + str(x) if x % 3 == 0 else 'buzz' + str(x) for x in range(10) if x %
#       3 == 0 or x % 5 == 0])
