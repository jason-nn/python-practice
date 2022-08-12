# foo = 'banana'

# iterator = iter(foo)

# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

# ----------------------------------------

# class OneToTen:
#     def __iter__(self):
#         self.current = 1
#         return self

#     def __next__(self):
#         if self.current <= 10:
#             current = self.current
#             self.current += 1
#             return current
#         else:
#             raise StopIteration


# one_to_ten = OneToTen()

# iterator = iter(one_to_ten)

# for num in one_to_ten:
#     print(num)
