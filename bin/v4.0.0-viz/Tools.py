from ProvModel import Object, File, Document, Module
from ProvModel import err
from Operators import jsonify
import time
from random import randint


class FastQC(Module):
    def body(self):
        import subprocess


        cmd = 'FastQC/./fastqc ' + str(self.P[0].ref.name)
        returned_value = subprocess.call(cmd, shell=True)

        r1 = File(open(str(self.P[0].ref.name)[:-3] + '_fastqc.html'))
        r2 = File(open(str(self.P[0].ref.name)[:-3] + '_fastqc.zip'))

        #print r1, r2

        return r1, r2

class DNALetterCount(Module):
    def body(self):


        filename = self.P[0].ref.name

        n = 0.0
        a = 0
        t = 0
        c = 0
        g = 0

        with open(filename) as f:
            for line in f:
                n = float(len(line))

                #print line

                for letter in line:
                    if letter == 'A':
                        a = a+1
                    elif letter == 'T':
                        t = t+1
                    elif letter == 'C':
                        c = c+1
                    elif letter == 'G':
                        g = g+1



        r1 = ('a', a/n)
        r2 = ('c', t/n)
        r3 = ('t', c/n)
        r4 = ('g', g/n)
        r5 = ('Len', n)

        return Object(r1), Object(r2), Object(r3), Object(r4), Object(r5)

class Entropy(Module):
    def body(self):


        import math

        aprob = self.P[0].ref[1]
        cprob = self.P[1].ref[1]
        tprob = self.P[2].ref[1]
        gprob = self.P[3].ref[1]



        H = aprob*math.log(aprob, 4) + cprob*math.log(cprob, 4) + tprob*math.log(tprob, 4) + gprob*math.log(gprob, 4)

        #print H

        return Object(H)

class MaxMinProb(Module):
    def body(self):

        b1 = self.P[0].ref
        b2 = self.P[1].ref
        b3 = self.P[2].ref
        b4 = self.P[3].ref

        data = (b1, b2, b3, b4)

        #print data
        maxval = 0
        maxname = ''

        minval = 1
        minname = ''

        for i in data:

            if i[1] >= maxval:
                maxval = i[1]
                maxname = i[0]

            if i[1] <= minval:
                minval = i[1]
                minname = i[0]

        return Object((maxname, maxval)), Object((minname, minval))
