
'''
The purpose of this form is to act as a quick
reference into the world of python
there is not much more purpose than that
YAY!!

2/1/2015 Python ver: 3.4.2
'''

# *** THIS IS BASIC VARIABLE SYNTAX		1$
age = 15

# *** THIS IS A BAIS IF STATEMENT		1$
if age < 21:
    print("NO!")

# *** THIS BLOCK IS SHOWING THE IF ELIS	1$
# *
name = "Scotty - b"

if name is "Allie":
	print("Hewro")
elif name is "Scott":
	print("are you coding")
else:
	print("who are you")
	
# *
# ***

# *** THIS IS THE BASIC LIST SET UP AND FOR STATEMENT THAT LOOPS THROUGH A LIST		1$
# *
	
food = ['Meat', 'Milk', 'Cearal']

for f in food:
	print(f)
	#THIS PRINTS THE LENGTH OF THE ELEMENT
	print(len(f))

# *
# ***

#JUST A SPACER HERE
print('\n')
print('\n')

# *** THIS IS A STATEMENT THAT CYCLES THROUGH A LIST AND STOPS AT A CERTIAN VALUE 	1$
# *
for lf in food[:2]:
	print(lf)

# *
# ***

print('\n')

# *** THIS IS AN EXAMPLE OF A RANGE		1$
# *
num = 0
for y in range(10):
	num += 1
	print(num)
	#print(y)
print('\n')	

for z in range(10 , 18):
	print(z)
print('\n')

for w in range(10, 40, 5):
	print(w)
print('\n')
# *
# ***

# *** WHILE LOOPS					1$
# *
num = 3
while num < 50:
	num += 1
	if num % 10 == 0:
		print(num)
print('\n')
# *
# ***

# *** Break Statement Example		1$
# *
mNum = 20

for n in range(101):
	if n == mNum:
		print(n, 'This is the Magic Number')
		break		
# *
# ***
print('\n')
# *** Continue Statement EXAMPLE	1$
# *
number = [2, 5, 8, 4]
for y in range(10):
	if y in number:
		continue
	print(y)
	
# *
# ***
print('\n')
# *** Functions
# *
def bucky(btc):
	amount = btc * 217.22
	print(amount)
bucky(200)
# *
# ***
print('\n')
# *** Return value
# *
num = 5

def main():
	n = matth(num)
	if n == 25:
		print("The Return value was correct")
	else:
		print("The return value was: ", n)

def matth(v):
	n = v * 5
	return n
	
main()
# *
# ***
print('\n')
# ***
# *

# *
# ***





































