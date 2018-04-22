import psutil
from py2neo import Graph
import time
#import Queries

query1 = 'match(n:Module) return n'


graph  = Graph(password = 'password')

query = query1

data = graph.run(query)

f = open('data/viz2.tsv', 'w')

f.write('time\tname\tstatus\tcpu\tmemory\tduration\n')
f.write('123\tdefault\tsuccess\t0\t0\t0')

for d in data:
    #print d['n']['NAME'], d['n']['error'], d['n']['cpu'], d['n']['memory'], d['n']['duration']

    name = d['n']['NAME']

    status = 'error'
    if d['n']['error'] == 'Null':
        status = 'success'

    cpu = '0'
    if str(d['n']['cpu']) != 'None':
        cpu = str(d['n']['cpu'])

    memory = '0'
    if str(d['n']['memory']) != 'None':
        memory = str(d['n']['memory'])

    duration = '0'
    if str(d['n']['duration']) != 'None':
        duration = str(d['n']['duration'])

    time = d['n']['time']

    print name, status, cpu, memory, duration

    f.write(time + '\t' + name + '\t' + status + '\t' + cpu + '\t' + memory + '\t' + duration + '\n')


f.close()

print psutil.virtual_memory()[3]