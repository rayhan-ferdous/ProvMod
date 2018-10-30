import sys
from ProvModel import Module, Object
import fn_logged
import psutil
import os

in1 = sys.argv[1]

d1 = Object(in1)
m = fn_logged.cr_to_bed_logged(d1)
d2 = m.run()

sys.stdout.write(d2.ref)

process = psutil.Process(os.getpid())
ram = process.memory_info().rss

mem = open('memory.csv', 'a')
mem.write(str(ram) + ',')
