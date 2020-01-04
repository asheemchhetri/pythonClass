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