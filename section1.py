'''
Lambdas: lambda <variables>: <expression body>
Map: map(function, iterative data)
Filter: filter(function, iterative data)
Zip: zip(*iterables)
'''
# Lambda is more of an anonymous function, that can take any number of argument, but has only 1 expression. They are used only for a short period of time, and we do not want to define a function.
add_two_num = lambda x, y: x+y
print(add_two_num(5,4))

# lambda with if/else
func1 = lambda x: "Number is GREATER than 10" if x > 10 else "Number is LESS than 10"
print(func1(11))
print(func1(6))

number = [1, 2, 3, 4, 5, 6, 7, 8]
# >>> Map: We use map to apply a function object on a iterative input, such a list, tuple, set, dictionary, etc.
# It return a MAP object, that should be converted to iterable, usually list
print(list(map(lambda x: x*10, number)))

# Write a mp with lambda function which adds 5 to a number if an item is <= 5 or multiply by 10, if > 5



# >>> Filter: We use filter to apply a function object on a iterative input, such a list, tuple, set, dictionary, etc.
# It returns a list of elements that is True where condition is met, and must be converted to iterable, usually list
print(list(filter(lambda x: x%2 == 0, number)))

# >>> Zip: We use zip to combine multiple iterables into a single iterator, which is very helpful when we iterate through in a loop by expansion.
# Returns a list of tuple
# Note: Iterators can only be use ONCE, to save memory by only generating the iterators as we need them, rahter storing them in memory
country = ['India', 'USA', 'China', 'Japan']
gdp = ['$2.72 trillion', '$20.49 trillion', '$13.41 trillion', '$4.97 trillion']

data = zip(country, gdp)
# print(list(data))

for name, nominal in data:
    print('{} has a nominal GDP of {}'.format(name, nominal))

# How to unzip a sequence
# To use the above zipped data, we need to comment out the for loop, as after for loop the iterable is cleared out and unzip command will get 0 values to unpack while it is expecting 2
# country_unzipped, gdp_unzipped = zip(*data)
# print(country_unzipped)
# print(gdp_unzipped)

# String slicing, we use [start_index :  end_index]. One must note that the end_index is not inclusive.
# Another form is skipping a index >> [start_index : end_index : jump]
# If start_index is blank, then it takes from beginning
# If end_index is blank, then it goes to all the way to the end
name = "Elon Musk"
print(name[:])
# Print First name
print(name[:4])
# Print Last Name
print(name[5:])
# Print Last name, using reverse slicing
print(name[-4:])
# Skip 1 letter
print(name[0::2])
# How will you reverse his name?
print(name[::])

# ---------------------
import numpy as np
arr = np.arange(16).reshape((2, 2, 4))
print (arr)