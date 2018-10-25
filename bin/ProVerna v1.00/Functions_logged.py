from Functions import Add
from lib.ProvModel import Object, Module

# takes 2 arguments and sums them up with ProvMod
# in1 : Object
# in2 : Object
# return Object
class Add_logged(Module):
    def body(self):
        # unpacking value only
        in1 = self.P[0].ref
        in2 = self.P[1].ref

        # applying raw function
        r = Add(in1, in2)

        # returning packed value
        return Object(r)