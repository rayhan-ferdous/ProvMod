from py2neo import Graph
graph  = Graph(password = 'password')
graph.delete_all()

f = open('bioblend.xml', 'r')

clones = []

for line in f:
    if '<source file=' in line:
        coms = line.split()

        fname = coms[1][6:-1]
        start = coms[2][11:-1]
        end = coms[3][9:-1]
        pcid = coms[4][6:-11]

        clones.append( (fname, start, end, pcid) )

for i in range(0, len(clones), 2):
    first = clones[i]
    second = clones[i+1]

    fname1 = first[0]
    start1 = first[1]
    end1 = first[2]
    pcid1 = first[3]


    createnode1 = 'create(n:fragments) set n.file="' + fname1 + '", n.start="' + start1 + '", n.end="' + end1 + '", n.pcid="' + pcid1 + '"'
    graph.run(createnode1)


    fname2 = second[0]
    start2 = second[1]
    end2 = second[2]
    pcid2 = second[3]

    createnode2 = 'create(n:fragments) set n.file="' + fname2 + '", n.start="' + start2 + '", n.end="' + end2 + '", n.pcid="' + pcid2 + '"'
    graph.run(createnode2)



for i in range(0, len(clones), 2):
    first = clones[i]
    second = clones[i+1]

    pcid1 = first[3]
    pcid2 = second[3]

    createrelation = 'match(n1), (n2) where n1.pcid="' + pcid1 + '" and n2.pcid="' + pcid2 + '" create (n1)-[:cloneof]->(n2)'
    graph.run(createrelation)




