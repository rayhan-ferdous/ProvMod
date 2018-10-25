# takes 2 arguments and sums them up
# arguments are passed as command line arguments
# invocation command : python Add_ProVerna.py %%in1%% %%in2%%

import sys
from Functions_logged import Add_logged
from lib.ProvModel import Object, File, Module

# getting command line arguments
script_name = sys.argv[0]

in1 = sys.argv[1]
in2 = sys.argv[2]

# packing necessary arguments
d1 = Object(in1)
d2 = Object(in2)

# initiating tool
m = Add_logged(d1, d2)

# executing tool and getting packed result
d3 = m.run()

# sending result value to stdout
result = str(d3.ref)
sys.stdout.write(result)