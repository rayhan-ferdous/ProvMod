from ProvModel import Object, Module
import fn_raw

class REMOVESPACE(Module):
    def body(self):

        #unpack input
        in1 = self.P[0].ref

        #apply logic
        res = fn_raw.removespace(in1)

        # pack value into Object
        flow = Object(res)

        #return Object
        return flow


