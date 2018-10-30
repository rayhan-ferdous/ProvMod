def start_raw(in1):
    import time

    millis = int(round(time.time() * 1000))

    f = open('/home/aapon/taverna/time.csv', 'a')

    f.write(str(millis) + ',')

    return in1


def cr_to_csv_raw(bedfile):
    filename = bedfile

    with open(filename, 'r') as f:

        out = open(bedfile[:-4] + '.csv', 'w')
        out.write(
            'exonchrome,exonstart,exonend,exonid,exonval,exonsign,snpchrome,snpstart,snpend,snpid,snpval,snpsign\n')

        for line in f:
            full_line = []
            for data in line.split('\t'):
                full_line.append(data)

            out.write(','.join(full_line) + '\n')


    return out.name

def count_raw(filename, target_id):
    import pandas as pd

    df = pd.read_csv(filename)
    t = target_id

    d = {}

    for i, r in df.iterrows():
        k = r[t]

        if k not in d:
            d[k] = 1
        else:
            d[k] = d[k] + 1

    out = open(t + '_count_index.csv', 'w')
    out.write('id,count\n')

    for k in d:
        out.write(str(k) + ',' + str(d[k]) + '\n')

    return out.name

def top_k_raw(in1):
    import pandas as pd

    df = pd.read_csv(in1)

    srt = df.sort_values('count', ascending=False).head(10)

    out = open('top_10_' + in1[:-4] + '.csv', 'w')

    srt.to_csv(out)

    return out.name

def show_raw(in1):
    import sys
    f = open(in1)

    for line in f:
        sys.stdout.write(line)

    return '---'


def end_raw(in1):

    import time

    millis = int(round(time.time() * 1000))

    f = open('/home/aapon/taverna/time.csv', 'a')

    f.write(str(millis) + '\n')

    return 'success!'
