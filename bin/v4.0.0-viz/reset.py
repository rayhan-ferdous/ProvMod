from py2neo import Graph

graph  = Graph(password = 'password')

graph.delete_all()


open('workflow.log', 'w').close()

