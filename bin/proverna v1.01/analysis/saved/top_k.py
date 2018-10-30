# input

import sys
import pandas as pd


df = pd.read_csv(sys.argv[1])

srt = df.sort_values('count', ascending=False).head(10)

out = open('top_10_' + sys.argv[1][:-4] + '.csv', 'w')

srt.to_csv(out)

sys.stdout.write( 'top_10_' + sys.argv[1][:-4] + '.csv' )
