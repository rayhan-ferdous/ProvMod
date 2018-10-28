py2neo=3.1.2 or 3.x.x with latest

reducer query

match(n1:Object), (n2:Object) where n1.time<n2.time and n1.VALUE=n2.VALUE create (n1)-[r:FLOW]->(n2)