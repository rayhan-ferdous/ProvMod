def get_all_nodes():
    pass

def get_all_object():
    query = 'match (n:Object) return n'

    return query

def get_all_file():
    query = 'match(n:File) return n'

    return query

def get_all_module():
    query = 'match (n:Module) return n'

    return query


def get_node(**kwargs):
    pass

def get_object(**kwargs):
    where_clauses = []

    for k in kwargs:
        where_clauses.append('n.' + str(k) + ' = ' + str(kwargs[k]))

    where_full = ' and '.join(where_clauses)

    query = 'match(n:Object) ' + where_full + ' return n'

    return query

def get_file(**kwargs):
    where_clauses = []

    for k in kwargs:
        where_clauses.append('n.' + str(k) + ' = ' + str(kwargs[k]))

    where_full = ' and '.join(where_clauses)

    query = 'match(n:File) ' + where_full + ' return n'

    return query

def get_module(**kwargs):
    pass



def get_object_source(**kwargs):
    pass

def get_object_destination(**kwargs):
    pass

def get_file_source(**kwargs):
    pass

def get_file_destination(**kwargs):
    pass



def get_module_input(**kwargs):
    pass

def get_module_output(**kwargs):
    pass


def get_node_property(**kwargs):
    pass

def get_object_property(**kwargs):
    pass

def get_file_property(**kwargs):
    pass

def get_module_property(**kwargs):
    pass



def get_all_node_frequency():
    pass

def get_all_object_frequency():
    pass

def get_all_file_frequency():
    pass

def get_all_module_frequency():
    pass


def get_node_frequency(**kwargs):
    pass

def get_object_frequency(**kwargs):
    pass

def get_file_frequency(**kwargs):
    pass

def get_module_frequency(**kwargs):
    pass

def get_object_property_frequency(**kwargs):
    pass

def get_file_property_frequency(**kwargs):
    pass

def get_module_property_frequency(**kwargs):
    pass


def get_node_timeseries(start, end, **kwargs):
    pass









