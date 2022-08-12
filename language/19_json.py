import json

foo = {
    'name': 'John',
    'age': 30,
    'married': True,
    'divorced': False,
    'children': ('Ann', 'Billy'),
    'pets': None,
    'cars': [
      {'model': 'BMW 230', 'mpg': 27.5},
        {'model': 'Ford Edge', 'mpg': 24.1}
    ]
}

bar = json.dumps(foo, indent=2)

print(type(bar))
print(bar)

bar = json.dumps(foo, indent=2, sort_keys=True)

print(type(bar))
print(bar)
