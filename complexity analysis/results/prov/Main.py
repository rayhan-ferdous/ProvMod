from ProvModel import Object, File, Module
import Tools
from random import randint
import time

result = open('prov.csv', 'w')

for i in range(0, 50):
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


    mcount = Tools.DNALetterCount(dna0)
    r1, r2, r3, r4, r5 = mcount.run()

    mentropy = Tools.Entropy(r1, r2, r3, r4)

    r = mentropy.run()

    mcount = Tools.DNALetterCount(dna1)
    r1, r2, r3, r4, r5 = mcount.run()

    mentropy = Tools.Entropy(r1, r2, r3, r4)

    r = mentropy.run()

    mcount = Tools.DNALetterCount(dna2)
    r1, r2, r3, r4, r5 = mcount.run()

    mentropy = Tools.Entropy(r1, r2, r3, r4)

    r = mentropy.run()

    mcount = Tools.DNALetterCount(dna3)
    r1, r2, r3, r4, r5 = mcount.run()

    mentropy = Tools.Entropy(r1, r2, r3, r4)

    r = mentropy.run()


    duration = time.time() - start_time
    result.write(str(duration) + '\n')