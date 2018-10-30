from ProvModel import Module, Object
from py2neo import Graph
import time
from py2neo import Graph

graph  = Graph(password = 'password')

class T(Module):
    def body(self):
        in1 = self.P[0].ref

        print in1 + ' as in'

        return Object(in1 + ' as out')

Qres = open('query eval.csv', 'a')
# millis = int(round(time.time() * 1000))


for i in range(0, 5000):
    d1 = Object(str(i))

    m = T(d1)
    d2 = m.run()

    t0 = int(round(time.time() * 1000))
    q1 = 'match(n) return n'
    d = graph.run(q1)
    t1 = int(round(time.time() * 1000))
    Qres.write(str(t1-t0) + ',')

    t0 = int(round(time.time() * 1000))
    q2 = 'match(n:Object) where n.VALUE = \'' + str(i) + '\' return n'
    d = graph.run(q2)
    t1 = int(round(time.time() * 1000))
    Qres.write(str(t1-t0) + ',')

    t0 = int(round(time.time() * 1000))
    q3 = 'match(n:Object) return n.VALUE order by n.time'
    d = graph.run(q3)
    t1 = int(round(time.time() * 1000))
    Qres.write(str(t1-t0) + ',')

    t0 = int(round(time.time() * 1000))
    q4 = 'match(n:Object) return n.cpu, n.memory'
    d = graph.run(q4)
    t1 = int(round(time.time() * 1000))
    Qres.write(str(t1-t0) + '\n')





    print d2.ref
