from ProvModel import Object, File, Module
import Tools
from random import randint
import time
from py2neo import Graph

graph  = Graph(password = 'password')

result = open('time vs nodes.csv', 'w')

for i in range(0, 500):
    print 'step', i
    start_time = time.time()

    fq0 = File(open('gene/fq0.fq'))
    fq1 = File(open('gene/fq1.bed'))
    fq2 = File(open('gene/fq2.fa'))
    fq3 = File(open('gene/fq3.fastq'))
    fq4 = File(open('gene/fq4.fastq'))

    dna0 = File(open('gene/dna0.txt'))
    dna1 = File(open('gene/dna1.txt'))
    dna2 = File(open('gene/dna2.txt'))
    dna3 = File(open('gene/dna3.txt'))

    '''
    mfq = Tools.FastQC(fq0)
    r1, r2 = mfq.run()

    mfq = Tools.FastQC(fq1)
    r = mfq.run()

    mfq = Tools.FastQC(fq2)
    r = mfq.run()

    mfq = Tools.FastQC(fq3)
    r = mfq.run()

    mfq = Tools.FastQC(fq4)
    r = mfq.run()
    '''

    mcount = Tools.DNALetterCount(dna0)
    r1, r2, r3, r4, r5 = mcount.run()

    mentropy = Tools.Entropy(r1, r2, r3, r4)

    mcount = Tools.DNALetterCount(dna1)
    r1, r2, r3, r4, r5 = mcount.run()

    mentropy = Tools.Entropy(r1, r2, r3, r4)

    mcount = Tools.DNALetterCount(dna2)
    r1, r2, r3, r4, r5 = mcount.run()

    mentropy = Tools.Entropy(r1, r2, r3, r4)

    mcount = Tools.DNALetterCount(dna3)
    r1, r2, r3, r4, r5 = mcount.run()

    mentropy = Tools.Entropy(r1, r2, r3, r4)


    duration = time.time() - start_time

    query = 'MATCH (n) RETURN count(*)'
    data = graph.run(query)

    nodes = 0
    for k in data:
        nodes = k[0]




    print duration, nodes
    result.write(str(duration) + ',' + str(nodes) + '\n')

