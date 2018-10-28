from ProvModel import Module, File, Object
import fn_raw


class start_logged(Module):
    def body(self):
        in1 = self.P[0].ref

        r = fn_raw.start_raw(in1)

        flow = Object(r)

        return flow

class cr_to_bed_logged(Module):
    def body(self):
        in1 = self.P[0].ref

        r = fn_raw.cr_to_csv_raw(in1)

        flow = Object(r)

        return flow

class count_logged(Module):
    def body(self):
        in1 = self.P[0].ref
        in2 = self.P[1].ref


        r = fn_raw.count_raw(in1, in2)
        flow = Object(r)

        return flow


class top_k_logged(Module):
    def body(self):
        in1 = self.P[0].ref

        r = fn_raw.top_k_raw(in1)
        flow = Object(r)

        return flow

class show_logged(Module):
    def body(self):
        in1 = self.P[0].ref

        r = fn_raw.show_raw(in1)

        flow = Object(r)

        return flow

class end_logged(Module):
    def body(self):
        in1 = self.P[0].ref

        r = fn_raw.end_raw(in1)
        flow = Object(r)

        return flow