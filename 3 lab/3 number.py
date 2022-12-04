def stairs(com):
    for i in range(1, com + 1):
        a = ''
        for j in range(1, i + 1):
            a = a + str(j)
        print(a)
    return 'End'
com = 0
com = int(input())

print(stairs(com))
