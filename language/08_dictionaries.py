# car = {
#     'brand': 'Ford',
#     'model': 'Mustang',
#     'year': 1964,
#     'year': 2020
# }

# print(car['year'])

# print(car.get('year'))

# print(len(car))

# ----------------------------------------

# car = {
#     'brand': 'Ford',
#     'model': 'Mustang',
#     'year': 2020
# }

# print(car.keys())

# print(car.values())

# print(car.items())

# for key, value in car.items():
#     print(key, value)

# if 'brand' in car:
#     print('\'brand\' key exists')

# ----------------------------------------

# car = {
#     'brand': 'Ford',
#     'model': 'Mustang',
#     'year': 2020
# }

# car['year'] = 2022
# print(car)

# car.update({'year': 2024, 'color': 'white'})
# print(car)

# ----------------------------------------

# car = {
#     'brand': 'Ford',
#     'model': 'Mustang',
#     'year': 2020
# }

# car.pop('brand')
# print(car)

# del car['year']
# print(car)

# ----------------------------------------

# car = {
#     'brand': 'Ford',
#     'model': 'Mustang',
#     'year': 2020
# }

# car.clear()
# print(car)

# ----------------------------------------

# foo = {
#     'a': 1,
#     'b': 2
# }
# bar = foo

# foo['a'] = 3

# print(foo)
# print(bar)

# ----------------------------------------

# foo = {
#     'a': 1,
#     'b': 2
# }
# bar = foo.copy()

# foo['a'] = 3

# print(foo)
# print(bar)

# ----------------------------------------

# foo = {
#     'a': 1,
#     'b': 2
# }

# foo.setdefault('b', 3)
# print(foo)

# foo.setdefault('c', 3)
# print(foo)
