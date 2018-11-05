import sys
from ProvModel import Module, Object
# create the logic function
def removespace(in1):
    # taking input filename as parameter
    f = open(in1)
    # function logic
    out = open('noSpace.txt', 'w')
    for line in f:
        for word in line:
            for letter in word:
                if letter == ' ':
                    pass
                else:
                    out.write(letter)
    # return output filename
    return out.name

# wrap the logic function with ProvMod
class REMOVESPACE(Module):
    def body(self):
        #unpack input
        in1 = self.P[0].ref
        #apply logic
        res = removespace(in1)
        # pack value into Object
        flow = Object(res)
        #return Object
        return flow

# this script's name as cmd line argument
src = sys.argv[0]
# this scripts first input as command line argument
in1 = sys.argv[1]
# create a tool invocation
# input dataflow
d1 = Object(in1)
# tool initiation *** *** ***
m = REMOVESPACE(d1)
# output dataflow
d2 = m.run()
# output to STDOUT
print d2.ref