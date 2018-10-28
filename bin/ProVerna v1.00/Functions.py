# takes 2 arguments and sums them up
# a : int
# b : int
# return : int
def Add(in1, in2):
    a = int(in1)
    b = int(in2)
    sum = a + b

    return sum

def Sub(in1, in2):
    return int(in1)-int(in2)

def Mul(in1, in2):
    return in1*in2

def Div(in1, in2):
    try:
        return in1/in2
    except Exception as e:
        print e
