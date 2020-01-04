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
