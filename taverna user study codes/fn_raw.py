def removespace(in1):
    # taking input filename as parameter
    f = open(in1)

    # function logic
    out = open('noSpace.txt', 'w')

    for line in f:
        for word in line:
            for letter in word:
                if letter == ' ':
                    pass
                else:
                    out.write(letter)

    # return output filename
    return out.name


