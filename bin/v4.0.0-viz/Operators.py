import json
import os

def jsonify(r):
    r = json.dumps(r)

    return r

def write_logic(in1):
    f = open('N.txt', 'w')

    f.write(str(in1))
    print 'value saved into file N.txt'