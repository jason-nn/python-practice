class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def name(self):
        return ('{} {}'.format(self.first_name, self.last_name))

    def greeting(self):
        return ('Hi, I\'m {} {}'.format(self.first_name, self.last_name))


tanjiro = Person('Tanjiro', 'Kamado')
print(tanjiro.name())
print(tanjiro.greeting())


class Student(Person):
    def __init__(self, first_name, last_name, school):
        super().__init__(first_name, last_name)
        self.school = school

    def greeting(self):
        return super().greeting() + ' from {}'.format(self.school)


nezuko = Student('Zenitsu', 'Agatsuma', 'Kimetsu Academy')
print(nezuko.name())
print(nezuko.greeting())
