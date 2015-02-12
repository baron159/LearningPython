__author__ = 'Scott'

fw = open('sample.txt', 'w')
fw.write('Write this into the file\n')
fw.write('Scott wrote this line too\n')
fw.close()

fr = open('sample.txt', 'r')
text = fr.read()
print(text)
fr.close()

print('\n')

# TODO write codte here that will print out only the first line of text in the file
print(text)