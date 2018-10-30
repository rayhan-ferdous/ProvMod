# input targetID

import sys
import pandas as pd


df = pd.read_csv(sys.argv[1])
t = sys.argv[2]


d = {}

for i, r in df.iterrows():
    k = r[t]



    if k not in d:
        d[k] = 1
    else:
        d[k] = d[k]+1

out = open(t + '_count_index.csv', 'w')
out.write('id,count\n')

for k in d:
    out.write(str(k) + ',' + str(d[k]) + '\n')

sys.stdout.write( t + '_count_index.csv' )
