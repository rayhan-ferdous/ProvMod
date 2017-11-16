def Flatten(*args):

    flat_list = []

    for i in args:
        if i is not None:
            flat_list.append(i)

    return  flat_list
