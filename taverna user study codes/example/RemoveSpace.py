import sys

# this script's name
src = sys.argv[0]

# this scripts first input as command line argument
in1 = sys.argv[1]

f = open(in1)

out = open('noSpace.txt', 'w')

for line in f:
    for word in line:
        for letter in word:
            if letter == ' ' :
                pass
            else:
                out.write(letter)

print out.name