import sys
import time

millis = int(round(time.time() * 1000))

f = open('/home/aapon/taverna/time.csv', 'a')


f.write( str(millis) + '\n' )

sys.stdout.write(sys.argv[0])
