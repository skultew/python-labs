a = [1, 324, 112, 2356, 1124, 5467, 11234, 1231, 54]
result = []
def more(list):
    for i in range(len(list)):
        if list[i] > list[i - 1]:
            result.append(list[i])
    print(result)
more(a)
