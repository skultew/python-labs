def counting_zero(com):
    a = 0
    for i in range(len(com)):
        if com[i] == 0:
            a += 1
            return a
com = list()
for i in range(10):
    com.append(int(input()))

print(counting_zero(com))
