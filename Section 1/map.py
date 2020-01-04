number = [1, 2, 3, 4, 5, 6, 7, 8]
# >>> Map: We use map to apply a function object on a iterative input, such a list, tuple, set, dictionary, etc.
# It return a MAP object, that should be converted to iterable, usually list
print(list(map(lambda x: x*10, number)))

# Write a map with lambda function which adds 5 to a number if an item is <= 5 or multiply by 10, if > 5