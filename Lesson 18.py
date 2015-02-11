__author__ = 'Scott'

# This is about unpacking Arguments

def health_calculator(age, apples, cigs):
    answer = (100 - age) + (apples * 3.5) - (cigs * 2)
    print(answer)
    return answer

bucky_data = [27, 20, 0]
scott_data = [20, 25, 2]

# This is the unpacking of an arg vs conventional methods
buck = health_calculator(bucky_data[0], bucky_data[1], bucky_data[2])
scott = health_calculator(*scott_data)

if scott > buck:
    print('Scotts Score is better')
else:
    print('Buckys Score is better')