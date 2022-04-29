# class Foo:
#     x = 5


# bar = Foo()
# print(bar.x)

# ----------------------------------------

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('initialized person')

    def hi(self):
        print('Hello, my name is {}!'.format(self.name))


foo = Person('John', 36)

print(foo.name)
print(foo.age)

foo.hi()

foo.name = 'Mike'

foo.hi()
