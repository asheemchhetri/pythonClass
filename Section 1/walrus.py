'''
Writing a simple example to use the new walrus operator, introduced in Python 3.8
It helps to perform assignment to a variable, while we are using a condition as part fo different function.
'''

### Wihout Walrus
num = input("Please enter a number: ")
while (num.isdigit()):
    print(num)
    num = input("Please enter a number: ")

### With Walrus
while(num := input("Please enter a number: ")).isdigit():
    print(num)
