import sys
from ProvModel import Module, File, Object
import fn_logged
import psutil

in1 = sys.argv[1]


d1 = Object(in1)

m = fn_logged.end_logged(d1)
d2 = m.run()

sys.stdout.write(d2.ref)