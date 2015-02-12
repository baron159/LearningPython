__author__ = 'Scott'

# This is an example of Dictanrys similar to Hash tables in java

gameDic = {1: "Civ 5", 2: "LOL", 3: "DL", 4: "Halo", 5: "Evolve"}

# This will only return one element 2nd
print(gameDic.get(2))
print('\n')

for k, v in gameDic.items():
    print(k, v)
