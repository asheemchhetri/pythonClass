# >>> Filter: We use filter to apply a function object on a iterative input, such a list, tuple, set, dictionary, etc.
# It returns a list of elements that is True where condition is met, and must be converted to iterable, usually list
number = [1, 2, 3, 4, 5, 6, 7, 8]

print(list(filter(lambda x: x%2 == 0, number)))
