import sys
from ProvModel import Object, Module
import fn_logged

in1 = sys.argv[1]
in2 = sys.argv[2]

d1 = Object(in1)
d2 = Object(in2)

m = fn_logged.count_logged(d1, d2)

d3 = m.run()

sys.stdout.write(d3.ref)