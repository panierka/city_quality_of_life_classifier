def fom(x: list):
    tmp = x[0]
    index = 0
    for i in range(len(x)):
        if tmp < x[i]:
            index = i
            tmp = x[i]
    return index


def lom(x: list):
    tmp = x[0]
    index = 0
    for i in range(len(x)):
        if tmp <= x[i]:
            index = i
            tmp = x[i]
    return index


def centroid(x: list):
    pass
