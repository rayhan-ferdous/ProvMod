'''run simulation'''

from ProvModel import Object, File, Module
import Tools
from random import randint
import time

fq0 = File(open('gene/fq0.fq'))
fq1 = File(open('gene/fq1.bed'))
fq2 = File(open('gene/fq2.fa'))
fq3 = File(open('gene/fq3.fastq'))
fq4 = File(open('gene/fq4.fastq'))

dna0 = File(open('gene/dna0.txt'))
dna1 = File(open('gene/dna1.txt'))
dna2 = File(open('gene/dna2.txt'))
dna3 = File(open('gene/dna3.txt'))

fqset = [fq0, fq1, fq2, fq3, fq4]
dnaset = [dna0, dna1, dna2, dna3]



m1 = Tools.DNALetterCount(dnaset[0])
a, c, t, g, n = m1.run()

m2 = Tools.Entropy(a, c, t, g)
ent = m2.run()

m3 = Tools.MaxMinProb(a, c, t, g)
maxbase, minbase = m3.run()


while True:

    time.sleep(randint(1, 9))

    print 'simulating...', time.time()

    rand = randint(0,8)



    if 0 <= rand <= 4:
        print 'fastqc'
        m = Tools.FastQC(fqset[rand])
        n = m.run()

    else:
        pass

    if 0 <= rand <= 1:
        print 'dnalettercount'

        m1 = Tools.DNALetterCount(dnaset[rand])
        a, c, t, g, n = m1.run()

    elif 2 <= rand <= 3:
        print 'dnalettercount entropy'

        m1 = Tools.DNALetterCount(dnaset[rand])
        a, c, t, g, n = m1.run()

        m2 = Tools.Entropy(a, c, t, g)
        ent = m2.run()

    elif 4 <= rand <= 7:
        print 'dnalettercount entropy maxminprob'

        m1 = Tools.DNALetterCount(dnaset[rand%4])
        a, c, t, g, n = m1.run()

        m2 = Tools.Entropy(a, c, t, g)
        ent = m2.run()

        m3 = Tools.MaxMinProb(a, c, t, g)
        maxbase, minbase = m3.run()

    else:
        print 'div'

        m = Tools.Div().run()