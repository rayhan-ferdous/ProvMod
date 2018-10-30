import sys




filename = sys.argv[1]


with open(filename, 'r') as f:

    out = open(sys.argv[1][:-4] + '.csv', 'w')
    out.write('exonchrome,exonstart,exonend,exonid,exonval,exonsign,snpchrome,snpstart,snpend,snpid,snpval,snpsign\n')

    for line in f:
        full_line = []
        for data in line.split('\t'):
            full_line.append(data)

        #print full_line
        out.write(','.join(full_line)+'\n')

        #print ','.join(full_line)+'\n'
        #break


sys.stdout.write( sys.argv[1][:-4] + '.csv' )
