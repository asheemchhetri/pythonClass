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