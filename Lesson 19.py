__author__ = 'Scott Baron'

# this is an example for set in Python

numSet = {9, 5, 7, 10, 8, 6, 5, 74, 10, 8}
numList = [9, 5, 7, 10, 8, 6, 5, 74, 10, 8]


# Set can cantain only unique entries, this is testing the if a repeat entry is counted in the overall size of the set
n = 0
for y in numSet:
    n += 1
print(n)

n = 0
for y in numList:
    n += 1
print('\n', n)

# Conclusion - repeated items are not included in the overall size of a Set
