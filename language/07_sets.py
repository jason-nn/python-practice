# # unordered and does not allow duplicates

# set = {'a', 'b', 'c', 'a'}

# print(set)

# ----------------------------------------

# set = {'a', 'b', 'c'}

# set.add('d')

# print(set)

# ----------------------------------------

# set = {'a', 'b', 'c'}

# set.update({'d', 'e'})

# print(set)

# ----------------------------------------

# set = {'a', 'b', 'c'}

# # will raise an error if item to remove does not exist

# set.remove('c')

# print(set)

# # will not raise an error if item to remove does not exist

# set.discard('b')

# print(set)

# ----------------------------------------

# set = {'a', 'b', 'c'}

# set.clear()

# print(set)

# ----------------------------------------

# foo = {1, 2, 3, 4}
# bar = {3, 4, 5, 6}

# foobar = foo.union(bar)

# print(foobar)

# ----------------------------------------

# foo = {1, 2, 3, 4}
# bar = {3, 4, 5, 6}

# foobar = foo.intersection(bar)

# print(foobar)

# ----------------------------------------

# foo = {1, 2, 3, 4}
# bar = {3, 4, 5, 6}

# foobar = foo.symmetric_difference(bar)

# print(foobar)

# ----------------------------------------

# foo = {1, 2, 3, 4}
# bar = {3, 4, 5, 6}

# foobar = foo.difference(bar)

# print(foobar)

# ----------------------------------------

# foo = {1, 2, 3, 4}
# bar = {3, 4, 5, 6}

# foo.update(bar)

# print(foo)

# ----------------------------------------

# foo = {1, 2, 3, 4}
# bar = {3, 4, 5, 6}

# foo.intersection_update(bar)

# print(foo)

# ----------------------------------------

# foo = {1, 2, 3, 4}
# bar = {3, 4, 5, 6}

# foo.symmetric_difference_update(bar)

# print(foo)

# ----------------------------------------

# foo = {1, 2, 3, 4}
# bar = {3, 4, 5, 6}

# foo.difference_update(bar)

# print(foo)
