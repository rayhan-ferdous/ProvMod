from ProvModel import Module, Object

class T(Module):
    def body(self):
        in1 = self.P[0].ref

        print in1 + ' as in'

        return Object(in1 + ' as out')

d1 = Object('INSTR')

m = T(d1)
d2 = m.run()

print d2.ref