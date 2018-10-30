from ProvModel import Object, Module

# raw functions
def fn_add(a, b):
    return a+b

def fn_mul(a, b):
    return a*b

def fn_double(a):
    return a*2

# creating modules
class Add(Module):
    # overwrite the body
    def body(self):

        #unpack values from input dataflows
        in1 = self.P[0].ref
        in2 = self.P[1].ref

        # apply function
        res = fn_add(in1, in2)

        # pack the values again
        flow = Object(res)

        # return output dataflow
        return flow

class Mul(Module):
    # overwrite the body
    def body(self):

        #unpack values from input dataflows
        in1 = self.P[0].ref
        in2 = self.P[1].ref

        # apply function
        res = fn_mul(in1, in2)

        # pack the values again
        flow = Object(res)

        # return output dataflow
        return flow

class Double(Module):
    # overwrite the body
    def body(self):

        #unpack values from input dataflows
        in1 = self.P[0].ref

        # apply function
        res = fn_double(in1)

        # pack the values again
        flow = Object(res)

        # return output dataflow
        return flow


d1 = Object(111)
d2 = Object(222)

d3 = Add(d1, d2).run()

d4 = Object(1000)

d5 = Mul(d3, d4).run()

print d5.ref