import time

def parse():
    print 'parsing...'
    ''' GDB part '''
    from py2neo import Graph

    import Queries

    graph  = Graph(password = 'password')

    query = Queries.get_all_modules

    data = graph.run(query)

    usage = []
    mapping = {}

    for d in data:
        target = d['n']['NAME']
        if target in mapping:
            mapping[target] = mapping[target]+1
        else:
            mapping[target] = 1

    print mapping

    f = open('data/viz.tsv', 'w')

    f.write('Tools\tFrequency\n')

    for k in mapping:
        f.write(k + '\t' + str(mapping[k]) + '\n')

    f.close()

while True:
    time.sleep(1)
    parse()