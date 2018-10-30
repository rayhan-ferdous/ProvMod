import sys
import fn_logged
from ProvModel import Module, Object

# this script's name
src = sys.argv[0]

# this scripts first input as command line argument
in1 = sys.argv[1]

# create a tool invocation

d1 = Object(in1)
m = fn_logged.REMOVESPACE(d1)
d2 = m.run()

# output to STDOUT
print d2.ref