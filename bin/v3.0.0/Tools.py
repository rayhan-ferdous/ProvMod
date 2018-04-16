from ProvModel import Object, File, Document, Module
from ProvModel import err
from Operators import jsonify

class Add(Module):
    def body(self):
        a = self.P[0].ref
        b = self.P[1].ref

        r = a+b

        return Object(r)

class Sub(Module):
    def body(self):
        a = self.P[0].ref
        b = self.P[1].ref

        r = a-b

        return Object(r)

class Mul(Module):
    def body(self):
        a = self.P[0].ref
        b = self.P[1].ref

        r = a*b

        return Object(r)

class Div(Module):
    def body(self):
        a = self.P[0].ref
        b = self.P[1].ref

        import numpy
        r = numpy.nan

        try:
            r = a/b
        except Exception as e:
            print e
            err.error("\"div-0-err\"")

        return Object(r)

class TensorAdd(Module):
    def body(self):
        a = self.P[0].ref
        b = self.P[1].ref

        import numpy

        r = numpy.add(a, b)

        return Object(r)

class TensorSub(Module):
    def body(self):
        a = self.P[0].ref
        b = self.P[1].ref

        import numpy

        r = numpy.subtract(a, b)

        return Object(r)

class TensorMul(Module):
    def body(self):
        a = self.P[0].ref
        b = self.P[1].ref

        import numpy

        r = numpy.matmul(a, b)

        return Object(r)

