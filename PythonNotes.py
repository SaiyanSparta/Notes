# Input
f = open("file.txt", 'r')
f.readline() # Leaves '\n' at the end, slice [:-1] to remove

with open("file.txt", 'r') as f: # Automatically closes file
	f.readline()

# Output
name = "Tyler", ID = 1234
print("{0} has an ID number of {1}".format(name, ID))
# For printing doubles with certain precisions
print("{0.2f}".format(3.1415)) # 3.14
print("{0.3f}".format(2.0)) # 2.000

#List Methods
l = [1, 2, 3, 4, 5, 4, 3]
m = list('applebottomjeans') # strings are lists!
n = list(set(m)) # Removes duplicates
# Output: ['o', 'j', 's', 't', 'b', 'p', 'm', 'l', 'n', 'a', 'e']
l = [1, 2, 3, 4, 5]
l += [6, 7, 8] # Result: [1, 2, 3, 4, 5, 6, 7, 8]
l.append([6, 7, 8]) # Result: [1, 2, 3, 4, 5, [6, 7, 8]]
# Warning: Make sure to use .append() when adding strings

l = 'Bob,Steve,Ann,Paula,Chris'.split(',') # Splits at the char
# Result: ['Bob', 'Steve', 'Ann', 'Paula', 'Chris']
"-".join(l) # Joins with provided char
# Result: 'Bob-Steve-Ann-Paula-Chris'

# Numerical Things
s = float("3.14159265") # Casting decimal strings to decimals

# Doing Character Arithmetics
c = chr(ord('D') - ord('A'))

#Permutations
from itertools import permutations
list(permutations(range(2))) # [(0, 1), (1, 0)]
list(permutations([3, 1, 4]))
