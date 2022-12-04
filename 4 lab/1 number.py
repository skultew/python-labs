list = [45, 23, 10, 11, 4, 220, 532, 2]


def var(list):
    l = []
    for index in list:
        if index % 2 == 0:
            l.append(index)
        
    return l
print(var(list))
